# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: HachiInfo.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import HachiStageInfo_pb2 as HachiStageInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fHachiInfo.proto\x1a\x14HachiStageInfo.proto\"y\n\tHachiInfo\x12*\n\x08stageMap\x18\t \x03(\x0b\x32\x18.HachiInfo.StageMapEntry\x1a@\n\rStageMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\x1e\n\x05value\x18\x02 \x01(\x0b\x32\x0f.HachiStageInfo:\x02\x38\x01\x42\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'HachiInfo_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _HACHIINFO_STAGEMAPENTRY._options = None
  _HACHIINFO_STAGEMAPENTRY._serialized_options = b'8\001'
  _globals['_HACHIINFO']._serialized_start=41
  _globals['_HACHIINFO']._serialized_end=162
  _globals['_HACHIINFO_STAGEMAPENTRY']._serialized_start=98
  _globals['_HACHIINFO_STAGEMAPENTRY']._serialized_end=162
# @@protoc_insertion_point(module_scope)