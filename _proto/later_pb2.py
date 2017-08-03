# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: later.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='later.proto',
  package='hippoai.later',
  syntax='proto3',
  serialized_pb=_b('\n\x0blater.proto\x12\rhippoai.later\"U\n\x08Instance\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\ttask_name\x18\x02 \x01(\t\x12\x16\n\x0e\x65xecution_time\x18\x03 \x01(\t\x12\x12\n\nparameters\x18\x04 \x01(\t\"\x18\n\x05\x45rror\x12\x0f\n\x07message\x18\x01 \x01(\t\"Q\n\x10\x41\x64\x64InstanceInput\x12\x11\n\ttask_name\x18\x01 \x01(\t\x12\x16\n\x0e\x65xecution_time\x18\x02 \x01(\t\x12\x12\n\nparameters\x18\x03 \x01(\t\"M\n\x11\x41\x64\x64InstanceOutput\x12\x13\n\x0binstance_id\x18\x01 \x01(\t\x12#\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x14.hippoai.later.Error\"<\n\x13\x41\x62ortInstancesInput\x12\x11\n\ttask_name\x18\x01 \x01(\t\x12\x12\n\nparameters\x18\x02 \x01(\t\"g\n\x14\x41\x62ortInstancesOutput\x12*\n\tinstances\x18\x01 \x03(\x0b\x32\x17.hippoai.later.Instance\x12#\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x14.hippoai.later.Error\"/\n\x11GetInstancesInput\x12\r\n\x05start\x18\x01 \x01(\t\x12\x0b\n\x03\x65nd\x18\x02 \x01(\t\"d\n\x12GetInstancesOutput\x12*\n\tinstances\x18\x01 \x03(\x0b\x32\x17.hippoai.later.Instance\x12\"\n\x04\x65rro\x18\x02 \x01(\x0b\x32\x14.hippoai.later.Error2\x93\x02\n\tMutations\x12R\n\x0b\x41\x64\x64Instance\x12\x1f.hippoai.later.AddInstanceInput\x1a .hippoai.later.AddInstanceOutput\"\x00\x12[\n\x0e\x41\x62ortInstances\x12\".hippoai.later.AbortInstancesInput\x1a#.hippoai.later.AbortInstancesOutput\"\x00\x12U\n\x0cGetInstances\x12 .hippoai.later.GetInstancesInput\x1a!.hippoai.later.GetInstancesOutput\"\x00\x42!Z\x1fgithub.com/hippoai/later/_protob\x06proto3')
)
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
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=30,
  serialized_end=115,
)


_ERROR = _descriptor.Descriptor(
  name='Error',
  full_name='hippoai.later.Error',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='hippoai.later.Error.message', index=0,
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
  serialized_start=117,
  serialized_end=141,
)


_ADDINSTANCEINPUT = _descriptor.Descriptor(
  name='AddInstanceInput',
  full_name='hippoai.later.AddInstanceInput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='task_name', full_name='hippoai.later.AddInstanceInput.task_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='execution_time', full_name='hippoai.later.AddInstanceInput.execution_time', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parameters', full_name='hippoai.later.AddInstanceInput.parameters', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=143,
  serialized_end=224,
)


_ADDINSTANCEOUTPUT = _descriptor.Descriptor(
  name='AddInstanceOutput',
  full_name='hippoai.later.AddInstanceOutput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance_id', full_name='hippoai.later.AddInstanceOutput.instance_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error', full_name='hippoai.later.AddInstanceOutput.error', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=226,
  serialized_end=303,
)


_ABORTINSTANCESINPUT = _descriptor.Descriptor(
  name='AbortInstancesInput',
  full_name='hippoai.later.AbortInstancesInput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='task_name', full_name='hippoai.later.AbortInstancesInput.task_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parameters', full_name='hippoai.later.AbortInstancesInput.parameters', index=1,
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
  serialized_start=305,
  serialized_end=365,
)


