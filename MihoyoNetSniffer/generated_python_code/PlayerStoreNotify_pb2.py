# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: PlayerStoreNotify.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import StoreType_pb2 as StoreType__pb2
import Item_pb2 as Item__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17PlayerStoreNotify.proto\x1a\x0fStoreType.proto\x1a\nItem.proto\"`\n\x11PlayerStoreNotify\x12\x17\n\x08itemList\x18\x05 \x03(\x0b\x32\x05.Item\x12\x13\n\x0bweightLimit\x18\x06 \x01(\r\x12\x1d\n\tstoreType\x18\n \x01(\x0e\x32\n.StoreTypeB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'PlayerStoreNotify_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _globals['_PLAYERSTORENOTIFY']._serialized_start=56
  _globals['_PLAYERSTORENOTIFY']._serialized_end=152
# @@protoc_insertion_point(module_scope)
