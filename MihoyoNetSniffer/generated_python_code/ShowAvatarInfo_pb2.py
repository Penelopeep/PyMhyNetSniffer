# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ShowAvatarInfo.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import AvatarExcelInfo_pb2 as AvatarExcelInfo__pb2
import AvatarFetterInfo_pb2 as AvatarFetterInfo__pb2
import PropValue_pb2 as PropValue__pb2
import ShowEquip_pb2 as ShowEquip__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14ShowAvatarInfo.proto\x1a\x15\x41vatarExcelInfo.proto\x1a\x16\x41vatarFetterInfo.proto\x1a\x0fPropValue.proto\x1a\x0fShowEquip.proto\"\xfa\x05\n\x0eShowAvatarInfo\x12\x11\n\tavatar_id\x18\x01 \x01(\r\x12.\n\x08prop_map\x18\x02 \x03(\x0b\x32\x1c.ShowAvatarInfo.PropMapEntry\x12\x16\n\x0etalent_id_list\x18\x03 \x03(\r\x12\x39\n\x0e\x66ight_prop_map\x18\x04 \x03(\x0b\x32!.ShowAvatarInfo.FightPropMapEntry\x12\x16\n\x0eskill_depot_id\x18\x05 \x01(\r\x12\x1e\n\x16\x63ore_proud_skill_level\x18\x06 \x01(\r\x12!\n\x19inherent_proud_skill_list\x18\x07 \x03(\r\x12;\n\x0fskill_level_map\x18\x08 \x03(\x0b\x32\".ShowAvatarInfo.SkillLevelMapEntry\x12Q\n\x1bproud_skill_extra_level_map\x18\t \x03(\x0b\x32,.ShowAvatarInfo.ProudSkillExtraLevelMapEntry\x12\x1e\n\nequip_list\x18\n \x03(\x0b\x32\n.ShowEquip\x12&\n\x0b\x66\x65tter_info\x18\x0b \x01(\x0b\x32\x11.AvatarFetterInfo\x12\x12\n\ncostume_id\x18\x0c \x01(\r\x12$\n\nexcel_info\x18\r \x01(\x0b\x32\x10.AvatarExcelInfo\x1a:\n\x0cPropMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\x19\n\x05value\x18\x02 \x01(\x0b\x32\n.PropValue:\x02\x38\x01\x1a\x33\n\x11\x46ightPropMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\x02:\x02\x38\x01\x1a\x34\n\x12SkillLevelMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a>\n\x1cProudSkillExtraLevelMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ShowAvatarInfo_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SHOWAVATARINFO_PROPMAPENTRY._options = None
  _SHOWAVATARINFO_PROPMAPENTRY._serialized_options = b'8\001'
  _SHOWAVATARINFO_FIGHTPROPMAPENTRY._options = None
  _SHOWAVATARINFO_FIGHTPROPMAPENTRY._serialized_options = b'8\001'
  _SHOWAVATARINFO_SKILLLEVELMAPENTRY._options = None
  _SHOWAVATARINFO_SKILLLEVELMAPENTRY._serialized_options = b'8\001'
  _SHOWAVATARINFO_PROUDSKILLEXTRALEVELMAPENTRY._options = None
  _SHOWAVATARINFO_PROUDSKILLEXTRALEVELMAPENTRY._serialized_options = b'8\001'
  _SHOWAVATARINFO._serialized_start=106
  _SHOWAVATARINFO._serialized_end=868
  _SHOWAVATARINFO_PROPMAPENTRY._serialized_start=639
  _SHOWAVATARINFO_PROPMAPENTRY._serialized_end=697
  _SHOWAVATARINFO_FIGHTPROPMAPENTRY._serialized_start=699
  _SHOWAVATARINFO_FIGHTPROPMAPENTRY._serialized_end=750
  _SHOWAVATARINFO_SKILLLEVELMAPENTRY._serialized_start=752
  _SHOWAVATARINFO_SKILLLEVELMAPENTRY._serialized_end=804
  _SHOWAVATARINFO_PROUDSKILLEXTRALEVELMAPENTRY._serialized_start=806
  _SHOWAVATARINFO_PROUDSKILLEXTRALEVELMAPENTRY._serialized_end=868
# @@protoc_insertion_point(module_scope)