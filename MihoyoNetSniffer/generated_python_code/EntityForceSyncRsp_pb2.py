# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: EntityForceSyncRsp.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import MotionInfo_pb2 as MotionInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18\x45ntityForceSyncRsp.proto\x1a\x10MotionInfo.proto\"n\n\x12\x45ntityForceSyncRsp\x12\x12\n\nscene_time\x18\x0e \x01(\r\x12\x11\n\tentity_id\x18\x06 \x01(\r\x12 \n\x0b\x66\x61il_motion\x18\x08 \x01(\x0b\x32\x0b.MotionInfo\x12\x0f\n\x07retcode\x18\x04 \x01(\x05\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'EntityForceSyncRsp_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ENTITYFORCESYNCRSP._serialized_start=46
  _ENTITYFORCESYNCRSP._serialized_end=156
# @@protoc_insertion_point(module_scope)