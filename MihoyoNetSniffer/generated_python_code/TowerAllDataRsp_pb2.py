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


import DKDAOPDHNED_pb2 as DKDAOPDHNED__pb2
import TowerCurLevelRecord_pb2 as TowerCurLevelRecord__pb2
import TowerFloorRecord_pb2 as TowerFloorRecord__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15TowerAllDataRsp.proto\x1a\x11\x44KDAOPDHNED.proto\x1a\x19TowerCurLevelRecord.proto\x1a\x16TowerFloorRecord.proto\"\x8d\x05\n\x0fTowerAllDataRsp\x12\x36\n\x0b\x42POEDICFILA\x18\x06 \x03(\x0b\x32!.TowerAllDataRsp.BPOEDICFILAEntry\x12!\n\x0bGPCJOCOKPCL\x18\x02 \x01(\x0b\x32\x0c.DKDAOPDHNED\x12\x13\n\x0b\x42\x41JALPKLOHN\x18\x0b \x01(\r\x12\x13\n\x0bOGLKMJOBNAK\x18\x03 \x01(\r\x12\x0f\n\x07retcode\x18\t \x01(\x05\x12\x13\n\x0b\x43KCFIIGKHMJ\x18\x0f \x01(\r\x12\x19\n\x11is_first_interact\x18\x0e \x01(\x08\x12\x13\n\x0b\x45JMAMALGICG\x18\x0c \x01(\r\x12\x13\n\x0bIOOHBFIGKHH\x18\r \x01(\r\x12\x36\n\x0b\x41HFICLOPFLC\x18\n \x03(\x0b\x32!.TowerAllDataRsp.AHFICLOPFLCEntry\x12\x32\n\x17tower_floor_record_list\x18\x01 \x03(\x0b\x32\x11.TowerFloorRecord\x12\"\n\x1ais_finished_entrance_floor\x18\x04 \x01(\x08\x12\x13\n\x0b\x43\x46\x45HKIFIKFB\x18\x07 \x01(\r\x12\x14\n\x0b\x41MFOBDDCIHK\x18\xde\r \x01(\r\x12\"\n\x0bHCLHNDJDAPC\x18\xee\x04 \x01(\x0b\x32\x0c.DKDAOPDHNED\x12\x13\n\x0b\x41KANNMFELNA\x18\x08 \x01(\r\x12.\n\x10\x63ur_level_record\x18\x05 \x01(\x0b\x32\x14.TowerCurLevelRecord\x1a\x32\n\x10\x42POEDICFILAEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a\x32\n\x10\x41HFICLOPFLCEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x42\x13\n\x11layla.sleep.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'TowerAllDataRsp_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\021layla.sleep.proto'
  _TOWERALLDATARSP_BPOEDICFILAENTRY._options = None
  _TOWERALLDATARSP_BPOEDICFILAENTRY._serialized_options = b'8\001'
  _TOWERALLDATARSP_AHFICLOPFLCENTRY._options = None
  _TOWERALLDATARSP_AHFICLOPFLCENTRY._serialized_options = b'8\001'
  _globals['_TOWERALLDATARSP']._serialized_start=96
  _globals['_TOWERALLDATARSP']._serialized_end=749
  _globals['_TOWERALLDATARSP_BPOEDICFILAENTRY']._serialized_start=647
  _globals['_TOWERALLDATARSP_BPOEDICFILAENTRY']._serialized_end=697
  _globals['_TOWERALLDATARSP_AHFICLOPFLCENTRY']._serialized_start=699
  _globals['_TOWERALLDATARSP_AHFICLOPFLCENTRY']._serialized_end=749
# @@protoc_insertion_point(module_scope)
