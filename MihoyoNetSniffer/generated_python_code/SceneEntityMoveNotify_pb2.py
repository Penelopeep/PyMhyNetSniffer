# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: SceneEntityMoveNotify.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import MotionInfo_pb2 as MotionInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bSceneEntityMoveNotify.proto\x1a\x10MotionInfo.proto\"v\n\x15SceneEntityMoveNotify\x12\x11\n\tentity_id\x18\x0f \x01(\r\x12\x14\n\x0creliable_seq\x18\x01 \x01(\r\x12 \n\x0bmotion_info\x18\x06 \x01(\x0b\x32\x0b.MotionInfo\x12\x12\n\nscene_time\x18\n \x01(\rB\x13\n\x11layla.sleep.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'SceneEntityMoveNotify_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\021layla.sleep.proto'
  _globals['_SCENEENTITYMOVENOTIFY']._serialized_start=49
  _globals['_SCENEENTITYMOVENOTIFY']._serialized_end=167
# @@protoc_insertion_point(module_scope)
