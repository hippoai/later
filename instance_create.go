package later

import (
	"time"

	"github.com/hippoai/later/structures"
)

// CreateInstance creates an instance:
// 1 - Store in database
// 2 - Run locally if it's time to
func (machine *Machine) CreateInstance(taskName string, executionTime time.Time, parameters []byte) (*structures.Instance, error) {

	// Store the instance in the database
	instanceID, err := machine.Database.CreateInstance(taskName, executionTime, parameters)
	if err != nil {
		return nil, err
	}

	executionTime = executionTime.UTC()

	instance := &structures.Instance{
		ExecutionTime: executionTime,
		ID:            instanceID,
		Parameters:    parameters,
		TaskName:      taskName,
	}

	// Run it locally if it's in the current timeframe
	timeframeEnd := time.Now().Add(machine.Parameters.TimeAhead)
	if executionTime.Before(timeframeEnd) {
		go func() {
			machine.RunInstanceIfNotAlreadyThere(instance)
		}()
	}

	machine.logger.Log("Created instance %s for task %s, running at %s, with parameters %s",
		instanceID,
		taskName,
		executionTime.Format(time.RFC3339),
		string(parameters),
	)

	return instance, nil

}
