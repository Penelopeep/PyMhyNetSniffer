# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: EvtEntityRenderersChangedNotify.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import EntityRendererChangedInfo_pb2 as EntityRendererChangedInfo__pb2
import ForwardType_pb2 as ForwardType__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%EvtEntityRenderersChangedNotify.proto\x1a\x1f\x45ntityRendererChangedInfo.proto\x1a\x11\x46orwardType.proto\"\xac\x01\n\x1f\x45vtEntityRenderersChangedNotify\x12\x39\n\x15renderer_changed_info\x18\x0f \x01(\x0b\x32\x1a.EntityRendererChangedInfo\x12\x11\n\tentity_id\x18\n \x01(\r\x12\x17\n\x0fis_server_cache\x18\x04 \x01(\x08\x12\"\n\x0c\x66orward_type\x18\x07 \x01(\x0e\x32\x0c.ForwardTypeB\x13\n\x11layla.sleep.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'EvtEntityRenderersChangedNotify_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\021layla.sleep.proto'
  _globals['_EVTENTITYRENDERERSCHANGEDNOTIFY']._serialized_start=94
  _globals['_EVTENTITYRENDERERSCHANGEDNOTIFY']._serialized_end=266
# @@protoc_insertion_point(module_scope)
