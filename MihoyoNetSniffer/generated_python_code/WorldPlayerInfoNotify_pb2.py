# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WorldPlayerInfoNotify.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import OnlinePlayerInfo_pb2 as OnlinePlayerInfo__pb2
import PlayerWidgetInfo_pb2 as PlayerWidgetInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bWorldPlayerInfoNotify.proto\x1a\x16OnlinePlayerInfo.proto\x1a\x16PlayerWidgetInfo.proto\"\x91\x01\n\x15WorldPlayerInfoNotify\x12\x32\n\x17player_widget_info_list\x18\x07 \x03(\x0b\x32\x11.PlayerWidgetInfo\x12\x17\n\x0fplayer_uid_list\x18\x0c \x03(\r\x12+\n\x10player_info_list\x18\x0f \x03(\x0b\x32\x11.OnlinePlayerInfob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'WorldPlayerInfoNotify_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _WORLDPLAYERINFONOTIFY._serialized_start=80
  _WORLDPLAYERINFONOTIFY._serialized_end=225
# @@protoc_insertion_point(module_scope)
