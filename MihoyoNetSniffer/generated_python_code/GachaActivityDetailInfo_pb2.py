# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: GachaActivityDetailInfo.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import GachaStageData_pb2 as GachaStageData__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dGachaActivityDetailInfo.proto\x1a\x14GachaStageData.proto\"\x9c\x03\n\x17GachaActivityDetailInfo\x12@\n\rrobot_num_map\x18\x02 \x03(\x0b\x32).GachaActivityDetailInfo.RobotNumMapEntry\x12\x13\n\x0bIPBJPBFDPAE\x18\x05 \x01(\r\x12V\n\x19have_reward_robot_num_map\x18\t \x03(\x0b\x32\x33.GachaActivityDetailInfo.HaveRewardRobotNumMapEntry\x12.\n\x15gacha_stage_data_list\x18\x06 \x03(\x0b\x32\x0f.GachaStageData\x12\x13\n\x0bMHLIDFAFDGD\x18\x0b \x01(\r\x12\x1b\n\x13have_get_robot_list\x18\x08 \x03(\r\x1a\x32\n\x10RobotNumMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a<\n\x1aHaveRewardRobotNumMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x42\x13\n\x11layla.sleep.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'GachaActivityDetailInfo_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\021layla.sleep.proto'
  _GACHAACTIVITYDETAILINFO_ROBOTNUMMAPENTRY._options = None
  _GACHAACTIVITYDETAILINFO_ROBOTNUMMAPENTRY._serialized_options = b'8\001'
  _GACHAACTIVITYDETAILINFO_HAVEREWARDROBOTNUMMAPENTRY._options = None
  _GACHAACTIVITYDETAILINFO_HAVEREWARDROBOTNUMMAPENTRY._serialized_options = b'8\001'
  _globals['_GACHAACTIVITYDETAILINFO']._serialized_start=56
  _globals['_GACHAACTIVITYDETAILINFO']._serialized_end=468
  _globals['_GACHAACTIVITYDETAILINFO_ROBOTNUMMAPENTRY']._serialized_start=356
  _globals['_GACHAACTIVITYDETAILINFO_ROBOTNUMMAPENTRY']._serialized_end=406
  _globals['_GACHAACTIVITYDETAILINFO_HAVEREWARDROBOTNUMMAPENTRY']._serialized_start=408
  _globals['_GACHAACTIVITYDETAILINFO_HAVEREWARDROBOTNUMMAPENTRY']._serialized_end=468
# @@protoc_insertion_point(module_scope)
