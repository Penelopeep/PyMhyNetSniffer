# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: FleurFairMinigameInfo.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import FleurFairBalloonInfo_pb2 as FleurFairBalloonInfo__pb2
import FleurFairFallInfo_pb2 as FleurFairFallInfo__pb2
import FleurFairMusicGameInfo_pb2 as FleurFairMusicGameInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1b\x46leurFairMinigameInfo.proto\x1a\x1a\x46leurFairBalloonInfo.proto\x1a\x17\x46leurFairFallInfo.proto\x1a\x1c\x46leurFairMusicGameInfo.proto\"\xe1\x01\n\x15\x46leurFairMinigameInfo\x12\x13\n\x0bminigame_id\x18\x03 \x01(\r\x12\x0f\n\x07is_open\x18\x0f \x01(\x08\x12\x11\n\topen_time\x18\r \x01(\r\x12-\n\x0c\x62\x61lloon_info\x18\x01 \x01(\x0b\x32\x15.FleurFairBalloonInfoH\x00\x12\'\n\tfall_info\x18\n \x01(\x0b\x32\x12.FleurFairFallInfoH\x00\x12-\n\nmusic_info\x18\x0e \x01(\x0b\x32\x17.FleurFairMusicGameInfoH\x00\x42\x08\n\x06\x64\x65tailb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'FleurFairMinigameInfo_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _FLEURFAIRMINIGAMEINFO._serialized_start=115
  _FLEURFAIRMINIGAMEINFO._serialized_end=340
# @@protoc_insertion_point(module_scope)
