# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: PlayerCompoundMaterialBoostRsp.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import CompoundBoostTakeStatusType_pb2 as CompoundBoostTakeStatusType__pb2
import CompoundQueueData_pb2 as CompoundQueueData__pb2
import ItemParam_pb2 as ItemParam__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$PlayerCompoundMaterialBoostRsp.proto\x1a!CompoundBoostTakeStatusType.proto\x1a\x17\x43ompoundQueueData.proto\x1a\x0fItemParam.proto\"\xbc\x01\n\x1ePlayerCompoundMaterialBoostRsp\x12\x0f\n\x07retcode\x18\r \x01(\x05\x12\x32\n\x16\x63ompound_que_data_list\x18\x08 \x03(\x0b\x32\x12.CompoundQueueData\x12\x31\n\x0btake_status\x18\x03 \x01(\x0e\x32\x1c.CompoundBoostTakeStatusType\x12\"\n\x0etake_item_list\x18\n \x03(\x0b\x32\n.ItemParamB\x13\n\x11layla.sleep.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'PlayerCompoundMaterialBoostRsp_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\021layla.sleep.proto'
  _globals['_PLAYERCOMPOUNDMATERIALBOOSTRSP']._serialized_start=118
  _globals['_PLAYERCOMPOUNDMATERIALBOOSTRSP']._serialized_end=306
# @@protoc_insertion_point(module_scope)
