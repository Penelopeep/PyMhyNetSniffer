# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: SummerTimeInfo.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import SummerTimeSprintBoatInfo_pb2 as SummerTimeSprintBoatInfo__pb2
import SummerTimeStageInfo_pb2 as SummerTimeStageInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14SummerTimeInfo.proto\x1a\x1eSummerTimeSprintBoatInfo.proto\x1a\x19SummerTimeStageInfo.proto\"\xeb\x01\n\x0eSummerTimeInfo\x12\x31\n\x0esprintBoatInfo\x18\x0b \x01(\x0b\x32\x19.SummerTimeSprintBoatInfo\x12\x18\n\x10\x63ontentCloseTime\x18\x06 \x01(\r\x12/\n\x08stageMap\x18\x02 \x03(\x0b\x32\x1d.SummerTimeInfo.StageMapEntry\x12\x14\n\x0cleftMonsters\x18\t \x01(\x08\x1a\x45\n\rStageMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.SummerTimeStageInfo:\x02\x38\x01\x42\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'SummerTimeInfo_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _SUMMERTIMEINFO_STAGEMAPENTRY._options = None
  _SUMMERTIMEINFO_STAGEMAPENTRY._serialized_options = b'8\001'
  _globals['_SUMMERTIMEINFO']._serialized_start=84
  _globals['_SUMMERTIMEINFO']._serialized_end=319
  _globals['_SUMMERTIMEINFO_STAGEMAPENTRY']._serialized_start=250
  _globals['_SUMMERTIMEINFO_STAGEMAPENTRY']._serialized_end=319
# @@protoc_insertion_point(module_scope)
