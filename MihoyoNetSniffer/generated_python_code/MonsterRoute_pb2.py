# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: MonsterRoute.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import RoutePoint_pb2 as RoutePoint__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12MonsterRoute.proto\x1a\x10RoutePoint.proto\"p\n\x0cMonsterRoute\x12!\n\x0croute_points\x18\x01 \x03(\x0b\x32\x0b.RoutePoint\x12\x13\n\x0bspeed_level\x18\x02 \x01(\r\x12\x12\n\nroute_type\x18\x03 \x01(\r\x12\x14\n\x0c\x61rrive_range\x18\x04 \x01(\x02\x42\x13\n\x11layla.sleep.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'MonsterRoute_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\021layla.sleep.proto'
  _globals['_MONSTERROUTE']._serialized_start=40
  _globals['_MONSTERROUTE']._serialized_end=152
# @@protoc_insertion_point(module_scope)
