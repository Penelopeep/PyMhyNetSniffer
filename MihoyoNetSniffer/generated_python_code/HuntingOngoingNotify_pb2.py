# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: HuntingOngoingNotify.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import HuntingPair_pb2 as HuntingPair__pb2
import Vector_pb2 as Vector__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1aHuntingOngoingNotify.proto\x1a\x11HuntingPair.proto\x1a\x0cVector.proto\"\xa7\x01\n\x14HuntingOngoingNotify\x12\x10\n\x08\x66\x61ilTime\x18\t \x01(\r\x12\x17\n\x0f\x66inishClueCount\x18\x08 \x01(\r\x12\x11\n\tisStarted\x18\x05 \x01(\x08\x12!\n\x0bhuntingPair\x18\n \x01(\x0b\x32\x0c.HuntingPair\x12\x1d\n\x0cnextPosition\x18\x0e \x01(\x0b\x32\x07.Vector\x12\x0f\n\x07isFinal\x18\x0b \x01(\x08\x42\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'HuntingOngoingNotify_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _globals['_HUNTINGONGOINGNOTIFY']._serialized_start=64
  _globals['_HUNTINGONGOINGNOTIFY']._serialized_end=231
# @@protoc_insertion_point(module_scope)
