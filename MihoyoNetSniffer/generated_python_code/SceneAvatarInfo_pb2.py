# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: SceneAvatarInfo.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import AvatarExcelInfo_pb2 as AvatarExcelInfo__pb2
import CurVehicleInfo_pb2 as CurVehicleInfo__pb2
import SceneReliquaryInfo_pb2 as SceneReliquaryInfo__pb2
import SceneWeaponInfo_pb2 as SceneWeaponInfo__pb2
import ServerBuff_pb2 as ServerBuff__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15SceneAvatarInfo.proto\x1a\x15\x41vatarExcelInfo.proto\x1a\x14\x43urVehicleInfo.proto\x1a\x18SceneReliquaryInfo.proto\x1a\x15SceneWeaponInfo.proto\x1a\x10ServerBuff.proto\"\x9d\x06\n\x0fSceneAvatarInfo\x12\x0b\n\x03uid\x18\x01 \x01(\r\x12\x11\n\tavatar_id\x18\x02 \x01(\r\x12\x0c\n\x04guid\x18\x03 \x01(\x04\x12\x0f\n\x07peer_id\x18\x04 \x01(\r\x12\x15\n\requip_id_list\x18\x05 \x03(\r\x12\x16\n\x0eskill_depot_id\x18\x06 \x01(\r\x12\x16\n\x0etalent_id_list\x18\x07 \x03(\r\x12 \n\x06weapon\x18\x08 \x01(\x0b\x32\x10.SceneWeaponInfo\x12+\n\x0ereliquary_list\x18\t \x03(\x0b\x32\x13.SceneReliquaryInfo\x12\x1e\n\x16\x63ore_proud_skill_level\x18\x0b \x01(\r\x12!\n\x19inherent_proud_skill_list\x18\x0c \x03(\r\x12<\n\x0fskill_level_map\x18\r \x03(\x0b\x32#.SceneAvatarInfo.SkillLevelMapEntry\x12R\n\x1bproud_skill_extra_level_map\x18\x0e \x03(\x0b\x32-.SceneAvatarInfo.ProudSkillExtraLevelMapEntry\x12%\n\x10server_buff_list\x18\x0f \x03(\x0b\x32\x0b.ServerBuff\x12\x1b\n\x13team_resonance_list\x18\x10 \x03(\r\x12\x1b\n\x13wearing_flycloak_id\x18\x11 \x01(\r\x12\x11\n\tborn_time\x18\x12 \x01(\r\x12\x12\n\ncostume_id\x18\x13 \x01(\r\x12)\n\x10\x63ur_vehicle_info\x18\x14 \x01(\x0b\x32\x0f.CurVehicleInfo\x12$\n\nexcel_info\x18\x15 \x01(\x0b\x32\x10.AvatarExcelInfo\x12\x11\n\tanim_hash\x18\x16 \x01(\r\x1a\x34\n\x12SkillLevelMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a>\n\x1cProudSkillExtraLevelMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x42\x13\n\x11layla.sleep.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'SceneAvatarInfo_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\021layla.sleep.proto'
  _SCENEAVATARINFO_SKILLLEVELMAPENTRY._options = None
  _SCENEAVATARINFO_SKILLLEVELMAPENTRY._serialized_options = b'8\001'
  _SCENEAVATARINFO_PROUDSKILLEXTRALEVELMAPENTRY._options = None
  _SCENEAVATARINFO_PROUDSKILLEXTRALEVELMAPENTRY._serialized_options = b'8\001'
  _globals['_SCENEAVATARINFO']._serialized_start=138
  _globals['_SCENEAVATARINFO']._serialized_end=935
  _globals['_SCENEAVATARINFO_SKILLLEVELMAPENTRY']._serialized_start=819
  _globals['_SCENEAVATARINFO_SKILLLEVELMAPENTRY']._serialized_end=871
  _globals['_SCENEAVATARINFO_PROUDSKILLEXTRALEVELMAPENTRY']._serialized_start=873
  _globals['_SCENEAVATARINFO_PROUDSKILLEXTRALEVELMAPENTRY']._serialized_end=935
# @@protoc_insertion_point(module_scope)
