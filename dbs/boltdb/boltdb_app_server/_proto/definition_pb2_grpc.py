# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import definition_pb2 as definition__pb2


class LaterBoltDBStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.AbortInstance = channel.unary_unary(
        '/hippoai.later.bolt.LaterBoltDB/AbortInstance',
        request_serializer=definition__pb2.AbortInstanceInput.SerializeToString,
        response_deserializer=definition__pb2.AbortInstanceOutput.FromString,
        )
    self.CreateInstance = channel.unary_unary(
        '/hippoai.later.bolt.LaterBoltDB/CreateInstance',
        request_serializer=definition__pb2.CreateInstanceInput.SerializeToString,
        response_deserializer=definition__pb2.CreateInstanceOutput.FromString,
        )
    self.GetInstances = channel.unary_unary(
        '/hippoai.later.bolt.LaterBoltDB/GetInstances',
        request_serializer=definition__pb2.GetInstancesInput.SerializeToString,
        response_deserializer=definition__pb2.GetInstancesOutput.FromString,
        )
    self.GetLastPullTime = channel.unary_unary(
        '/hippoai.later.bolt.LaterBoltDB/GetLastPullTime',
        request_serializer=definition__pb2.GetLastPullTimeInput.SerializeToString,
        response_deserializer=definition__pb2.GetLastPullTimeOutput.FromString,
        )
    self.MarkAsSuccessful = channel.unary_unary(
        '/hippoai.later.bolt.LaterBoltDB/MarkAsSuccessful',
        request_serializer=definition__pb2.MarkAsSuccessfulInput.SerializeToString,
        response_deserializer=definition__pb2.MarkAsSuccessfulOutput.FromString,
        )
    self.MarkAsFailed = channel.unary_unary(
        '/hippoai.later.bolt.LaterBoltDB/MarkAsFailed',
        request_serializer=definition__pb2.MarkAsFailedInput.SerializeToString,
        response_deserializer=definition__pb2.MarkAsFailedOutput.FromString,
        )
    self.SetPullTime = channel.unary_unary(
        '/hippoai.later.bolt.LaterBoltDB/SetPullTime',
        request_serializer=definition__pb2.SetPullTimeInput.SerializeToString,
        response_deserializer=definition__pb2.SetPullTimeOutput.FromString,
        )


class LaterBoltDBServicer(object):

  def AbortInstance(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateInstance(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetInstances(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetLastPullTime(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MarkAsSuccessful(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MarkAsFailed(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetPullTime(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_LaterBoltDBServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'AbortInstance': grpc.unary_unary_rpc_method_handler(
          servicer.AbortInstance,
          request_deserializer=definition__pb2.AbortInstanceInput.FromString,
          response_serializer=definition__pb2.AbortInstanceOutput.SerializeToString,
      ),
      'CreateInstance': grpc.unary_unary_rpc_method_handler(
          servicer.CreateInstance,
          request_deserializer=definition__pb2.CreateInstanceInput.FromString,
          response_serializer=definition__pb2.CreateInstanceOutput.SerializeToString,
      ),
      'GetInstances': grpc.unary_unary_rpc_method_handler(
          servicer.GetInstances,
          request_deserializer=definition__pb2.GetInstancesInput.FromString,
          response_serializer=definition__pb2.GetInstancesOutput.SerializeToString,
      ),
      'GetLastPullTime': grpc.unary_unary_rpc_method_handler(
          servicer.GetLastPullTime,
          request_deserializer=definition__pb2.GetLastPullTimeInput.FromString,
          response_serializer=definition__pb2.GetLastPullTimeOutput.SerializeToString,
      ),
      'MarkAsSuccessful': grpc.unary_unary_rpc_method_handler(
          servicer.MarkAsSuccessful,
          request_deserializer=definition__pb2.MarkAsSuccessfulInput.FromString,
          response_serializer=definition__pb2.MarkAsSuccessfulOutput.SerializeToString,
      ),
      'MarkAsFailed': grpc.unary_unary_rpc_method_handler(
          servicer.MarkAsFailed,
          request_deserializer=definition__pb2.MarkAsFailedInput.FromString,
          response_serializer=definition__pb2.MarkAsFailedOutput.SerializeToString,
      ),
      'SetPullTime': grpc.unary_unary_rpc_method_handler(
          servicer.SetPullTime,
          request_deserializer=definition__pb2.SetPullTimeInput.FromString,
          response_serializer=definition__pb2.SetPullTimeOutput.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'hippoai.later.bolt.LaterBoltDB', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))