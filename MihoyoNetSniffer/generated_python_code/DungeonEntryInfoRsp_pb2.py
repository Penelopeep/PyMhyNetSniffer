# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: DungeonEntryInfoRsp.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import DungeonEntryInfo_pb2 as DungeonEntryInfo__pb2
import DungeonEntryPointInfo_pb2 as DungeonEntryPointInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x44ungeonEntryInfoRsp.proto\x1a\x16\x44ungeonEntryInfo.proto\x1a\x1b\x44ungeonEntryPointInfo.proto\"\xbf\x01\n\x13\x44ungeonEntryInfoRsp\x12\x1c\n\x14recommend_dungeon_id\x18\r \x01(\r\x12\x0f\n\x07retcode\x18\x0f \x01(\x05\x12\x10\n\x08point_id\x18\x0e \x01(\r\x12-\n\x12\x64ungeon_entry_list\x18\x04 \x03(\x0b\x32\x11.DungeonEntryInfo\x12\x38\n\x18\x64ungeon_entry_point_list\x18\t \x03(\x0b\x32\x16.DungeonEntryPointInfoB\x13\n\x11layla.sleep.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'DungeonEntryInfoRsp_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\021layla.sleep.proto'
  _globals['_DUNGEONENTRYINFORSP']._serialized_start=83
  _globals['_DUNGEONENTRYINFORSP']._serialized_end=274
# @@protoc_insertion_point(module_scope)
