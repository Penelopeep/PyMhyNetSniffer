# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: MapMarkPoint.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import Vector_pb2 as Vector__pb2
import MapMarkPointType_pb2 as MapMarkPointType__pb2
import MapMarkFromType_pb2 as MapMarkFromType__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12MapMarkPoint.proto\x1a\x0cVector.proto\x1a\x16MapMarkPointType.proto\x1a\x15MapMarkFromType.proto\"\xb1\x01\n\x0cMapMarkPoint\x12\x0f\n\x07sceneId\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x14\n\x03pos\x18\x03 \x01(\x0b\x32\x07.Vector\x12$\n\tpointType\x18\x04 \x01(\x0e\x32\x11.MapMarkPointType\x12\x11\n\tmonsterId\x18\x05 \x01(\r\x12\"\n\x08\x66romType\x18\x06 \x01(\x0e\x32\x10.MapMarkFromType\x12\x0f\n\x07questId\x18\x07 \x01(\rB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'MapMarkPoint_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _globals['_MAPMARKPOINT']._serialized_start=84
  _globals['_MAPMARKPOINT']._serialized_end=261
# @@protoc_insertion_point(module_scope)
