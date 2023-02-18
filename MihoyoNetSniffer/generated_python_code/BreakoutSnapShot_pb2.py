# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: BreakoutSnapShot.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import BreakoutPhysicalObject_pb2 as BreakoutPhysicalObject__pb2
import BreakoutAction_pb2 as BreakoutAction__pb2
import BreakoutSpawnPoint_pb2 as BreakoutSpawnPoint__pb2
import BreakoutElementReactionCounter_pb2 as BreakoutElementReactionCounter__pb2
import BreakoutSyncConnectUidInfo_pb2 as BreakoutSyncConnectUidInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16\x42reakoutSnapShot.proto\x1a\x1c\x42reakoutPhysicalObject.proto\x1a\x14\x42reakoutAction.proto\x1a\x18\x42reakoutSpawnPoint.proto\x1a$BreakoutElementReactionCounter.proto\x1a BreakoutSyncConnectUidInfo.proto\"\xa8\x05\n\x10\x42reakoutSnapShot\x12\x16\n\x0e\x63lientGameTime\x18\x01 \x01(\x04\x12\x16\n\x0eserverGameTime\x18\x02 \x01(\x04\x12)\n\x08\x62\x61llList\x18\x03 \x03(\x0b\x32\x17.BreakoutPhysicalObject\x12\x33\n\x12physicalObjectList\x18\x04 \x03(\x0b\x32\x17.BreakoutPhysicalObject\x12#\n\nactionList\x18\x05 \x03(\x0b\x32\x0f.BreakoutAction\x12\x11\n\twaveIndex\x18\x06 \x01(\r\x12\x10\n\x08isFinish\x18\x07 \x01(\x08\x12\r\n\x05score\x18\x08 \x01(\r\x12\r\n\x05\x63ombo\x18\t \x01(\r\x12\x10\n\x08maxCombo\x18\n \x01(\r\x12\x11\n\tlifeCount\x18\x0b \x01(\r\x12\x16\n\x0ewaveSuiteIndex\x18\x0c \x01(\r\x12+\n\x0espawnPointList\x18\r \x03(\x0b\x32\x13.BreakoutSpawnPoint\x12\x17\n\x0fremainingBossHp\x18\x0e \x01(\r\x12\x41\n\x18\x62rickElementReactionList\x18\x0f \x03(\x0b\x32\x1f.BreakoutElementReactionCounter\x12@\n\x17\x62\x61llElementReactionList\x18\x10 \x03(\x0b\x32\x1f.BreakoutElementReactionCounter\x12\x30\n\x0buidInfoList\x18\x11 \x03(\x0b\x32\x1b.BreakoutSyncConnectUidInfo\x12\x32\n\x11\x64ynamicObjectList\x18\x12 \x03(\x0b\x32\x17.BreakoutPhysicalObject\x12\x13\n\x0bidIndexList\x18\x13 \x03(\r\x12\x19\n\x11rawClientGameTime\x18\x14 \x01(\x05\x42\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'BreakoutSnapShot_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _globals['_BREAKOUTSNAPSHOT']._serialized_start=177
  _globals['_BREAKOUTSNAPSHOT']._serialized_end=857
# @@protoc_insertion_point(module_scope)
