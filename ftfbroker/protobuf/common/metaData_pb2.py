# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ftfbroker/protobuf/common/metaData.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ftfbroker/protobuf/common/metaData.proto',
  package='ftfbroker.protobuf.common',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n(ftfbroker/protobuf/common/metaData.proto\x12\x19\x66tfbroker.protobuf.common\"\xeb\x01\n\nMetaDataV1\x12\x10\n\x08iso_date\x18\x01 \x01(\t\x12\x46\n\x0b\x65nvironment\x18\x02 \x01(\x0e\x32\x31.ftfbroker.protobuf.common.MetaDataV1.Environment\x12\x17\n\x0fsending_service\x18\x03 \x01(\t\x12\x0e\n\x06offset\x18\x04 \x01(\x03\x12\x11\n\tpartition\x18\x05 \x01(\x03\"G\n\x0b\x45nvironment\x12\x17\n\x13UNKNOWN_ENVIRONMENT\x10\x00\x12\x0e\n\nPRODUCTION\x10\x01\x12\x0f\n\x0b\x44\x45VELOPMENT\x10\x02\x62\x06proto3')
)



_METADATAV1_ENVIRONMENT = _descriptor.EnumDescriptor(
  name='Environment',
  full_name='ftfbroker.protobuf.common.MetaDataV1.Environment',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_ENVIRONMENT', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRODUCTION', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEVELOPMENT', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=236,
  serialized_end=307,
)
_sym_db.RegisterEnumDescriptor(_METADATAV1_ENVIRONMENT)


_METADATAV1 = _descriptor.Descriptor(
  name='MetaDataV1',
  full_name='ftfbroker.protobuf.common.MetaDataV1',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='iso_date', full_name='ftfbroker.protobuf.common.MetaDataV1.iso_date', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='environment', full_name='ftfbroker.protobuf.common.MetaDataV1.environment', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sending_service', full_name='ftfbroker.protobuf.common.MetaDataV1.sending_service', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='offset', full_name='ftfbroker.protobuf.common.MetaDataV1.offset', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='partition', full_name='ftfbroker.protobuf.common.MetaDataV1.partition', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _METADATAV1_ENVIRONMENT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=72,
  serialized_end=307,
)

_METADATAV1.fields_by_name['environment'].enum_type = _METADATAV1_ENVIRONMENT
_METADATAV1_ENVIRONMENT.containing_type = _METADATAV1
DESCRIPTOR.message_types_by_name['MetaDataV1'] = _METADATAV1
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MetaDataV1 = _reflection.GeneratedProtocolMessageType('MetaDataV1', (_message.Message,), {
  'DESCRIPTOR' : _METADATAV1,
  '__module__' : 'ftfbroker.protobuf.common.metaData_pb2'
  # @@protoc_insertion_point(class_scope:ftfbroker.protobuf.common.MetaDataV1)
  })
_sym_db.RegisterMessage(MetaDataV1)


# @@protoc_insertion_point(module_scope)
