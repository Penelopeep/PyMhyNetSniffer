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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18GetActivityInfoRsp.proto\x1a\x12\x41\x63tivityInfo.proto\x1a\x10Uint32Pair.proto\"\xae\x01\n\x12GetActivityInfoRsp\x12\x1e\n\x16\x61\x63tivated_sale_id_list\x18\x05 \x03(\r\x12)\n\x12\x61\x63tivity_info_list\x18\t \x03(\x0b\x32\r.ActivityInfo\x12\x0f\n\x07retcode\x18\x0b \x01(\x05\x12<\n\'disable_transfer_point_interaction_list\x18\x0f \x03(\x0b\x32\x0b.Uint32PairB\x13\n\x11layla.sleep.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'GetActivityInfoRsp_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\021layla.sleep.proto'
  _globals['_GETACTIVITYINFORSP']._serialized_start=67
  _globals['_GETACTIVITYINFORSP']._serialized_end=241
# @@protoc_insertion_point(module_scope)
