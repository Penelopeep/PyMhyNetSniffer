# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: FleurFairActivityDetailInfo.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import FleurFairChapterInfo_pb2 as FleurFairChapterInfo__pb2
import FleurFairDungeonSectionInfo_pb2 as FleurFairDungeonSectionInfo__pb2
import FleurFairMinigameInfo_pb2 as FleurFairMinigameInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!FleurFairActivityDetailInfo.proto\x1a\x1a\x46leurFairChapterInfo.proto\x1a!FleurFairDungeonSectionInfo.proto\x1a\x1b\x46leurFairMinigameInfo.proto\"\xa2\x04\n\x1b\x46leurFairActivityDetailInfo\x12L\n\x11minigame_info_map\x18\x0b \x03(\x0b\x32\x31.FleurFairActivityDetailInfo.MinigameInfoMapEntry\x12\x1b\n\x13is_dungeon_unlocked\x18\x01 \x01(\x08\x12\x13\n\x0bPEIAKLKGGIP\x18\x08 \x01(\r\x12\x13\n\x0bPIIHNGHBLJI\x18\x0f \x01(\r\x12Y\n\x18\x64ungeon_section_info_map\x18\x03 \x03(\x0b\x32\x37.FleurFairActivityDetailInfo.DungeonSectionInfoMapEntry\x12\x19\n\x11is_content_closed\x18\n \x01(\x08\x12\x30\n\x11\x63hapter_info_list\x18\x0e \x03(\x0b\x32\x15.FleurFairChapterInfo\x12\x1a\n\x12\x63ontent_close_time\x18\x02 \x01(\r\x1aN\n\x14MinigameInfoMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.FleurFairMinigameInfo:\x02\x38\x01\x1aZ\n\x1a\x44ungeonSectionInfoMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12+\n\x05value\x18\x02 \x01(\x0b\x32\x1c.FleurFairDungeonSectionInfo:\x02\x38\x01\x42\x13\n\x11layla.sleep.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'FleurFairActivityDetailInfo_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\021layla.sleep.proto'
  _FLEURFAIRACTIVITYDETAILINFO_MINIGAMEINFOMAPENTRY._options = None
  _FLEURFAIRACTIVITYDETAILINFO_MINIGAMEINFOMAPENTRY._serialized_options = b'8\001'
  _FLEURFAIRACTIVITYDETAILINFO_DUNGEONSECTIONINFOMAPENTRY._options = None
  _FLEURFAIRACTIVITYDETAILINFO_DUNGEONSECTIONINFOMAPENTRY._serialized_options = b'8\001'
  _globals['_FLEURFAIRACTIVITYDETAILINFO']._serialized_start=130
  _globals['_FLEURFAIRACTIVITYDETAILINFO']._serialized_end=676
  _globals['_FLEURFAIRACTIVITYDETAILINFO_MINIGAMEINFOMAPENTRY']._serialized_start=506
  _globals['_FLEURFAIRACTIVITYDETAILINFO_MINIGAMEINFOMAPENTRY']._serialized_end=584
  _globals['_FLEURFAIRACTIVITYDETAILINFO_DUNGEONSECTIONINFOMAPENTRY']._serialized_start=586
  _globals['_FLEURFAIRACTIVITYDETAILINFO_DUNGEONSECTIONINFOMAPENTRY']._serialized_end=676
# @@protoc_insertion_point(module_scope)
