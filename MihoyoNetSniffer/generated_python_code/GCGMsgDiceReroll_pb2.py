# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: GCGMsgDiceReroll.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import GCGDiceSideType_pb2 as GCGDiceSideType__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16GCGMsgDiceReroll.proto\x1a\x15GCGDiceSideType.proto\"s\n\x10GCGMsgDiceReroll\x12(\n\x0e\x64ice_side_list\x18\x01 \x03(\x0e\x32\x10.GCGDiceSideType\x12\x1e\n\x16select_dice_index_list\x18\x02 \x03(\r\x12\x15\n\rcontroller_id\x18\r \x01(\rB\x13\n\x11layla.sleep.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'GCGMsgDiceReroll_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\021layla.sleep.proto'
  _globals['_GCGMSGDICEREROLL']._serialized_start=49
  _globals['_GCGMSGDICEREROLL']._serialized_end=164
# @@protoc_insertion_point(module_scope)
