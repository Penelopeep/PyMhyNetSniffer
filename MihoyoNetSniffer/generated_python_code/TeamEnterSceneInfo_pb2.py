# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: TeamEnterSceneInfo.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import AbilityControlBlock_pb2 as AbilityControlBlock__pb2
import AbilitySyncStateInfo_pb2 as AbilitySyncStateInfo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='TeamEnterSceneInfo.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\n\031emu.grasscutter.net.proto',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x18TeamEnterSceneInfo.proto\x1a\x19\x41\x62ilityControlBlock.proto\x1a\x1a\x41\x62ilitySyncStateInfo.proto\"\x8d\x01\n\x12TeamEnterSceneInfo\x12\x14\n\x0cteamEntityId\x18\x04 \x01(\r\x12\x31\n\x13\x61\x62ilityControlBlock\x18\x0c \x01(\x0b\x32\x14.AbilityControlBlock\x12.\n\x0fteamAbilityInfo\x18\n \x01(\x0b\x32\x15.AbilitySyncStateInfoB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3'
  ,
  dependencies=[AbilityControlBlock__pb2.DESCRIPTOR,AbilitySyncStateInfo__pb2.DESCRIPTOR,])




_TEAMENTERSCENEINFO = _descriptor.Descriptor(
  name='TeamEnterSceneInfo',
  full_name='TeamEnterSceneInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='teamEntityId', full_name='TeamEnterSceneInfo.teamEntityId', index=0,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='abilityControlBlock', full_name='TeamEnterSceneInfo.abilityControlBlock', index=1,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='teamAbilityInfo', full_name='TeamEnterSceneInfo.teamAbilityInfo', index=2,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=84,
  serialized_end=225,
)

_TEAMENTERSCENEINFO.fields_by_name['abilityControlBlock'].message_type = AbilityControlBlock__pb2._ABILITYCONTROLBLOCK
_TEAMENTERSCENEINFO.fields_by_name['teamAbilityInfo'].message_type = AbilitySyncStateInfo__pb2._ABILITYSYNCSTATEINFO
DESCRIPTOR.message_types_by_name['TeamEnterSceneInfo'] = _TEAMENTERSCENEINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TeamEnterSceneInfo = _reflection.GeneratedProtocolMessageType('TeamEnterSceneInfo', (_message.Message,), {
  'DESCRIPTOR' : _TEAMENTERSCENEINFO,
  '__module__' : 'TeamEnterSceneInfo_pb2'
  # @@protoc_insertion_point(class_scope:TeamEnterSceneInfo)
  })
_sym_db.RegisterMessage(TeamEnterSceneInfo)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
