# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: RogueDiaryActivityDetailInfo.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import RogueDiaryProgress_pb2 as RogueDiaryProgress__pb2
import RogueDiaryStageInfo_pb2 as RogueDiaryStageInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"RogueDiaryActivityDetailInfo.proto\x1a\x18RogueDiaryProgress.proto\x1a\x19RogueDiaryStageInfo.proto\"\xa8\x01\n\x1cRogueDiaryActivityDetailInfo\x12)\n\x0c\x63ur_progress\x18\x0f \x01(\x0b\x32\x13.RogueDiaryProgress\x12\x19\n\x11is_content_closed\x18\x03 \x01(\x08\x12(\n\nstage_list\x18\r \x03(\x0b\x32\x14.RogueDiaryStageInfo\x12\x18\n\x10is_have_progress\x18\x0e \x01(\x08\x42\x13\n\x11layla.sleep.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'RogueDiaryActivityDetailInfo_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\021layla.sleep.proto'
  _globals['_ROGUEDIARYACTIVITYDETAILINFO']._serialized_start=92
  _globals['_ROGUEDIARYACTIVITYDETAILINFO']._serialized_end=260
# @@protoc_insertion_point(module_scope)