_ABORTINSTANCESOUTPUT = _descriptor.Descriptor(
  name='AbortInstancesOutput',
  full_name='hippoai.later.AbortInstancesOutput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instances', full_name='hippoai.later.AbortInstancesOutput.instances', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error', full_name='hippoai.later.AbortInstancesOutput.error', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=367,
  serialized_end=470,
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
  serialized_start=472,
  serialized_end=519,
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
    _descriptor.FieldDescriptor(
      name='erro', full_name='hippoai.later.GetInstancesOutput.erro', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=521,
  serialized_end=621,
)

_ADDINSTANCEOUTPUT.fields_by_name['error'].message_type = _ERROR
_ABORTINSTANCESOUTPUT.fields_by_name['instances'].message_type = _INSTANCE
_ABORTINSTANCESOUTPUT.fields_by_name['error'].message_type = _ERROR
_GETINSTANCESOUTPUT.fields_by_name['instances'].message_type = _INSTANCE
_GETINSTANCESOUTPUT.fields_by_name['erro'].message_type = _ERROR
DESCRIPTOR.message_types_by_name['Instance'] = _INSTANCE
DESCRIPTOR.message_types_by_name['Error'] = _ERROR
DESCRIPTOR.message_types_by_name['AddInstanceInput'] = _ADDINSTANCEINPUT
DESCRIPTOR.message_types_by_name['AddInstanceOutput'] = _ADDINSTANCEOUTPUT
DESCRIPTOR.message_types_by_name['AbortInstancesInput'] = _ABORTINSTANCESINPUT
DESCRIPTOR.message_types_by_name['AbortInstancesOutput'] = _ABORTINSTANCESOUTPUT
DESCRIPTOR.message_types_by_name['GetInstancesInput'] = _GETINSTANCESINPUT
DESCRIPTOR.message_types_by_name['GetInstancesOutput'] = _GETINSTANCESOUTPUT

Instance = _reflection.GeneratedProtocolMessageType('Instance', (_message.Message,), dict(
  DESCRIPTOR = _INSTANCE,
  __module__ = 'later_pb2'
  # @@protoc_insertion_point(class_scope:hippoai.later.Instance)
  ))
_sym_db.RegisterMessage(Instance)

Error = _reflection.GeneratedProtocolMessageType('Error', (_message.Message,), dict(
  DESCRIPTOR = _ERROR,
  __module__ = 'later_pb2'
  # @@protoc_insertion_point(class_scope:hippoai.later.Error)
  ))
_sym_db.RegisterMessage(Error)

AddInstanceInput = _reflection.GeneratedProtocolMessageType('AddInstanceInput', (_message.Message,), dict(
  DESCRIPTOR = _ADDINSTANCEINPUT,
  __module__ = 'later_pb2'
  # @@protoc_insertion_point(class_scope:hippoai.later.AddInstanceInput)
  ))
_sym_db.RegisterMessage(AddInstanceInput)

AddInstanceOutput = _reflection.GeneratedProtocolMessageType('AddInstanceOutput', (_message.Message,), dict(
  DESCRIPTOR = _ADDINSTANCEOUTPUT,
  __module__ = 'later_pb2'
  # @@protoc_insertion_point(class_scope:hippoai.later.AddInstanceOutput)
  ))
_sym_db.RegisterMessage(AddInstanceOutput)

AbortInstancesInput = _reflection.GeneratedProtocolMessageType('AbortInstancesInput', (_message.Message,), dict(
  DESCRIPTOR = _ABORTINSTANCESINPUT,
  __module__ = 'later_pb2'
  # @@protoc_insertion_point(class_scope:hippoai.later.AbortInstancesInput)
  ))
_sym_db.RegisterMessage(AbortInstancesInput)

AbortInstancesOutput = _reflection.GeneratedProtocolMessageType('AbortInstancesOutput', (_message.Message,), dict(
  DESCRIPTOR = _ABORTINSTANCESOUTPUT,
  __module__ = 'later_pb2'
  # @@protoc_insertion_point(class_scope:hippoai.later.AbortInstancesOutput)
  ))
_sym_db.RegisterMessage(AbortInstancesOutput)

GetInstancesInput = _reflection.GeneratedProtocolMessageType('GetInstancesInput', (_message.Message,), dict(
  DESCRIPTOR = _GETINSTANCESINPUT,
  __module__ = 'later_pb2'
  # @@protoc_insertion_point(class_scope:hippoai.later.GetInstancesInput)
  ))
_sym_db.RegisterMessage(GetInstancesInput)

GetInstancesOutput = _reflection.GeneratedProtocolMessageType('GetInstancesOutput', (_message.Message,), dict(
  DESCRIPTOR = _GETINSTANCESOUTPUT,
  __module__ = 'later_pb2'
  # @@protoc_insertion_point(class_scope:hippoai.later.GetInstancesOutput)
  ))
_sym_db.RegisterMessage(GetInstancesOutput)


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


  class MutationsStub(object):

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.AddInstance = channel.unary_unary(
          '/hippoai.later.Mutations/AddInstance',
          request_serializer=AddInstanceInput.SerializeToString,
          response_deserializer=AddInstanceOutput.FromString,
          )
      self.AbortInstances = channel.unary_unary(
          '/hippoai.later.Mutations/AbortInstances',
          request_serializer=AbortInstancesInput.SerializeToString,
          response_deserializer=AbortInstancesOutput.FromString,
          )
      self.GetInstances = channel.unary_unary(
          '/hippoai.later.Mutations/GetInstances',
          request_serializer=GetInstancesInput.SerializeToString,
          response_deserializer=GetInstancesOutput.FromString,
          )


  class MutationsServicer(object):

    def AddInstance(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def AbortInstances(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def GetInstances(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_MutationsServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'AddInstance': grpc.unary_unary_rpc_method_handler(
            servicer.AddInstance,
            request_deserializer=AddInstanceInput.FromString,
            response_serializer=AddInstanceOutput.SerializeToString,
        ),
        'AbortInstances': grpc.unary_unary_rpc_method_handler(
            servicer.AbortInstances,
            request_deserializer=AbortInstancesInput.FromString,
            response_serializer=AbortInstancesOutput.SerializeToString,
        ),
        'GetInstances': grpc.unary_unary_rpc_method_handler(
            servicer.GetInstances,
            request_deserializer=GetInstancesInput.FromString,
            response_serializer=GetInstancesOutput.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'hippoai.later.Mutations', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaMutationsServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    def AddInstance(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def AbortInstances(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def GetInstances(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaMutationsStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    def AddInstance(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    AddInstance.future = None
    def AbortInstances(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    AbortInstances.future = None
    def GetInstances(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    GetInstances.future = None


  def beta_create_Mutations_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('hippoai.later.Mutations', 'AbortInstances'): AbortInstancesInput.FromString,
      ('hippoai.later.Mutations', 'AddInstance'): AddInstanceInput.FromString,
      ('hippoai.later.Mutations', 'GetInstances'): GetInstancesInput.FromString,
    }
    response_serializers = {
      ('hippoai.later.Mutations', 'AbortInstances'): AbortInstancesOutput.SerializeToString,
      ('hippoai.later.Mutations', 'AddInstance'): AddInstanceOutput.SerializeToString,
      ('hippoai.later.Mutations', 'GetInstances'): GetInstancesOutput.SerializeToString,
    }
    method_implementations = {
      ('hippoai.later.Mutations', 'AbortInstances'): face_utilities.unary_unary_inline(servicer.AbortInstances),
      ('hippoai.later.Mutations', 'AddInstance'): face_utilities.unary_unary_inline(servicer.AddInstance),
      ('hippoai.later.Mutations', 'GetInstances'): face_utilities.unary_unary_inline(servicer.GetInstances),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_Mutations_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('hippoai.later.Mutations', 'AbortInstances'): AbortInstancesInput.SerializeToString,
      ('hippoai.later.Mutations', 'AddInstance'): AddInstanceInput.SerializeToString,
      ('hippoai.later.Mutations', 'GetInstances'): GetInstancesInput.SerializeToString,
    }
    response_deserializers = {
      ('hippoai.later.Mutations', 'AbortInstances'): AbortInstancesOutput.FromString,
      ('hippoai.later.Mutations', 'AddInstance'): AddInstanceOutput.FromString,
      ('hippoai.later.Mutations', 'GetInstances'): GetInstancesOutput.FromString,
    }
    cardinalities = {
      'AbortInstances': cardinality.Cardinality.UNARY_UNARY,
      'AddInstance': cardinality.Cardinality.UNARY_UNARY,
      'GetInstances': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'hippoai.later.Mutations', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
