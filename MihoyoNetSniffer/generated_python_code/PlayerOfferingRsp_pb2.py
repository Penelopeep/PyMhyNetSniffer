# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: PlayerOfferingRsp.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ItemParam_pb2 as ItemParam__pb2
import PlayerOfferingData_pb2 as PlayerOfferingData__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17PlayerOfferingRsp.proto\x1a\x0fItemParam.proto\x1a\x18PlayerOfferingData.proto\"o\n\x11PlayerOfferingRsp\x12*\n\roffering_data\x18\x01 \x01(\x0b\x32\x13.PlayerOfferingData\x12\x0f\n\x07retcode\x18\x05 \x01(\x05\x12\x1d\n\titem_list\x18\x0e \x03(\x0b\x32\n.ItemParamB\x13\n\x11layla.sleep.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'PlayerOfferingRsp_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\021layla.sleep.proto'
  _globals['_PLAYEROFFERINGRSP']._serialized_start=70
  _globals['_PLAYEROFFERINGRSP']._serialized_end=181
# @@protoc_insertion_point(module_scope)
