package later

import (
	"time"

	"github.com/hippoai/later/structures"
)

// Database lists what the database needs to be able to do for this library
type Database interface {
	AbortInstances(taskName string, parameters []byte) ([]string, error)
	CreateInstance(taskName string, executionTime time.Time, parameters []byte) (string, error)
	GetInstances(start, end time.Time) ([]*structures.Instance, error)
	GetLastPullTime() (*time.Time, error)
	SetPullTime(t time.Time) error
}
