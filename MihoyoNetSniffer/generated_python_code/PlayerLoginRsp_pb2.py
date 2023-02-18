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


import bytes_pb2 as bytes__pb2
import ResVersionConfig_pb2 as ResVersionConfig__pb2
import FeatureBlockInfo_pb2 as FeatureBlockInfo__pb2
import BlockInfo_pb2 as BlockInfo__pb2
import ShortAbilityHashPair_pb2 as ShortAbilityHashPair__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14PlayerLoginRsp.proto\x1a\x0b\x62ytes.proto\x1a\x16ResVersionConfig.proto\x1a\x16\x46\x65\x61tureBlockInfo.proto\x1a\x0f\x42lockInfo.proto\x1a\x1aShortAbilityHashPair.proto\"\x8a\t\n\x0ePlayerLoginRsp\x12\x10\n\x07isAudit\x18\xc9\x01 \x01(\x08\x12\x1b\n\x13Unk3300_IIHDKKNJPGD\x18\x06 \x01(\x08\x12\x12\n\tclientMd5\x18\xae\x08 \x01(\t\x12\x19\n\x11playerDataVersion\x18\t \x01(\r\x12\x1c\n\x13\x63lientVersionSuffix\x18\xf0\x04 \x01(\t\x12\x11\n\tloginRand\x18\x08 \x01(\x04\x12\x30\n\x14\x66\x65\x61tureBlockInfoList\x18\xf3\x0f \x03(\x0b\x32\x11.FeatureBlockInfo\x12\x18\n\x10isUseAbilityHash\x18\x0f \x01(\x08\x12\x11\n\x08isScOpen\x18\xbc\x0e \x01(\x08\x12\x12\n\nplayerData\x18\x0e \x01(\x0c\x12\x16\n\rtotalTickTime\x18\xe9\r \x01(\x01\x12\x38\n\x0c\x62lockInfoMap\x18\xd6\x07 \x03(\x0b\x32!.PlayerLoginRsp.BlockInfoMapEntry\x12\x14\n\x0b\x63ountryCode\x18\xee\x01 \x01(\t\x12,\n\x10resVersionConfig\x18\x89\x06 \x01(\x0b\x32\x11.ResVersionConfig\x12 \n\x18\x63lientSilenceDataVersion\x18\x02 \x01(\r\x12#\n\x1a\x63lientSilenceVersionSuffix\x18\xa7\x07 \x01(\t\x12\x1c\n\x13Unk3300_EJKCNNDFAAI\x18\xe6\t \x01(\x08\x12\x19\n\x10\x63lientSilenceMd5\x18\xd3\x07 \x01(\t\x12\x1a\n\x11isDataNeedRelogin\x18\xfd\x07 \x01(\x08\x12\x33\n\x13shortAbilityHashMap\x18\xaf\t \x03(\x0b\x32\x15.ShortAbilityHashPair\x12\x11\n\ttargetUid\x18\x03 \x01(\r\x12\x0f\n\x07gameBiz\x18\x04 \x01(\t\x12\x13\n\nisTransfer\x18\xbc\x07 \x01(\x08\x12\x0f\n\x07retcode\x18\x01 \x01(\x05\x12;\n\x0e\x61\x62ilityHashMap\x18\x05 \x03(\x0b\x32#.PlayerLoginRsp.AbilityHashMapEntry\x12\x1c\n\x13Unk3300_IADLIIMGDMC\x18\x9b\x0b \x01(\x08\x12\x0f\n\x06scInfo\x18\x97\x01 \x01(\x0c\x12\x1b\n\x13Unk3300_HGFNECIJDLN\x18\n \x01(\x08\x12\x19\n\x11\x63lientDataVersion\x18\x07 \x01(\r\x12\x1b\n\x12targetHomeOwnerUid\x18\x93\x06 \x01(\r\x12\x14\n\x0bregisterCps\x18\xa8\x04 \x01(\t\x12\x11\n\x08\x62irthday\x18\xa3\x01 \x01(\t\x12\x30\n\x14nextResVersionConfig\x18\xb3\n \x01(\x0b\x32\x11.ResVersionConfig\x12\x17\n\x0f\x61\x62ilityHashCode\x18\r \x01(\x05\x12\x18\n\x0fnextResourceUrl\x18\xc7\x08 \x01(\t\x1a?\n\x11\x42lockInfoMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\x19\n\x05value\x18\x02 \x01(\x0b\x32\n.BlockInfo:\x02\x38\x01\x1a\x35\n\x13\x41\x62ilityHashMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x42\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'PlayerLoginRsp_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _PLAYERLOGINRSP_BLOCKINFOMAPENTRY._options = None
  _PLAYERLOGINRSP_BLOCKINFOMAPENTRY._serialized_options = b'8\001'
  _PLAYERLOGINRSP_ABILITYHASHMAPENTRY._options = None
  _PLAYERLOGINRSP_ABILITYHASHMAPENTRY._serialized_options = b'8\001'
  _globals['_PLAYERLOGINRSP']._serialized_start=131
  _globals['_PLAYERLOGINRSP']._serialized_end=1293
  _globals['_PLAYERLOGINRSP_BLOCKINFOMAPENTRY']._serialized_start=1175
  _globals['_PLAYERLOGINRSP_BLOCKINFOMAPENTRY']._serialized_end=1238
  _globals['_PLAYERLOGINRSP_ABILITYHASHMAPENTRY']._serialized_start=1240
  _globals['_PLAYERLOGINRSP_ABILITYHASHMAPENTRY']._serialized_end=1293
# @@protoc_insertion_point(module_scope)
