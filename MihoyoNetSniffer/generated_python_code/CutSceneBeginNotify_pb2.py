# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: CutSceneBeginNotify.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import CutSceneExtraParam_pb2 as CutSceneExtraParam__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x43utSceneBeginNotify.proto\x1a\x18\x43utSceneExtraParam.proto\"q\n\x13\x43utSceneBeginNotify\x12\x13\n\x0b\x63utscene_id\x18\x0e \x01(\r\x12-\n\x10\x65xtra_param_list\x18\r \x03(\x0b\x32\x13.CutSceneExtraParam\x12\x16\n\x0eis_wait_others\x18\x01 \x01(\x08\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'CutSceneBeginNotify_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CUTSCENEBEGINNOTIFY._serialized_start=55
  _CUTSCENEBEGINNOTIFY._serialized_end=168
# @@protoc_insertion_point(module_scope)
