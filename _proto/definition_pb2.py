# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: definition.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='definition.proto',
  package='hippoai.later',
  syntax='proto3',
  serialized_pb=_b('\n\x10\x64\x65\x66inition.proto\x12\rhippoai.later\x1a\x1cgoogle/api/annotations.proto\"U\n\x08Instance\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\ttask_name\x18\x02 \x01(\t\x12\x16\n\x0e\x65xecution_time\x18\x03 \x01(\t\x12\x12\n\nparameters\x18\x04 \x01(\x0c\"T\n\x13\x43reateInstanceInput\x12\x11\n\ttask_name\x18\x01 \x01(\t\x12\x16\n\x0e\x65xecution_time\x18\x02 \x01(\t\x12\x12\n\nparameters\x18\x03 \x01(\x0c\"+\n\x14\x43reateInstanceOutput\x12\x13\n\x0binstance_id\x18\x01 \x01(\t\"<\n\x12\x41\x62ortInstanceInput\x12\x11\n\ttask_name\x18\x01 \x01(\t\x12\x13\n\x0binstance_id\x18\x02 \x01(\t\"\x15\n\x13\x41\x62ortInstanceOutput\"/\n\x11GetInstancesInput\x12\r\n\x05start\x18\x01 \x01(\t\x12\x0b\n\x03\x65nd\x18\x02 \x01(\t\"@\n\x12GetInstancesOutput\x12*\n\tinstances\x18\x01 \x03(\x0b\x32\x17.hippoai.later.Instance\"\x0c\n\nStatsInput\"@\n\x0bStatsOutput\x12\r\n\x05token\x18\x01 \x01(\t\x12\x13\n\x0bn_in_memory\x18\x02 \x01(\x03\x12\r\n\x05tasks\x18\x03 \x03(\t2\xfe\x05\n\x05Later\x12v\n\x0e\x43reateInstance\x12\".hippoai.later.CreateInstanceInput\x1a#.hippoai.later.CreateInstanceOutput\"\x1b\x82\xd3\xe4\x93\x02\x15\"\x10/create_instance:\x01*\x12r\n\rAbortInstance\x12!.hippoai.later.AbortInstanceInput\x1a\".hippoai.later.AbortInstanceOutput\"\x1a\x82\xd3\xe4\x93\x02\x14\"\x0f/abort_instance:\x01*\x12n\n\x0cGetInstances\x12 .hippoai.later.GetInstancesInput\x1a!.hippoai.later.GetInstancesOutput\"\x19\x82\xd3\xe4\x93\x02\x13\"\x0e/get_instances:\x01*\x12p\n\rGetSuccessful\x12 .hippoai.later.GetInstancesInput\x1a!.hippoai.later.GetInstancesOutput\"\x1a\x82\xd3\xe4\x93\x02\x14\"\x0f/get_successful:\x01*\x12h\n\tGetFailed\x12 .hippoai.later.GetInstancesInput\x1a!.hippoai.later.GetInstancesOutput\"\x16\x82\xd3\xe4\x93\x02\x10\"\x0b/get_failed:\x01*\x12j\n\nGetAborted\x12 .hippoai.later.GetInstancesInput\x1a!.hippoai.later.GetInstancesOutput\"\x17\x82\xd3\xe4\x93\x02\x11\"\x0c/get_aborted:\x01*\x12Q\n\x05Stats\x12\x19.hippoai.later.StatsInput\x1a\x1a.hippoai.later.StatsOutput\"\x11\x82\xd3\xe4\x93\x02\x0b\"\x06/stats:\x01*B!Z\x1fgithub.com/hippoai/later/_protob\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_INSTANCE = _descriptor.Descriptor(
  name='Instance',
  full_name='hippoai.later.Instance',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='hippoai.later.Instance.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='task_name', full_name='hippoai.later.Instance.task_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='execution_time', full_name='hippoai.later.Instance.execution_time', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parameters', full_name='hippoai.later.Instance.parameters', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=65,
  serialized_end=150,
)


_CREATEINSTANCEINPUT = _descriptor.Descriptor(
  name='CreateInstanceInput',
  full_name='hippoai.later.CreateInstanceInput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='task_name', full_name='hippoai.later.CreateInstanceInput.task_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='execution_time', full_name='hippoai.later.CreateInstanceInput.execution_time', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parameters', full_name='hippoai.later.CreateInstanceInput.parameters', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=152,
  serialized_end=236,
)


_CREATEINSTANCEOUTPUT = _descriptor.Descriptor(
  name='CreateInstanceOutput',
  full_name='hippoai.later.CreateInstanceOutput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance_id', full_name='hippoai.later.CreateInstanceOutput.instance_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=238,
  serialized_end=281,
)


