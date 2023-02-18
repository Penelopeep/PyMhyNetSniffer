# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: AvatarEnterSceneInfo.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import AbilitySyncStateInfo_pb2 as AbilitySyncStateInfo__pb2
import ServerBuff_pb2 as ServerBuff__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='AvatarEnterSceneInfo.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\n\031emu.grasscutter.net.proto',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1a\x41vatarEnterSceneInfo.proto\x1a\x1a\x41\x62ilitySyncStateInfo.proto\x1a\x10ServerBuff.proto\"\x8b\x02\n\x14\x41vatarEnterSceneInfo\x12\x12\n\navatarGuid\x18\x08 \x01(\x04\x12\x16\n\x0eweaponEntityId\x18\r \x01(\r\x12\x30\n\x11\x61vatarAbilityInfo\x18\x01 \x01(\x0b\x32\x15.AbilitySyncStateInfo\x12\x12\n\nbuffIdList\x18\x07 \x03(\r\x12\x16\n\x0e\x61vatarEntityId\x18\n \x01(\r\x12#\n\x0eserverBuffList\x18\x04 \x03(\x0b\x32\x0b.ServerBuff\x12\x30\n\x11weaponAbilityInfo\x18\x0b \x01(\x0b\x32\x15.AbilitySyncStateInfo\x12\x12\n\nweaponGuid\x18\x0e \x01(\x04\x42\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3'
  ,
  dependencies=[AbilitySyncStateInfo__pb2.DESCRIPTOR,ServerBuff__pb2.DESCRIPTOR,])




_AVATARENTERSCENEINFO = _descriptor.Descriptor(
  name='AvatarEnterSceneInfo',
  full_name='AvatarEnterSceneInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='avatarGuid', full_name='AvatarEnterSceneInfo.avatarGuid', index=0,
      number=8, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='weaponEntityId', full_name='AvatarEnterSceneInfo.weaponEntityId', index=1,
      number=13, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='avatarAbilityInfo', full_name='AvatarEnterSceneInfo.avatarAbilityInfo', index=2,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='buffIdList', full_name='AvatarEnterSceneInfo.buffIdList', index=3,
      number=7, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='avatarEntityId', full_name='AvatarEnterSceneInfo.avatarEntityId', index=4,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='serverBuffList', full_name='AvatarEnterSceneInfo.serverBuffList', index=5,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='weaponAbilityInfo', full_name='AvatarEnterSceneInfo.weaponAbilityInfo', index=6,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='weaponGuid', full_name='AvatarEnterSceneInfo.weaponGuid', index=7,
      number=14, type=4, cpp_type=4, label=1,
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
  serialized_start=77,
  serialized_end=344,
)

_AVATARENTERSCENEINFO.fields_by_name['avatarAbilityInfo'].message_type = AbilitySyncStateInfo__pb2._ABILITYSYNCSTATEINFO
_AVATARENTERSCENEINFO.fields_by_name['serverBuffList'].message_type = ServerBuff__pb2._SERVERBUFF
_AVATARENTERSCENEINFO.fields_by_name['weaponAbilityInfo'].message_type = AbilitySyncStateInfo__pb2._ABILITYSYNCSTATEINFO
DESCRIPTOR.message_types_by_name['AvatarEnterSceneInfo'] = _AVATARENTERSCENEINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AvatarEnterSceneInfo = _reflection.GeneratedProtocolMessageType('AvatarEnterSceneInfo', (_message.Message,), {
  'DESCRIPTOR' : _AVATARENTERSCENEINFO,
  '__module__' : 'AvatarEnterSceneInfo_pb2'
  # @@protoc_insertion_point(class_scope:AvatarEnterSceneInfo)
  })
_sym_db.RegisterMessage(AvatarEnterSceneInfo)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
