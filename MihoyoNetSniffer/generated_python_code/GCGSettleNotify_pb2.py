# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: GCGSettleNotify.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import GCGEndReason_pb2 as GCGEndReason__pb2
import GCGGameBusinessType_pb2 as GCGGameBusinessType__pb2
import ItemParam_pb2 as ItemParam__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15GCGSettleNotify.proto\x1a\x12GCGEndReason.proto\x1a\x19GCGGameBusinessType.proto\x1a\x0fItemParam.proto\"\x89\x02\n\x0fGCGSettleNotify\x12$\n\x10reward_item_list\x18\x08 \x03(\x0b\x32\n.ItemParam\x12\"\n\x1a\x66inished_challenge_id_list\x18\x01 \x03(\r\x12\x0f\n\x07game_id\x18\x03 \x01(\r\x12\x0e\n\x06is_win\x18\x02 \x01(\x08\x12+\n\rbusiness_type\x18\x05 \x01(\x0e\x32\x14.GCGGameBusinessType\x12\x19\n\x11win_controller_id\x18\x0b \x01(\r\x12$\n\x1c\x66orbid_finish_challenge_list\x18\n \x03(\r\x12\x1d\n\x06reason\x18\x04 \x01(\x0e\x32\r.GCGEndReasonb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'GCGSettleNotify_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GCGSETTLENOTIFY._serialized_start=90
  _GCGSETTLENOTIFY._serialized_end=355
# @@protoc_insertion_point(module_scope)