_ABORTINSTANCEINPUT = _descriptor.Descriptor(
  name='AbortInstanceInput',
  full_name='hippoai.later.AbortInstanceInput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='task_name', full_name='hippoai.later.AbortInstanceInput.task_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='instance_id', full_name='hippoai.later.AbortInstanceInput.instance_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=283,
  serialized_end=343,
)


_ABORTINSTANCEOUTPUT = _descriptor.Descriptor(
  name='AbortInstanceOutput',
  full_name='hippoai.later.AbortInstanceOutput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=345,
  serialized_end=366,
)


_GETINSTANCESINPUT = _descriptor.Descriptor(
  name='GetInstancesInput',
  full_name='hippoai.later.GetInstancesInput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start', full_name='hippoai.later.GetInstancesInput.start', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end', full_name='hippoai.later.GetInstancesInput.end', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=368,
  serialized_end=415,
)


_GETINSTANCESOUTPUT = _descriptor.Descriptor(
  name='GetInstancesOutput',
  full_name='hippoai.later.GetInstancesOutput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instances', full_name='hippoai.later.GetInstancesOutput.instances', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=417,
  serialized_end=481,
)


_STATSINPUT = _descriptor.Descriptor(
  name='StatsInput',
  full_name='hippoai.later.StatsInput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=483,
  serialized_end=495,
)


_STATSOUTPUT = _descriptor.Descriptor(
  name='StatsOutput',
  full_name='hippoai.later.StatsOutput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='hippoai.later.StatsOutput.token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='n_in_memory', full_name='hippoai.later.StatsOutput.n_in_memory', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tasks', full_name='hippoai.later.StatsOutput.tasks', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=497,
  serialized_end=561,
)

_GETINSTANCESOUTPUT.fields_by_name['instances'].message_type = _INSTANCE
DESCRIPTOR.message_types_by_name['Instance'] = _INSTANCE
DESCRIPTOR.message_types_by_name['CreateInstanceInput'] = _CREATEINSTANCEINPUT
DESCRIPTOR.message_types_by_name['CreateInstanceOutput'] = _CREATEINSTANCEOUTPUT
DESCRIPTOR.message_types_by_name['AbortInstanceInput'] = _ABORTINSTANCEINPUT
DESCRIPTOR.message_types_by_name['AbortInstanceOutput'] = _ABORTINSTANCEOUTPUT
DESCRIPTOR.message_types_by_name['GetInstancesInput'] = _GETINSTANCESINPUT
DESCRIPTOR.message_types_by_name['GetInstancesOutput'] = _GETINSTANCESOUTPUT
DESCRIPTOR.message_types_by_name['StatsInput'] = _STATSINPUT
DESCRIPTOR.message_types_by_name['StatsOutput'] = _STATSOUTPUT

Instance = _reflection.GeneratedProtocolMessageType('Instance', (_message.Message,), dict(
  DESCRIPTOR = _INSTANCE,
  __module__ = 'definition_pb2'
  # @@protoc_insertion_point(class_scope:hippoai.later.Instance)
  ))
_sym_db.RegisterMessage(Instance)

CreateInstanceInput = _reflection.GeneratedProtocolMessageType('CreateInstanceInput', (_message.Message,), dict(
  DESCRIPTOR = _CREATEINSTANCEINPUT,
  __module__ = 'definition_pb2'
  # @@protoc_insertion_point(class_scope:hippoai.later.CreateInstanceInput)
  ))
_sym_db.RegisterMessage(CreateInstanceInput)

CreateInstanceOutput = _reflection.GeneratedProtocolMessageType('CreateInstanceOutput', (_message.Message,), dict(
  DESCRIPTOR = _CREATEINSTANCEOUTPUT,
  __module__ = 'definition_pb2'
  # @@protoc_insertion_point(class_scope:hippoai.later.CreateInstanceOutput)
  ))
_sym_db.RegisterMessage(CreateInstanceOutput)

AbortInstanceInput = _reflection.GeneratedProtocolMessageType('AbortInstanceInput', (_message.Message,), dict(
  DESCRIPTOR = _ABORTINSTANCEINPUT,
  __module__ = 'definition_pb2'
  # @@protoc_insertion_point(class_scope:hippoai.later.AbortInstanceInput)
  ))
_sym_db.RegisterMessage(AbortInstanceInput)

AbortInstanceOutput = _reflection.GeneratedProtocolMessageType('AbortInstanceOutput', (_message.Message,), dict(
  DESCRIPTOR = _ABORTINSTANCEOUTPUT,
  __module__ = 'definition_pb2'
  # @@protoc_insertion_point(class_scope:hippoai.later.AbortInstanceOutput)
  ))
_sym_db.RegisterMessage(AbortInstanceOutput)

