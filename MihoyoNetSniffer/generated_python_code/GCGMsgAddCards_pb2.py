# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: GCGMsgAddCards.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import GCGReason_pb2 as GCGReason__pb2
import GCGZoneType_pb2 as GCGZoneType__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14GCGMsgAddCards.proto\x1a\x0fGCGReason.proto\x1a\x11GCGZoneType.proto\"\x84\x01\n\x0eGCGMsgAddCards\x12\x16\n\x0e\x63\x61rd_guid_list\x18\x06 \x03(\r\x12\x1a\n\x06reason\x18\r \x01(\x0e\x32\n.GCGReason\x12\x15\n\rcontroller_id\x18\t \x01(\r\x12\x1a\n\x04zone\x18\x02 \x01(\x0e\x32\x0c.GCGZoneType\x12\x0b\n\x03pos\x18\x05 \x01(\rB\x13\n\x11layla.sleep.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'GCGMsgAddCards_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\021layla.sleep.proto'
  _globals['_GCGMSGADDCARDS']._serialized_start=61
  _globals['_GCGMSGADDCARDS']._serialized_end=193
# @@protoc_insertion_point(module_scope)
