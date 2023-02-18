# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: TeamEntityInfo.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import AbilitySyncStateInfo_pb2 as AbilitySyncStateInfo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='TeamEntityInfo.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\n\031emu.grasscutter.net.proto',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x14TeamEntityInfo.proto\x1a\x1a\x41\x62ilitySyncStateInfo.proto\"o\n\x0eTeamEntityInfo\x12.\n\x0fteamAbilityInfo\x18\x08 \x01(\x0b\x32\x15.AbilitySyncStateInfo\x12\x14\n\x0cteamEntityId\x18\x02 \x01(\r\x12\x17\n\x0f\x61uthorityPeerId\x18\x0c \x01(\rB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3'
  ,
  dependencies=[AbilitySyncStateInfo__pb2.DESCRIPTOR,])




_TEAMENTITYINFO = _descriptor.Descriptor(
  name='TeamEntityInfo',
  full_name='TeamEntityInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='teamAbilityInfo', full_name='TeamEntityInfo.teamAbilityInfo', index=0,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='teamEntityId', full_name='TeamEntityInfo.teamEntityId', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='authorityPeerId', full_name='TeamEntityInfo.authorityPeerId', index=2,
      number=12, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=52,
  serialized_end=163,
)

_TEAMENTITYINFO.fields_by_name['teamAbilityInfo'].message_type = AbilitySyncStateInfo__pb2._ABILITYSYNCSTATEINFO
DESCRIPTOR.message_types_by_name['TeamEntityInfo'] = _TEAMENTITYINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TeamEntityInfo = _reflection.GeneratedProtocolMessageType('TeamEntityInfo', (_message.Message,), {
  'DESCRIPTOR' : _TEAMENTITYINFO,
  '__module__' : 'TeamEntityInfo_pb2'
  # @@protoc_insertion_point(class_scope:TeamEntityInfo)
  })
_sym_db.RegisterMessage(TeamEntityInfo)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
