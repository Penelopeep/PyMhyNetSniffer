# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: TowerFloorRecord.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import TowerLevelRecord_pb2 as TowerLevelRecord__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16TowerFloorRecord.proto\x1a\x16TowerLevelRecord.proto\"\xf5\x01\n\x10TowerFloorRecord\x12\"\n\x1a\x66loor_star_reward_progress\x18\x04 \x01(\r\x12\x33\n\x18passed_level_record_list\x18\x03 \x03(\x0b\x32\x11.TowerLevelRecord\x12\x10\n\x08\x66loor_id\x18\x02 \x01(\r\x12?\n\x10passed_level_map\x18\x0e \x03(\x0b\x32%.TowerFloorRecord.PassedLevelMapEntry\x1a\x35\n\x13PassedLevelMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x42\x13\n\x11layla.sleep.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'TowerFloorRecord_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\021layla.sleep.proto'
  _TOWERFLOORRECORD_PASSEDLEVELMAPENTRY._options = None
  _TOWERFLOORRECORD_PASSEDLEVELMAPENTRY._serialized_options = b'8\001'
  _globals['_TOWERFLOORRECORD']._serialized_start=51
  _globals['_TOWERFLOORRECORD']._serialized_end=296
  _globals['_TOWERFLOORRECORD_PASSEDLEVELMAPENTRY']._serialized_start=243
  _globals['_TOWERFLOORRECORD_PASSEDLEVELMAPENTRY']._serialized_end=296
# @@protoc_insertion_point(module_scope)
