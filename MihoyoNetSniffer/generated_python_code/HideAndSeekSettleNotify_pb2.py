# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: HideAndSeekSettleNotify.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ExhibitionDisplayInfo_pb2 as ExhibitionDisplayInfo__pb2
import HideAndSeekSettleInfo_pb2 as HideAndSeekSettleInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dHideAndSeekSettleNotify.proto\x1a\x1b\x45xhibitionDisplayInfo.proto\x1a\x1bHideAndSeekSettleInfo.proto\"\xf0\x02\n\x17HideAndSeekSettleNotify\x12\x30\n\x10settle_info_list\x18\x06 \x03(\x0b\x32\x16.HideAndSeekSettleInfo\x12*\n\nscore_list\x18\x03 \x03(\x0b\x32\x16.ExhibitionDisplayInfo\x12\x12\n\nplay_index\x18\x05 \x01(\r\x12\x11\n\tcost_time\x18\x0c \x01(\r\x12\x12\n\nstage_type\x18\n \x01(\r\x12\x35\n\x06reason\x18\x0b \x01(\x0e\x32%.HideAndSeekSettleNotify.SettleReason\x12\x13\n\x0bwinner_list\x18\x02 \x03(\r\x12\x17\n\x0fis_record_score\x18\x07 \x01(\x08\"W\n\x0cSettleReason\x12\x1a\n\x16SETTLE_REASON_TIME_OUT\x10\x00\x12\x13\n\x0fSETTLE_PLAY_END\x10\x01\x12\x16\n\x12SETTLE_PLAYER_QUIT\x10\x02\x42\x13\n\x11layla.sleep.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'HideAndSeekSettleNotify_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\021layla.sleep.proto'
  _globals['_HIDEANDSEEKSETTLENOTIFY']._serialized_start=92
  _globals['_HIDEANDSEEKSETTLENOTIFY']._serialized_end=460
  _globals['_HIDEANDSEEKSETTLENOTIFY_SETTLEREASON']._serialized_start=373
  _globals['_HIDEANDSEEKSETTLENOTIFY_SETTLEREASON']._serialized_end=460
# @@protoc_insertion_point(module_scope)
