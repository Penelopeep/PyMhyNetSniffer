# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: GetCustomDungeonRsp.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import CustomDungeonBanInfo_pb2 as CustomDungeonBanInfo__pb2
import CustomDungeonBrief_pb2 as CustomDungeonBrief__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19GetCustomDungeonRsp.proto\x1a\x1a\x43ustomDungeonBanInfo.proto\x1a\x18\x43ustomDungeonBrief.proto\"x\n\x13GetCustomDungeonRsp\x12\'\n\nbrief_list\x18\x05 \x03(\x0b\x32\x13.CustomDungeonBrief\x12\x0f\n\x07retcode\x18\x03 \x01(\x05\x12\'\n\x08\x62\x61n_info\x18\n \x01(\x0b\x32\x15.CustomDungeonBanInfob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'GetCustomDungeonRsp_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GETCUSTOMDUNGEONRSP._serialized_start=83
  _GETCUSTOMDUNGEONRSP._serialized_end=203
# @@protoc_insertion_point(module_scope)