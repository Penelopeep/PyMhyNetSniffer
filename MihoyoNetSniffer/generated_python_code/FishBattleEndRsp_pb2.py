# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: FishBattleEndRsp.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import FishBattleResult_pb2 as FishBattleResult__pb2
import ItemParam_pb2 as ItemParam__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16\x46ishBattleEndRsp.proto\x1a\x16\x46ishBattleResult.proto\x1a\x0fItemParam.proto\"\xc8\x03\n\x10\x46ishBattleEndRsp\x12(\n\rbattle_result\x18\x06 \x01(\x0e\x32\x11.FishBattleResult\x12>\n\x10no_reward_reason\x18\x02 \x01(\x0e\x32$.FishBattleEndRsp.FishNoRewardReason\x12\x0f\n\x07retcode\x18\t \x01(\x05\x12\'\n\x13Unk3300_ABBBGOBDJEC\x18\x0c \x03(\x0b\x32\n.ItemParam\x12\x15\n\ris_got_reward\x18\x08 \x01(\x08\x12\'\n\x13Unk3300_MDCKKPGNKGL\x18\x01 \x03(\x0b\x32\n.ItemParam\x12$\n\x10reward_item_list\x18\x0f \x03(\x0b\x32\n.ItemParam\"\xa9\x01\n\x12\x46ishNoRewardReason\x12\x1e\n\x1a\x46ISH_NO_REWARD_REASON_NONE\x10\x00\x12(\n$FISH_NO_REWARD_REASON_ACTIVITY_LIMIT\x10\x01\x12#\n\x1f\x46ISH_NO_REWARD_REASON_BAG_LIMIT\x10\x02\x12$\n FISH_NO_REWARD_REASON_POOL_LIMIT\x10\x03\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'FishBattleEndRsp_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _FISHBATTLEENDRSP._serialized_start=68
  _FISHBATTLEENDRSP._serialized_end=524
  _FISHBATTLEENDRSP_FISHNOREWARDREASON._serialized_start=355
  _FISHBATTLEENDRSP_FISHNOREWARDREASON._serialized_end=524
# @@protoc_insertion_point(module_scope)
