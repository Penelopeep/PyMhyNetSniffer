# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: TowerAllDataRsp.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import TowerCurLevelRecord_pb2 as TowerCurLevelRecord__pb2
import TowerMonthlyBrief_pb2 as TowerMonthlyBrief__pb2
import TowerFloorRecord_pb2 as TowerFloorRecord__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15TowerAllDataRsp.proto\x1a\x19TowerCurLevelRecord.proto\x1a\x17TowerMonthlyBrief.proto\x1a\x16TowerFloorRecord.proto\"\x9f\x06\n\x0fTowerAllDataRsp\x12\x1b\n\x13Unk3300_OHCHCJGJIDK\x18\x07 \x01(\r\x12,\n\x0e\x63urLevelRecord\x18\x01 \x01(\x0b\x32\x14.TowerCurLevelRecord\x12\x17\n\x0fisFirstInteract\x18\x08 \x01(\x08\x12/\n\x14towerFloorRecordList\x18\x06 \x03(\x0b\x32\x11.TowerFloorRecord\x12\x1e\n\x16nextScheduleChangeTime\x18\x0f \x01(\r\x12\x17\n\x0ftowerScheduleId\x18\t \x01(\r\x12@\n\x10\x66loorOpenTimeMap\x18\x0c \x03(\x0b\x32&.TowerAllDataRsp.FloorOpenTimeMapEntry\x12\x1b\n\x13validTowerRecordNum\x18\x05 \x01(\r\x12Z\n\x1dskipFloorGrantedRewardItemMap\x18\x0b \x03(\x0b\x32\x33.TowerAllDataRsp.SkipFloorGrantedRewardItemMapEntry\x12\x1a\n\x11scheduleStartTime\x18\xcf\x04 \x01(\r\x12\x35\n\x18lastScheduleMonthlyBrief\x18\xca\x0b \x01(\x0b\x32\x12.TowerMonthlyBrief\x12\x1b\n\x13Unk3300_LEKODCFPINJ\x18\n \x01(\r\x12\x1b\n\x13Unk3300_HCDFJBHMHHF\x18\x03 \x01(\r\x12\x1b\n\x13Unk3300_JBACKENDHDG\x18\x0e \x01(\r\x12\x1f\n\x17isFinishedEntranceFloor\x18\x02 \x01(\x08\x12(\n\x0cmonthlyBrief\x18\r \x01(\x0b\x32\x12.TowerMonthlyBrief\x12\x0f\n\x07retcode\x18\x04 \x01(\x05\x1a\x37\n\x15\x46loorOpenTimeMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a\x44\n\"SkipFloorGrantedRewardItemMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x42\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'TowerAllDataRsp_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _TOWERALLDATARSP_FLOOROPENTIMEMAPENTRY._options = None
  _TOWERALLDATARSP_FLOOROPENTIMEMAPENTRY._serialized_options = b'8\001'
  _TOWERALLDATARSP_SKIPFLOORGRANTEDREWARDITEMMAPENTRY._options = None
  _TOWERALLDATARSP_SKIPFLOORGRANTEDREWARDITEMMAPENTRY._serialized_options = b'8\001'
  _globals['_TOWERALLDATARSP']._serialized_start=102
  _globals['_TOWERALLDATARSP']._serialized_end=901
  _globals['_TOWERALLDATARSP_FLOOROPENTIMEMAPENTRY']._serialized_start=776
  _globals['_TOWERALLDATARSP_FLOOROPENTIMEMAPENTRY']._serialized_end=831
  _globals['_TOWERALLDATARSP_SKIPFLOORGRANTEDREWARDITEMMAPENTRY']._serialized_start=833
  _globals['_TOWERALLDATARSP_SKIPFLOORGRANTEDREWARDITEMMAPENTRY']._serialized_end=901
# @@protoc_insertion_point(module_scope)
