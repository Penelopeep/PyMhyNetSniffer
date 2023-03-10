# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: SceneMonsterInfo.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import FishtankFishInfo_pb2 as FishtankFishInfo__pb2
import MonsterBornType_pb2 as MonsterBornType__pb2
import MonsterRoute_pb2 as MonsterRoute__pb2
import SceneFishInfo_pb2 as SceneFishInfo__pb2
import SceneWeaponInfo_pb2 as SceneWeaponInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16SceneMonsterInfo.proto\x1a\x16\x46ishtankFishInfo.proto\x1a\x15MonsterBornType.proto\x1a\x12MonsterRoute.proto\x1a\x13SceneFishInfo.proto\x1a\x15SceneWeaponInfo.proto\"\xe3\x05\n\x10SceneMonsterInfo\x12\x12\n\nmonster_id\x18\x01 \x01(\r\x12\x10\n\x08group_id\x18\x02 \x01(\r\x12\x11\n\tconfig_id\x18\x03 \x01(\r\x12%\n\x0bweapon_list\x18\x04 \x03(\x0b\x32\x10.SceneWeaponInfo\x12\x19\n\x11\x61uthority_peer_id\x18\x05 \x01(\r\x12\x12\n\naffix_list\x18\x06 \x03(\r\x12\x10\n\x08is_elite\x18\x07 \x01(\x08\x12\x17\n\x0fowner_entity_id\x18\x08 \x01(\r\x12\x14\n\x0csummoned_tag\x18\t \x01(\r\x12;\n\x0esummon_tag_map\x18\n \x03(\x0b\x32#.SceneMonsterInfo.SummonTagMapEntry\x12\x0f\n\x07pose_id\x18\x0b \x01(\r\x12#\n\tborn_type\x18\x0c \x01(\x0e\x32\x10.MonsterBornType\x12\x10\n\x08\x62lock_id\x18\r \x01(\r\x12\x11\n\tmark_flag\x18\x0e \x01(\r\x12\x10\n\x08title_id\x18\x0f \x01(\r\x12\x17\n\x0fspecial_name_id\x18\x10 \x01(\r\x12\x18\n\x10\x61ttack_target_id\x18\x11 \x01(\r\x12$\n\rmonster_route\x18\x12 \x01(\x0b\x32\r.MonsterRoute\x12\x14\n\x0c\x61i_config_id\x18\x13 \x01(\r\x12\x16\n\x0elevel_route_id\x18\x14 \x01(\r\x12\x14\n\x0cinit_pose_id\x18\x15 \x01(\r\x12\x10\n\x08is_light\x18\x16 \x01(\x08\x12\x10\n\x08kill_num\x18\x17 \x01(\r\x12#\n\tfish_info\x18\x32 \x01(\x0b\x32\x0e.SceneFishInfoH\x00\x12/\n\x12\x66ishtank_fish_info\x18\x33 \x01(\x0b\x32\x11.FishtankFishInfoH\x00\x1a\x33\n\x11SummonTagMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x42\t\n\x07\x63ontentB\x13\n\x11layla.sleep.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'SceneMonsterInfo_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\021layla.sleep.proto'
  _SCENEMONSTERINFO_SUMMONTAGMAPENTRY._options = None
  _SCENEMONSTERINFO_SUMMONTAGMAPENTRY._serialized_options = b'8\001'
  _globals['_SCENEMONSTERINFO']._serialized_start=138
  _globals['_SCENEMONSTERINFO']._serialized_end=877
  _globals['_SCENEMONSTERINFO_SUMMONTAGMAPENTRY']._serialized_start=815
  _globals['_SCENEMONSTERINFO_SUMMONTAGMAPENTRY']._serialized_end=866
# @@protoc_insertion_point(module_scope)
