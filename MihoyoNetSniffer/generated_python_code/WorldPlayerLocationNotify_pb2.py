# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WorldPlayerLocationNotify.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import PlayerLocationInfo_pb2 as PlayerLocationInfo__pb2
import PlayerWorldLocationInfo_pb2 as PlayerWorldLocationInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fWorldPlayerLocationNotify.proto\x1a\x18PlayerLocationInfo.proto\x1a\x1dPlayerWorldLocationInfo.proto\"\x82\x01\n\x19WorldPlayerLocationNotify\x12\x37\n\x15player_world_loc_list\x18\x05 \x03(\x0b\x32\x18.PlayerWorldLocationInfo\x12,\n\x0fplayer_loc_list\x18\x0e \x03(\x0b\x32\x13.PlayerLocationInfob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'WorldPlayerLocationNotify_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _WORLDPLAYERLOCATIONNOTIFY._serialized_start=93
  _WORLDPLAYERLOCATIONNOTIFY._serialized_end=223
# @@protoc_insertion_point(module_scope)
