# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: QueryPathReq.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import Vector3Int_pb2 as Vector3Int__pb2
import OptionType_pb2 as OptionType__pb2
import QueryFilter_pb2 as QueryFilter__pb2
import Vector_pb2 as Vector__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12QueryPathReq.proto\x1a\x10Vector3Int.proto\x1a\x10OptionType.proto\x1a\x11QueryFilter.proto\x1a\x0cVector.proto\"\xff\x01\n\x0cQueryPathReq\x12\x0f\n\x07queryId\x18\r \x01(\x05\x12\x1f\n\x0e\x64\x65stinationPos\x18\x04 \x03(\x0b\x32\x07.Vector\x12(\n\x13Unk3300_LHNGPJFOMIK\x18\x05 \x01(\x0b\x32\x0b.Vector3Int\x12\x1e\n\tqueryType\x18\x0c \x01(\x0e\x32\x0b.OptionType\x12\x1c\n\x06\x66ilter\x18\x02 \x01(\x0b\x32\x0c.QueryFilter\x12(\n\x13Unk3300_CLGJBBJDOLN\x18\x0f \x01(\x0b\x32\x0b.Vector3Int\x12\x0f\n\x07sceneId\x18\x07 \x01(\r\x12\x1a\n\tsourcePos\x18\n \x01(\x0b\x32\x07.VectorB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'QueryPathReq_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _globals['_QUERYPATHREQ']._serialized_start=92
  _globals['_QUERYPATHREQ']._serialized_end=347
# @@protoc_insertion_point(module_scope)
