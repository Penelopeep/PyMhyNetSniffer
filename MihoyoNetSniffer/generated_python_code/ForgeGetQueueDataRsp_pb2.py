# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ForgeGetQueueDataRsp.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ForgeQueueData_pb2 as ForgeQueueData__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1a\x46orgeGetQueueDataRsp.proto\x1a\x14\x46orgeQueueData.proto\"\xc8\x01\n\x14\x46orgeGetQueueDataRsp\x12\x15\n\rmax_queue_num\x18\x02 \x01(\r\x12\x0f\n\x07retcode\x18\x01 \x01(\x05\x12\x41\n\x0f\x66orge_queue_map\x18\t \x03(\x0b\x32(.ForgeGetQueueDataRsp.ForgeQueueMapEntry\x1a\x45\n\x12\x46orgeQueueMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\x1e\n\x05value\x18\x02 \x01(\x0b\x32\x0f.ForgeQueueData:\x02\x38\x01\x42\x13\n\x11layla.sleep.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ForgeGetQueueDataRsp_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\021layla.sleep.proto'
  _FORGEGETQUEUEDATARSP_FORGEQUEUEMAPENTRY._options = None
  _FORGEGETQUEUEDATARSP_FORGEQUEUEMAPENTRY._serialized_options = b'8\001'
  _globals['_FORGEGETQUEUEDATARSP']._serialized_start=53
  _globals['_FORGEGETQUEUEDATARSP']._serialized_end=253
  _globals['_FORGEGETQUEUEDATARSP_FORGEQUEUEMAPENTRY']._serialized_start=184
  _globals['_FORGEGETQUEUEDATARSP_FORGEQUEUEMAPENTRY']._serialized_end=253
# @@protoc_insertion_point(module_scope)
