# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: BrickBreakerSettleNotify.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import Uint32Pair_pb2 as Uint32Pair__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1e\x42rickBreakerSettleNotify.proto\x1a\x10Uint32Pair.proto\"\x95\x03\n\x18\x42rickBreakerSettleNotify\x12\x0c\n\x04time\x18\x05 \x01(\r\x12\x16\n\x0eis_single_mode\x18\x0f \x01(\x08\x12\x12\n\nis_dungeon\x18\x02 \x01(\x08\x12\r\n\x05score\x18\x07 \x01(\r\x12\r\n\x05\x63ombo\x18\x0c \x01(\r\x12\x10\n\x08level_id\x18\x0b \x01(\r\x12\x36\n\x06reason\x18\x01 \x01(\x0e\x32&.BrickBreakerSettleNotify.SettleReason\x12\x15\n\ris_new_record\x18\x03 \x01(\x08\x12\x12\n\ngallery_id\x18\r \x01(\r\x12&\n\x11update_skill_list\x18\x04 \x03(\x0b\x32\x0b.Uint32Pair\"\x83\x01\n\x0cSettleReason\x12\x1a\n\x16SETTLE_REASON_TIME_OUT\x10\x00\x12\x1a\n\x16SETTLE_REASON_PLAY_END\x10\x01\x12\x1d\n\x19SETTLE_REASON_PLAYER_QUIT\x10\x02\x12\x1c\n\x18SETTLE_REASON_LIFE_COUNT\x10\x03\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'BrickBreakerSettleNotify_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BRICKBREAKERSETTLENOTIFY._serialized_start=53
  _BRICKBREAKERSETTLENOTIFY._serialized_end=458
  _BRICKBREAKERSETTLENOTIFY_SETTLEREASON._serialized_start=327
  _BRICKBREAKERSETTLENOTIFY_SETTLEREASON._serialized_end=458
# @@protoc_insertion_point(module_scope)
