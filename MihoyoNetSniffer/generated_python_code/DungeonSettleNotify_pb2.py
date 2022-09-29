# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: DungeonSettleNotify.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ChannelerSlabLoopDungeonResultInfo_pb2 as ChannelerSlabLoopDungeonResultInfo__pb2
import CrystalLinkSettleInfo_pb2 as CrystalLinkSettleInfo__pb2
import DungeonSettleExhibitionInfo_pb2 as DungeonSettleExhibitionInfo__pb2
import EffigyChallengeDungeonResultInfo_pb2 as EffigyChallengeDungeonResultInfo__pb2
import InstableSpraySettleInfo_pb2 as InstableSpraySettleInfo__pb2
import ParamList_pb2 as ParamList__pb2
import RoguelikeDungeonSettleInfo_pb2 as RoguelikeDungeonSettleInfo__pb2
import StrengthenPointData_pb2 as StrengthenPointData__pb2
import SummerTimeV2DungeonSettleInfo_pb2 as SummerTimeV2DungeonSettleInfo__pb2
import TowerLevelEndNotify_pb2 as TowerLevelEndNotify__pb2
import TrialAvatarFirstPassDungeonNotify_pb2 as TrialAvatarFirstPassDungeonNotify__pb2
import WindFieldDungeonSettleInfo_pb2 as WindFieldDungeonSettleInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x44ungeonSettleNotify.proto\x1a(ChannelerSlabLoopDungeonResultInfo.proto\x1a\x1b\x43rystalLinkSettleInfo.proto\x1a!DungeonSettleExhibitionInfo.proto\x1a&EffigyChallengeDungeonResultInfo.proto\x1a\x1dInstableSpraySettleInfo.proto\x1a\x0fParamList.proto\x1a RoguelikeDungeonSettleInfo.proto\x1a\x19StrengthenPointData.proto\x1a#SummerTimeV2DungeonSettleInfo.proto\x1a\x19TowerLevelEndNotify.proto\x1a\'TrialAvatarFirstPassDungeonNotify.proto\x1a WindFieldDungeonSettleInfo.proto\"\xb6\t\n\x13\x44ungeonSettleNotify\x12\x0e\n\x06result\x18\n \x01(\r\x12\x12\n\ndungeon_id\x18\r \x01(\r\x12S\n\x19strengthen_point_data_map\x18\x0e \x03(\x0b\x32\x30.DungeonSettleNotify.StrengthenPointDataMapEntry\x12:\n\x14\x65xhibition_info_list\x18\x08 \x03(\x0b\x32\x1c.DungeonSettleExhibitionInfo\x12\x1b\n\x13Unk3100_PIFIBCAMAIG\x18\x0c \x01(\r\x12\x16\n\x0e\x66\x61il_cond_list\x18\x0b \x03(\r\x12\x1b\n\x13Unk2700_OMCCFBBDJMI\x18\x01 \x01(\r\x12\x12\n\nclose_time\x18\x04 \x01(\r\x12\x12\n\nis_success\x18\x07 \x01(\x08\x12\x39\n\x0bsettle_show\x18\x05 \x03(\x0b\x32$.DungeonSettleNotify.SettleShowEntry\x12\x37\n\x16tower_level_end_notify\x18\xdf\x02 \x01(\x0b\x32\x14.TowerLevelEndNotifyH\x00\x12U\n&trial_avatar_first_pass_dungeon_notify\x18\xfb\x04 \x01(\x0b\x32\".TrialAvatarFirstPassDungeonNotifyH\x00\x12X\n(channeller_slab_loop_dungeon_result_info\x18\xae\x05 \x01(\x0b\x32#.ChannelerSlabLoopDungeonResultInfoH\x00\x12R\n$effigy_challenge_dungeon_result_info\x18\xc8\x02 \x01(\x0b\x32!.EffigyChallengeDungeonResultInfoH\x00\x12\x45\n\x1droguelike_dungeon_settle_info\x18\xca\x0b \x01(\x0b\x32\x1b.RoguelikeDungeonSettleInfoH\x00\x12:\n\x18\x63rystal_link_settle_info\x18p \x01(\x0b\x32\x16.CrystalLinkSettleInfoH\x00\x12M\n\"summer_time_v2_dungeon_settle_info\x18\xda\x0e \x01(\x0b\x32\x1e.SummerTimeV2DungeonSettleInfoH\x00\x12?\n\x1ainstable_spray_settle_info\x18\xc1\x01 \x01(\x0b\x32\x18.InstableSpraySettleInfoH\x00\x12\x46\n\x1ewind_field_dungeon_settle_info\x18\xa1\x0e \x01(\x0b\x32\x1b.WindFieldDungeonSettleInfoH\x00\x1aS\n\x1bStrengthenPointDataMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.StrengthenPointData:\x02\x38\x01\x1a=\n\x0fSettleShowEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\x19\n\x05value\x18\x02 \x01(\x0b\x32\n.ParamList:\x02\x38\x01\x42\x08\n\x06\x64\x65tailb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'DungeonSettleNotify_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DUNGEONSETTLENOTIFY_STRENGTHENPOINTDATAMAPENTRY._options = None
  _DUNGEONSETTLENOTIFY_STRENGTHENPOINTDATAMAPENTRY._serialized_options = b'8\001'
  _DUNGEONSETTLENOTIFY_SETTLESHOWENTRY._options = None
  _DUNGEONSETTLENOTIFY_SETTLESHOWENTRY._serialized_options = b'8\001'
  _DUNGEONSETTLENOTIFY._serialized_start=424
  _DUNGEONSETTLENOTIFY._serialized_end=1630
  _DUNGEONSETTLENOTIFY_STRENGTHENPOINTDATAMAPENTRY._serialized_start=1474
  _DUNGEONSETTLENOTIFY_STRENGTHENPOINTDATAMAPENTRY._serialized_end=1557
  _DUNGEONSETTLENOTIFY_SETTLESHOWENTRY._serialized_start=1559
  _DUNGEONSETTLENOTIFY_SETTLESHOWENTRY._serialized_end=1620
# @@protoc_insertion_point(module_scope)
