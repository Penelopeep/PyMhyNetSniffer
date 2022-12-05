# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: PlayerLoginRsp.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import BlockInfo_pb2 as BlockInfo__pb2
import FeatureBlockInfo_pb2 as FeatureBlockInfo__pb2
import ResVersionConfig_pb2 as ResVersionConfig__pb2
import ShortAbilityHashPair_pb2 as ShortAbilityHashPair__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14PlayerLoginRsp.proto\x1a\x0f\x42lockInfo.proto\x1a\x16\x46\x65\x61tureBlockInfo.proto\x1a\x16ResVersionConfig.proto\x1a\x1aShortAbilityHashPair.proto\"\xed\t\n\x0ePlayerLoginRsp\x12\x12\n\nlogin_rand\x18\t \x01(\x04\x12\x1b\n\x13Unk3300_DHCMDHHDLFF\x18\x02 \x01(\x0c\x12\x1b\n\x13Unk3300_HMGCPAGLDHB\x18\x10 \x01(\t\x12\x18\n\x0ftotal_tick_time\x18\x92\x04 \x01(\x01\x12\x1b\n\x13Unk3300_LLIJKLDBHNN\x18\x05 \x01(\x08\x12\x11\n\x08is_audit\x18\xa2\x07 \x01(\x08\x12\x11\n\x08\x62irthday\x18\xeb\n \x01(\t\x12\x1b\n\x13Unk3300_HGFNECIJDLN\x18\r \x01(\x08\x12&\n\x1d\x63lient_silence_version_suffix\x18\x8c\x07 \x01(\t\x12\x1e\n\x15\x63lient_version_suffix\x18\xb5\x0e \x01(\t\x12\x1a\n\x11next_resource_url\x18\xac\n \x01(\t\x12\x1c\n\x13Unk3300_EJKCNNDFAAI\x18\xc4\x01 \x01(\x08\x12\x36\n\x16short_ability_hash_map\x18\xdd\n \x03(\x0b\x32\x15.ShortAbilityHashPair\x12\x1d\n\x14is_data_need_relogin\x18\xdf\x08 \x01(\x08\x12.\n\x12res_version_config\x18\xa8\x06 \x01(\x0b\x32\x11.ResVersionConfig\x12#\n\x1b\x63lient_silence_data_version\x18\x01 \x01(\r\x12\x12\n\ntarget_uid\x18\x0f \x01(\r\x12\x1b\n\x13Unk3300_NEICPFBPNPD\x18\x63 \x01(\t\x12\x1c\n\x13Unk3300_CANONIPHMDI\x18\xf2\x0b \x01(\x08\x12\x1b\n\x13Unk3300_IIHDKKNJPGD\x18\x08 \x01(\x08\x12\x1b\n\x13player_data_version\x18\x0e \x01(\r\x12\x1c\n\x13Unk3300_MOPDDGHMKBD\x18\xe0\x0e \x01(\x0c\x12\x15\n\x0c\x63ountry_code\x18\xe8\x02 \x01(\t\x12\x33\n\x17next_res_version_config\x18\x98\r \x01(\x0b\x32\x11.ResVersionConfig\x12\x1b\n\x13Unk3300_IADLIIMGDMC\x18\x11 \x01(\x08\x12:\n\x0e\x62lock_info_map\x18\xe2\x0f \x03(\x0b\x32!.PlayerLoginRsp.BlockInfoMapEntry\x12\x14\n\x0bis_transfer\x18\xa7\x02 \x01(\x08\x12\x1e\n\x15target_home_owner_uid\x18\xbe\x03 \x01(\r\x12\x10\n\x08game_biz\x18\x04 \x01(\t\x12=\n\x10\x61\x62ility_hash_map\x18\x03 \x03(\x0b\x32#.PlayerLoginRsp.AbilityHashMapEntry\x12\x19\n\x11\x61\x62ility_hash_code\x18\x0c \x01(\x05\x12\x1b\n\x13\x63lient_data_version\x18\n \x01(\r\x12\x1c\n\x13Unk3300_OPGDBOLKLJA\x18\x93\n \x01(\t\x12\x0f\n\x07retcode\x18\x07 \x01(\x05\x12\x33\n\x17\x66\x65\x61ture_block_info_list\x18\x8a\x01 \x03(\x0b\x32\x11.FeatureBlockInfo\x1a?\n\x11\x42lockInfoMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\x19\n\x05value\x18\x02 \x01(\x0b\x32\n.BlockInfo:\x02\x38\x01\x1a\x35\n\x13\x41\x62ilityHashMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'PlayerLoginRsp_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PLAYERLOGINRSP_BLOCKINFOMAPENTRY._options = None
  _PLAYERLOGINRSP_BLOCKINFOMAPENTRY._serialized_options = b'8\001'
  _PLAYERLOGINRSP_ABILITYHASHMAPENTRY._options = None
  _PLAYERLOGINRSP_ABILITYHASHMAPENTRY._serialized_options = b'8\001'
  _PLAYERLOGINRSP._serialized_start=118
  _PLAYERLOGINRSP._serialized_end=1379
  _PLAYERLOGINRSP_BLOCKINFOMAPENTRY._serialized_start=1261
  _PLAYERLOGINRSP_BLOCKINFOMAPENTRY._serialized_end=1324
  _PLAYERLOGINRSP_ABILITYHASHMAPENTRY._serialized_start=1326
  _PLAYERLOGINRSP_ABILITYHASHMAPENTRY._serialized_end=1379
# @@protoc_insertion_point(module_scope)
