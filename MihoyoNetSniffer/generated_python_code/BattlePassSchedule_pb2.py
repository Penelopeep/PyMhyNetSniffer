# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: BattlePassSchedule.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import BattlePassCycle_pb2 as BattlePassCycle__pb2
import BattlePassUnlockStatus_pb2 as BattlePassUnlockStatus__pb2
import BattlePassProduct_pb2 as BattlePassProduct__pb2
import BattlePassRewardTag_pb2 as BattlePassRewardTag__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18\x42\x61ttlePassSchedule.proto\x1a\x15\x42\x61ttlePassCycle.proto\x1a\x1c\x42\x61ttlePassUnlockStatus.proto\x1a\x17\x42\x61ttlePassProduct.proto\x1a\x19\x42\x61ttlePassRewardTag.proto\"\xfa\x02\n\x12\x42\x61ttlePassSchedule\x12\x12\n\nscheduleId\x18\x0b \x01(\r\x12\r\n\x05level\x18\n \x01(\r\x12\r\n\x05point\x18\x07 \x01(\r\x12\"\n\x08\x63urCycle\x18\x05 \x01(\x0b\x32\x10.BattlePassCycle\x12\x11\n\tbeginTime\x18\x08 \x01(\r\x12\x19\n\x11paidPlatformFlags\x18\x02 \x01(\r\x12\x0f\n\x07\x65ndTime\x18\x0e \x01(\r\x12\x1e\n\x16isExtraPaidRewardTaken\x18\x0c \x01(\x08\x12-\n\x0frewardTakenList\x18\x03 \x03(\x0b\x32\x14.BattlePassRewardTag\x12\x16\n\x0e\x63urCyclePoints\x18\t \x01(\r\x12\x10\n\x08isViewed\x18\x04 \x01(\x08\x12-\n\x0cunlockStatus\x18\x06 \x01(\x0e\x32\x17.BattlePassUnlockStatus\x12\'\n\x0bproductInfo\x18\x0f \x01(\x0b\x32\x12.BattlePassProductB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'BattlePassSchedule_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _globals['_BATTLEPASSSCHEDULE']._serialized_start=134
  _globals['_BATTLEPASSSCHEDULE']._serialized_end=512
# @@protoc_insertion_point(module_scope)
