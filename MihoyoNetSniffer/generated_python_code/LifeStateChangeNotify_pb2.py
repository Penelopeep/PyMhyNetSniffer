# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: LifeStateChangeNotify.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import PlayerDieType_pb2 as PlayerDieType__pb2
import ServerBuff_pb2 as ServerBuff__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bLifeStateChangeNotify.proto\x1a\x13PlayerDieType.proto\x1a\x10ServerBuff.proto\"\xc6\x01\n\x15LifeStateChangeNotify\x12\x10\n\x08\x65ntityId\x18\x07 \x01(\r\x12#\n\x0eserverBuffList\x18\x02 \x03(\x0b\x32\x0b.ServerBuff\x12\x17\n\x0fmoveReliableSeq\x18\x05 \x01(\r\x12\x11\n\tattackTag\x18\r \x01(\t\x12\x16\n\x0esourceEntityId\x18\x0f \x01(\r\x12\x11\n\tlifeState\x18\t \x01(\r\x12\x1f\n\x07\x64ieType\x18\x06 \x01(\x0e\x32\x0e.PlayerDieTypeB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'LifeStateChangeNotify_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _globals['_LIFESTATECHANGENOTIFY']._serialized_start=71
  _globals['_LIFESTATECHANGENOTIFY']._serialized_end=269
# @@protoc_insertion_point(module_scope)
