# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: CoopChapter.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import State_pb2 as State__pb2
import CoopCg_pb2 as CoopCg__pb2
import CoopReward_pb2 as CoopReward__pb2
import CoopPoint_pb2 as CoopPoint__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x43oopChapter.proto\x1a\x0bState.proto\x1a\x0c\x43oopCg.proto\x1a\x10\x43oopReward.proto\x1a\x0f\x43oopPoint.proto\"\xe6\x02\n\x0b\x43oopChapter\x12\x36\n\rseenEndingMap\x18\x0c \x03(\x0b\x32\x1f.CoopChapter.SeenEndingMapEntry\x12\x18\n\x10\x66inishDialogList\x18\x05 \x03(\r\x12\x1b\n\ncoopCgList\x18\x0b \x03(\x0b\x32\x07.CoopCg\x12#\n\x0e\x63oopRewardList\x18\t \x03(\x0b\x32\x0b.CoopReward\x12\x16\n\x0elockReasonList\x18\x04 \x03(\r\x12\x18\n\x10\x66inishedEndCount\x18\x08 \x01(\r\x12!\n\rcoopPointList\x18\x07 \x03(\x0b\x32\n.CoopPoint\x12\x15\n\x05state\x18\x0f \x01(\x0e\x32\x06.State\x12\n\n\x02id\x18\x06 \x01(\r\x12\x15\n\rtotalEndCount\x18\x0e \x01(\r\x1a\x34\n\x12SeenEndingMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x42\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'CoopChapter_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _COOPCHAPTER_SEENENDINGMAPENTRY._options = None
  _COOPCHAPTER_SEENENDINGMAPENTRY._serialized_options = b'8\001'
  _globals['_COOPCHAPTER']._serialized_start=84
  _globals['_COOPCHAPTER']._serialized_end=442
  _globals['_COOPCHAPTER_SEENENDINGMAPENTRY']._serialized_start=390
  _globals['_COOPCHAPTER_SEENENDINGMAPENTRY']._serialized_end=442
# @@protoc_insertion_point(module_scope)
