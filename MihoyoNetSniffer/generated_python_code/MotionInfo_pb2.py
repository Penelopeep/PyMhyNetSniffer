# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: MotionInfo.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import MotionState_pb2 as MotionState__pb2
import Vector_pb2 as Vector__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10MotionInfo.proto\x1a\x11MotionState.proto\x1a\x0cVector.proto\"\xdf\x01\n\nMotionInfo\x12\x14\n\x03pos\x18\x01 \x01(\x0b\x32\x07.Vector\x12\x14\n\x03rot\x18\x02 \x01(\x0b\x32\x07.Vector\x12\x16\n\x05speed\x18\x03 \x01(\x0b\x32\x07.Vector\x12\x1b\n\x05state\x18\x04 \x01(\x0e\x32\x0c.MotionState\x12\x17\n\x06params\x18\x05 \x03(\x0b\x32\x07.Vector\x12\x18\n\x07ref_pos\x18\x06 \x01(\x0b\x32\x07.Vector\x12\x0e\n\x06ref_id\x18\x07 \x01(\r\x12\x12\n\nscene_time\x18\x08 \x01(\r\x12\x19\n\x11interval_velocity\x18\t \x01(\x04\x42\x13\n\x11layla.sleep.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'MotionInfo_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\021layla.sleep.proto'
  _globals['_MOTIONINFO']._serialized_start=54
  _globals['_MOTIONINFO']._serialized_end=277
# @@protoc_insertion_point(module_scope)