GetInstancesInput = _reflection.GeneratedProtocolMessageType('GetInstancesInput', (_message.Message,), dict(
  DESCRIPTOR = _GETINSTANCESINPUT,
  __module__ = 'definition_pb2'
  # @@protoc_insertion_point(class_scope:hippoai.later.GetInstancesInput)
  ))
_sym_db.RegisterMessage(GetInstancesInput)

GetInstancesOutput = _reflection.GeneratedProtocolMessageType('GetInstancesOutput', (_message.Message,), dict(
  DESCRIPTOR = _GETINSTANCESOUTPUT,
  __module__ = 'definition_pb2'
  # @@protoc_insertion_point(class_scope:hippoai.later.GetInstancesOutput)
  ))
_sym_db.RegisterMessage(GetInstancesOutput)

StatsInput = _reflection.GeneratedProtocolMessageType('StatsInput', (_message.Message,), dict(
  DESCRIPTOR = _STATSINPUT,
  __module__ = 'definition_pb2'
  # @@protoc_insertion_point(class_scope:hippoai.later.StatsInput)
  ))
_sym_db.RegisterMessage(StatsInput)

StatsOutput = _reflection.GeneratedProtocolMessageType('StatsOutput', (_message.Message,), dict(
  DESCRIPTOR = _STATSOUTPUT,
  __module__ = 'definition_pb2'
  # @@protoc_insertion_point(class_scope:hippoai.later.StatsOutput)
  ))
