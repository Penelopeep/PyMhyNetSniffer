# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: BossChest.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import WeeklyBossResinDiscountInfo_pb2 as WeeklyBossResinDiscountInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0f\x42ossChest.proto\x1a!WeeklyBossResinDiscountInfo.proto\"\xef\x01\n\tBossChest\x12\x17\n\x0fmonsterConfigId\x18\x01 \x01(\r\x12\r\n\x05resin\x18\x02 \x01(\r\x12\x15\n\rremainUidList\x18\x03 \x03(\r\x12\x16\n\x0equalifyUidList\x18\x04 \x03(\r\x12\x36\n\x0euidDiscountMap\x18\x05 \x03(\x0b\x32\x1e.BossChest.UidDiscountMapEntry\x1aS\n\x13UidDiscountMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12+\n\x05value\x18\x02 \x01(\x0b\x32\x1c.WeeklyBossResinDiscountInfo:\x02\x38\x01\x42\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'BossChest_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _BOSSCHEST_UIDDISCOUNTMAPENTRY._options = None
  _BOSSCHEST_UIDDISCOUNTMAPENTRY._serialized_options = b'8\001'
  _globals['_BOSSCHEST']._serialized_start=55
  _globals['_BOSSCHEST']._serialized_end=294
  _globals['_BOSSCHEST_UIDDISCOUNTMAPENTRY']._serialized_start=211
  _globals['_BOSSCHEST_UIDDISCOUNTMAPENTRY']._serialized_end=294
# @@protoc_insertion_point(module_scope)
