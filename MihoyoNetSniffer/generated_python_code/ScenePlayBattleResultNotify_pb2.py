# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ScenePlayBattleResultNotify.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ScenePlayBattleSettlePlayerInfo_pb2 as ScenePlayBattleSettlePlayerInfo__pb2
import ScenePlayBattleSettleRewardInfo_pb2 as ScenePlayBattleSettleRewardInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!ScenePlayBattleResultNotify.proto\x1a%ScenePlayBattleSettlePlayerInfo.proto\x1a%ScenePlayBattleSettleRewardInfo.proto\"\xea\x01\n\x1bScenePlayBattleResultNotify\x12\x11\n\tcost_time\x18\x07 \x01(\r\x12\x0f\n\x07play_id\x18\x0c \x01(\r\x12\x11\n\tplay_type\x18\n \x01(\r\x12\x41\n\x17settle_reward_info_list\x18\x04 \x03(\x0b\x32 .ScenePlayBattleSettleRewardInfo\x12\x41\n\x17settle_player_info_list\x18\x02 \x03(\x0b\x32 .ScenePlayBattleSettlePlayerInfo\x12\x0e\n\x06is_win\x18\x06 \x01(\x08\x42\x13\n\x11layla.sleep.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ScenePlayBattleResultNotify_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\021layla.sleep.proto'
  _globals['_SCENEPLAYBATTLERESULTNOTIFY']._serialized_start=116
  _globals['_SCENEPLAYBATTLERESULTNOTIFY']._serialized_end=350
# @@protoc_insertion_point(module_scope)
