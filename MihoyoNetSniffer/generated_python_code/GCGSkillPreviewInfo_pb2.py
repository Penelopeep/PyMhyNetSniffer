# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: GCGSkillPreviewInfo.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import GCGSkillPreviewExtraInfo_pb2 as GCGSkillPreviewExtraInfo__pb2
import GCGSkillPreviewTokenChangeInfo_pb2 as GCGSkillPreviewTokenChangeInfo__pb2
import GCGSkillPreviewOnstageChangeInfo_pb2 as GCGSkillPreviewOnstageChangeInfo__pb2
import GCGSkillPreviewHpInfo_pb2 as GCGSkillPreviewHpInfo__pb2
import GCGSkillPreviewElementReactionInfo_pb2 as GCGSkillPreviewElementReactionInfo__pb2
import GCGSkillPreviewCardInfo_pb2 as GCGSkillPreviewCardInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19GCGSkillPreviewInfo.proto\x1a\x1eGCGSkillPreviewExtraInfo.proto\x1a$GCGSkillPreviewTokenChangeInfo.proto\x1a&GCGSkillPreviewOnstageChangeInfo.proto\x1a\x1bGCGSkillPreviewHpInfo.proto\x1a(GCGSkillPreviewElementReactionInfo.proto\x1a\x1dGCGSkillPreviewCardInfo.proto\"\xd2\x05\n\x13GCGSkillPreviewInfo\x12H\n\x12\x63\x61rdTokenChangeMap\x18\x0c \x03(\x0b\x32,.GCGSkillPreviewInfo.CardTokenChangeMapEntry\x12\x45\n\x1a\x63hangeOnstageCharacterList\x18\x0e \x03(\x0b\x32!.GCGSkillPreviewOnstageChangeInfo\x12,\n\textraInfo\x18\x06 \x01(\x0b\x32\x19.GCGSkillPreviewExtraInfo\x12\x36\n\thpInfoMap\x18\x01 \x03(\x0b\x32#.GCGSkillPreviewInfo.HpInfoMapEntry\x12\x42\n\x0freactionInfoMap\x18\t \x03(\x0b\x32).GCGSkillPreviewInfo.ReactionInfoMapEntry\x12\x35\n\x13Unk3300_AGNONGELFGC\x18\x0b \x03(\x0b\x32\x18.GCGSkillPreviewCardInfo\x12\x0f\n\x07skillId\x18\x02 \x01(\r\x12\x35\n\x13Unk3300_DAJFJEDNLKK\x18\x0f \x03(\x0b\x32\x18.GCGSkillPreviewCardInfo\x1aZ\n\x17\x43\x61rdTokenChangeMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12.\n\x05value\x18\x02 \x01(\x0b\x32\x1f.GCGSkillPreviewTokenChangeInfo:\x02\x38\x01\x1aH\n\x0eHpInfoMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.GCGSkillPreviewHpInfo:\x02\x38\x01\x1a[\n\x14ReactionInfoMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\x32\n\x05value\x18\x02 \x01(\x0b\x32#.GCGSkillPreviewElementReactionInfo:\x02\x38\x01\x42\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'GCGSkillPreviewInfo_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _GCGSKILLPREVIEWINFO_CARDTOKENCHANGEMAPENTRY._options = None
  _GCGSKILLPREVIEWINFO_CARDTOKENCHANGEMAPENTRY._serialized_options = b'8\001'
  _GCGSKILLPREVIEWINFO_HPINFOMAPENTRY._options = None
  _GCGSKILLPREVIEWINFO_HPINFOMAPENTRY._serialized_options = b'8\001'
  _GCGSKILLPREVIEWINFO_REACTIONINFOMAPENTRY._options = None
  _GCGSKILLPREVIEWINFO_REACTIONINFOMAPENTRY._serialized_options = b'8\001'
  _globals['_GCGSKILLPREVIEWINFO']._serialized_start=242
  _globals['_GCGSKILLPREVIEWINFO']._serialized_end=964
  _globals['_GCGSKILLPREVIEWINFO_CARDTOKENCHANGEMAPENTRY']._serialized_start=707
  _globals['_GCGSKILLPREVIEWINFO_CARDTOKENCHANGEMAPENTRY']._serialized_end=797
  _globals['_GCGSKILLPREVIEWINFO_HPINFOMAPENTRY']._serialized_start=799
  _globals['_GCGSKILLPREVIEWINFO_HPINFOMAPENTRY']._serialized_end=871
  _globals['_GCGSKILLPREVIEWINFO_REACTIONINFOMAPENTRY']._serialized_start=873
  _globals['_GCGSKILLPREVIEWINFO_REACTIONINFOMAPENTRY']._serialized_end=964
# @@protoc_insertion_point(module_scope)