_sym_db.RegisterMessage(StatsOutput)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z\037github.com/hippoai/later/_proto'))
try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities


  class LaterStub(object):

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.CreateInstance = channel.unary_unary(
          '/hippoai.later.Later/CreateInstance',
          request_serializer=CreateInstanceInput.SerializeToString,
          response_deserializer=CreateInstanceOutput.FromString,
          )
      self.AbortInstance = channel.unary_unary(
          '/hippoai.later.Later/AbortInstance',
          request_serializer=AbortInstanceInput.SerializeToString,
          response_deserializer=AbortInstanceOutput.FromString,
          )
      self.GetInstances = channel.unary_unary(
          '/hippoai.later.Later/GetInstances',
          request_serializer=GetInstancesInput.SerializeToString,
          response_deserializer=GetInstancesOutput.FromString,
          )
      self.GetSuccessful = channel.unary_unary(
          '/hippoai.later.Later/GetSuccessful',
          request_serializer=GetInstancesInput.SerializeToString,
          response_deserializer=GetInstancesOutput.FromString,
          )
      self.GetFailed = channel.unary_unary(
          '/hippoai.later.Later/GetFailed',
          request_serializer=GetInstancesInput.SerializeToString,
          response_deserializer=GetInstancesOutput.FromString,
          )
      self.GetAborted = channel.unary_unary(
          '/hippoai.later.Later/GetAborted',
          request_serializer=GetInstancesInput.SerializeToString,
          response_deserializer=GetInstancesOutput.FromString,
          )
      self.Stats = channel.unary_unary(
          '/hippoai.later.Later/Stats',
          request_serializer=StatsInput.SerializeToString,
          response_deserializer=StatsOutput.FromString,
          )


  class LaterServicer(object):

    def CreateInstance(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def AbortInstance(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def GetInstances(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def GetSuccessful(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def GetFailed(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def GetAborted(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def Stats(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_LaterServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'CreateInstance': grpc.unary_unary_rpc_method_handler(
            servicer.CreateInstance,
            request_deserializer=CreateInstanceInput.FromString,
            response_serializer=CreateInstanceOutput.SerializeToString,
        ),
        'AbortInstance': grpc.unary_unary_rpc_method_handler(
            servicer.AbortInstance,
            request_deserializer=AbortInstanceInput.FromString,
            response_serializer=AbortInstanceOutput.SerializeToString,
        ),
        'GetInstances': grpc.unary_unary_rpc_method_handler(
            servicer.GetInstances,
            request_deserializer=GetInstancesInput.FromString,
            response_serializer=GetInstancesOutput.SerializeToString,
        ),
        'GetSuccessful': grpc.unary_unary_rpc_method_handler(
            servicer.GetSuccessful,
            request_deserializer=GetInstancesInput.FromString,
            response_serializer=GetInstancesOutput.SerializeToString,
        ),
        'GetFailed': grpc.unary_unary_rpc_method_handler(
            servicer.GetFailed,
            request_deserializer=GetInstancesInput.FromString,
            response_serializer=GetInstancesOutput.SerializeToString,
        ),
        'GetAborted': grpc.unary_unary_rpc_method_handler(
            servicer.GetAborted,
            request_deserializer=GetInstancesInput.FromString,
            response_serializer=GetInstancesOutput.SerializeToString,
        ),
        'Stats': grpc.unary_unary_rpc_method_handler(
            servicer.Stats,
            request_deserializer=StatsInput.FromString,
            response_serializer=StatsOutput.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'hippoai.later.Later', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaLaterServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    def CreateInstance(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def AbortInstance(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def GetInstances(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def GetSuccessful(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def GetFailed(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def GetAborted(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def Stats(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaLaterStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    def CreateInstance(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    CreateInstance.future = None
    def AbortInstance(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    AbortInstance.future = None
    def GetInstances(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    GetInstances.future = None
    def GetSuccessful(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    GetSuccessful.future = None
    def GetFailed(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    GetFailed.future = None
    def GetAborted(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    GetAborted.future = None
    def Stats(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    Stats.future = None


  def beta_create_Later_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('hippoai.later.Later', 'AbortInstance'): AbortInstanceInput.FromString,
      ('hippoai.later.Later', 'CreateInstance'): CreateInstanceInput.FromString,
      ('hippoai.later.Later', 'GetAborted'): GetInstancesInput.FromString,
      ('hippoai.later.Later', 'GetFailed'): GetInstancesInput.FromString,
      ('hippoai.later.Later', 'GetInstances'): GetInstancesInput.FromString,
      ('hippoai.later.Later', 'GetSuccessful'): GetInstancesInput.FromString,
      ('hippoai.later.Later', 'Stats'): StatsInput.FromString,
    }
    response_serializers = {
      ('hippoai.later.Later', 'AbortInstance'): AbortInstanceOutput.SerializeToString,
      ('hippoai.later.Later', 'CreateInstance'): CreateInstanceOutput.SerializeToString,
      ('hippoai.later.Later', 'GetAborted'): GetInstancesOutput.SerializeToString,
      ('hippoai.later.Later', 'GetFailed'): GetInstancesOutput.SerializeToString,
      ('hippoai.later.Later', 'GetInstances'): GetInstancesOutput.SerializeToString,
      ('hippoai.later.Later', 'GetSuccessful'): GetInstancesOutput.SerializeToString,
      ('hippoai.later.Later', 'Stats'): StatsOutput.SerializeToString,
    }
    method_implementations = {
      ('hippoai.later.Later', 'AbortInstance'): face_utilities.unary_unary_inline(servicer.AbortInstance),
      ('hippoai.later.Later', 'CreateInstance'): face_utilities.unary_unary_inline(servicer.CreateInstance),
      ('hippoai.later.Later', 'GetAborted'): face_utilities.unary_unary_inline(servicer.GetAborted),
      ('hippoai.later.Later', 'GetFailed'): face_utilities.unary_unary_inline(servicer.GetFailed),
      ('hippoai.later.Later', 'GetInstances'): face_utilities.unary_unary_inline(servicer.GetInstances),
      ('hippoai.later.Later', 'GetSuccessful'): face_utilities.unary_unary_inline(servicer.GetSuccessful),
      ('hippoai.later.Later', 'Stats'): face_utilities.unary_unary_inline(servicer.Stats),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_Later_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('hippoai.later.Later', 'AbortInstance'): AbortInstanceInput.SerializeToString,
      ('hippoai.later.Later', 'CreateInstance'): CreateInstanceInput.SerializeToString,
      ('hippoai.later.Later', 'GetAborted'): GetInstancesInput.SerializeToString,
      ('hippoai.later.Later', 'GetFailed'): GetInstancesInput.SerializeToString,
      ('hippoai.later.Later', 'GetInstances'): GetInstancesInput.SerializeToString,
      ('hippoai.later.Later', 'GetSuccessful'): GetInstancesInput.SerializeToString,
      ('hippoai.later.Later', 'Stats'): StatsInput.SerializeToString,
    }
    response_deserializers = {
      ('hippoai.later.Later', 'AbortInstance'): AbortInstanceOutput.FromString,
      ('hippoai.later.Later', 'CreateInstance'): CreateInstanceOutput.FromString,
      ('hippoai.later.Later', 'GetAborted'): GetInstancesOutput.FromString,
      ('hippoai.later.Later', 'GetFailed'): GetInstancesOutput.FromString,
      ('hippoai.later.Later', 'GetInstances'): GetInstancesOutput.FromString,
      ('hippoai.later.Later', 'GetSuccessful'): GetInstancesOutput.FromString,
      ('hippoai.later.Later', 'Stats'): StatsOutput.FromString,
    }
    cardinalities = {
      'AbortInstance': cardinality.Cardinality.UNARY_UNARY,
      'CreateInstance': cardinality.Cardinality.UNARY_UNARY,
      'GetAborted': cardinality.Cardinality.UNARY_UNARY,
      'GetFailed': cardinality.Cardinality.UNARY_UNARY,
      'GetInstances': cardinality.Cardinality.UNARY_UNARY,
      'GetSuccessful': cardinality.Cardinality.UNARY_UNARY,
      'Stats': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'hippoai.later.Later', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
