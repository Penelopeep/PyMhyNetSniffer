# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: GetActivityInfoRsp.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ActivityInfo_pb2 as ActivityInfo__pb2
import Uint32Pair_pb2 as Uint32Pair__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18GetActivityInfoRsp.proto\x1a\x12\x41\x63tivityInfo.proto\x1a\x10Uint32Pair.proto\"\xa5\x01\n\x12GetActivityInfoRsp\x12\'\n\x10\x61\x63tivityInfoList\x18\r \x03(\x0b\x32\r.ActivityInfo\x12\x38\n#disableTransferPointInteractionList\x18\x03 \x03(\x0b\x32\x0b.Uint32Pair\x12\x1b\n\x13\x61\x63tivatedSaleIdList\x18\x07 \x03(\r\x12\x0f\n\x07retcode\x18\x0e \x01(\x05\x42\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'GetActivityInfoRsp_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _globals['_GETACTIVITYINFORSP']._serialized_start=67
  _globals['_GETACTIVITYINFORSP']._serialized_end=232
# @@protoc_insertion_point(module_scope)
