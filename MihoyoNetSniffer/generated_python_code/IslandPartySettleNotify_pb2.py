# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: IslandPartySettleNotify.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ExhibitionDisplayInfo_pb2 as ExhibitionDisplayInfo__pb2
import GalleryStopReason_pb2 as GalleryStopReason__pb2
import IslandPartyGallerySettleInfo_pb2 as IslandPartyGallerySettleInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dIslandPartySettleNotify.proto\x1a\x1b\x45xhibitionDisplayInfo.proto\x1a\x17GalleryStopReason.proto\x1a\"IslandPartyGallerySettleInfo.proto\"\xce\x01\n\x17IslandPartySettleNotify\x12\x13\n\x0btime_remain\x18\t \x01(\r\x12\x15\n\ris_new_record\x18\x03 \x01(\x08\x12*\n\nscore_list\x18\x05 \x03(\x0b\x32\x16.ExhibitionDisplayInfo\x12\"\n\x06reason\x18\x0c \x01(\x0e\x32\x12.GalleryStopReason\x12\x37\n\x10settle_info_list\x18\r \x03(\x0b\x32\x1d.IslandPartyGallerySettleInfob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'IslandPartySettleNotify_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ISLANDPARTYSETTLENOTIFY._serialized_start=124
  _ISLANDPARTYSETTLENOTIFY._serialized_end=330
# @@protoc_insertion_point(module_scope)
