package main

import (
	"encoding/json"
	"log"
	"time"

	"github.com/hippoai/goutil"
	pb "github.com/hippoai/later/_proto"
	"github.com/hippoai/later/tasks/echo"
	"golang.org/x/net/context"
	"google.golang.org/grpc"
)

var grpc_address = "localhost:9081"

func get_instances() {

	// Create gRPC connection
	conn, err := grpc.Dial(grpc_address, grpc.WithInsecure())
	if err != nil {
		log.Fatal(err)
	}
	defer conn.Close()

	client := pb.NewLaterClient(conn)

	out, err := client.GetInstances(context.Background(), &pb.GetInstancesInput{
		Start: time.Now().UTC().Add(-10 * time.Minute).Format(time.RFC3339),
		End:   time.Now().UTC().Add(10 * time.Minute).Format(time.RFC3339),
	})
	if err != nil {
		log.Fatal(err)
	}

	instances := out.GetInstances()

	for _, instance := range instances {
		log.Println(instance.GetId(), instance.GetExecutionTime(), instance.GetTaskName(), string(instance.GetParameters()))
	}

}

func get_successful() {

	// Create gRPC connection
	conn, err := grpc.Dial(grpc_address, grpc.WithInsecure())
	if err != nil {
		log.Fatal(err)
	}
	defer conn.Close()

	client := pb.NewLaterClient(conn)

	out, err := client.GetSuccessful(context.Background(), &pb.GetInstancesInput{
		Start: "2017-08-06T05:15:08Z",
		End:   time.Now().UTC().Add(10 * time.Minute).Format(time.RFC3339),
	})
	if err != nil {
		log.Fatal(err)
	}

	instances := out.GetInstances()

	for _, instance := range instances {
		log.Println(instance.GetId(), instance.GetExecutionTime(), instance.GetTaskName(), string(instance.GetParameters()))
	}

}

func add_instance() string {

	// Create gRPC connection
	conn, err := grpc.Dial(grpc_address, grpc.WithInsecure())
	if err != nil {
		log.Fatal(err)
	}
	defer conn.Close()

	client := pb.NewLaterClient(conn)

	msg := "Hello world!"
	parameters := &echo.Parameters{
		Message: &msg,
	}
	b, _ := json.Marshal(parameters)

	out, err := client.CreateInstance(context.Background(), &pb.CreateInstanceInput{
		TaskName:      "echo",
		ExecutionTime: time.Now().Add(20 * time.Second).Format(time.RFC3339),
		Parameters:    b,
	})

	if err != nil {
		log.Fatal(err)
	}

	log.Println(goutil.Pretty(out))

	return out.GetInstanceId()

}

func abort_instance(instanceID string) {

	// Create gRPC connection
	conn, err := grpc.Dial(grpc_address, grpc.WithInsecure())
	if err != nil {
		log.Fatal(err)
	}
	defer conn.Close()

	client := pb.NewLaterClient(conn)

	out, err := client.AbortInstance(context.Background(), &pb.AbortInstanceInput{
		TaskName:   "echo",
		InstanceId: instanceID,
	})

	if err != nil {
		log.Fatal(err)
	}

	log.Println(goutil.Pretty(out))

}

func stats() {

	// Create gRPC connection
	conn, err := grpc.Dial(grpc_address, grpc.WithInsecure())
	if err != nil {
		log.Fatal(err)
	}
	defer conn.Close()

	client := pb.NewLaterClient(conn)

	out, err := client.Stats(context.Background(), &pb.StatsInput{})

	if err != nil {
		log.Fatal(err)
	}

	log.Println(goutil.Pretty(out.GetNInMemory()))

}
func main() {

	instanceID := add_instance()
	get_instances()
	get_successful()

	time.Sleep(1 * time.Second)
	abort_instance(instanceID)
	stats()

}
