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


import CoopCg_pb2 as CoopCg__pb2
import CoopPoint_pb2 as CoopPoint__pb2
import CoopReward_pb2 as CoopReward__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x43oopChapter.proto\x1a\x0c\x43oopCg.proto\x1a\x0f\x43oopPoint.proto\x1a\x10\x43oopReward.proto\"\xc5\x03\n\x0b\x43oopChapter\x12\x1d\n\x0c\x63oop_cg_list\x18\x02 \x03(\x0b\x32\x07.CoopCg\x12%\n\x10\x63oop_reward_list\x18\x05 \x03(\x0b\x32\x0b.CoopReward\x12#\n\x0f\x63oop_point_list\x18\x0c \x03(\x0b\x32\n.CoopPoint\x12!\n\x05state\x18\x07 \x01(\x0e\x32\x12.CoopChapter.State\x12\x13\n\x0b\x45\x46PMMEKFFHG\x18\n \x03(\r\x12\x13\n\x0bNLNALPGOELK\x18\x06 \x01(\r\x12\x13\n\x0bKOFPBNBJDAF\x18\x04 \x01(\r\x12\n\n\x02id\x18\t \x01(\r\x12\x13\n\x0b\x45HIGCPDOPMG\x18\r \x03(\r\x12\x38\n\x0fseen_ending_map\x18\x0b \x03(\x0b\x32\x1f.CoopChapter.SeenEndingMapEntry\x1a\x34\n\x12SeenEndingMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\"X\n\x05State\x12\x0f\n\x0bSTATE_CLOSE\x10\x00\x12\x17\n\x13STATE_COND_NOT_MEET\x10\x01\x12\x13\n\x0fSTATE_COND_MEET\x10\x02\x12\x10\n\x0cSTATE_ACCEPT\x10\x03\x42\x13\n\x11layla.sleep.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'CoopChapter_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\021layla.sleep.proto'
  _COOPCHAPTER_SEENENDINGMAPENTRY._options = None
  _COOPCHAPTER_SEENENDINGMAPENTRY._serialized_options = b'8\001'
  _globals['_COOPCHAPTER']._serialized_start=71
  _globals['_COOPCHAPTER']._serialized_end=524
  _globals['_COOPCHAPTER_SEENENDINGMAPENTRY']._serialized_start=382
  _globals['_COOPCHAPTER_SEENENDINGMAPENTRY']._serialized_end=434
  _globals['_COOPCHAPTER_STATE']._serialized_start=436
  _globals['_COOPCHAPTER_STATE']._serialized_end=524
# @@protoc_insertion_point(module_scope)
