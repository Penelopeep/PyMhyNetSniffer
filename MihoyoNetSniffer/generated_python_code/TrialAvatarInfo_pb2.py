# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: TrialAvatarInfo.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import Item_pb2 as Item__pb2
import TrialAvatarGrantRecord_pb2 as TrialAvatarGrantRecord__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15TrialAvatarInfo.proto\x1a\nItem.proto\x1a\x1cTrialAvatarGrantRecord.proto\"z\n\x0fTrialAvatarInfo\x12\x17\n\x0ftrial_avatar_id\x18\x01 \x01(\r\x12\x1f\n\x10trial_equip_list\x18\x02 \x03(\x0b\x32\x05.Item\x12-\n\x0cgrant_record\x18\x03 \x01(\x0b\x32\x17.TrialAvatarGrantRecordB\x13\n\x11layla.sleep.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'TrialAvatarInfo_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\021layla.sleep.proto'
  _globals['_TRIALAVATARINFO']._serialized_start=67
  _globals['_TRIALAVATARINFO']._serialized_end=189
# @@protoc_insertion_point(module_scope)
