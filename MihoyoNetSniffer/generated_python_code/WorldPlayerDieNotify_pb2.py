# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WorldPlayerDieNotify.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import PlayerDieType_pb2 as PlayerDieType__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1aWorldPlayerDieNotify.proto\x1a\x13PlayerDieType.proto\"\x89\x01\n\x14WorldPlayerDieNotify\x12 \n\x08\x64ie_type\x18\x04 \x01(\x0e\x32\x0e.PlayerDieType\x12\x1a\n\x12murderer_entity_id\x18\x0e \x01(\r\x12\x14\n\nmonster_id\x18\x0f \x01(\rH\x00\x12\x13\n\tgadget_id\x18\x03 \x01(\rH\x00\x42\x08\n\x06\x65ntityB\x13\n\x11layla.sleep.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'WorldPlayerDieNotify_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\021layla.sleep.proto'
  _globals['_WORLDPLAYERDIENOTIFY']._serialized_start=52
  _globals['_WORLDPLAYERDIENOTIFY']._serialized_end=189
# @@protoc_insertion_point(module_scope)
