# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: TreasureMapDetectorData.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import Vector_pb2 as Vector__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dTreasureMapDetectorData.proto\x1a\x0cVector.proto\"\x91\x01\n\x17TreasureMapDetectorData\x12\x1b\n\ncenter_pos\x18\x04 \x01(\x0b\x32\x07.Vector\x12\x11\n\tregion_id\x18\r \x01(\r\x12\x1a\n\x12is_region_detected\x18\x01 \x01(\x08\x12\x0e\n\x06radius\x18\x08 \x01(\r\x12\x1a\n\tspot_list\x18\x07 \x03(\x0b\x32\x07.VectorB\x13\n\x11layla.sleep.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'TreasureMapDetectorData_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\021layla.sleep.proto'
  _globals['_TREASUREMAPDETECTORDATA']._serialized_start=48
  _globals['_TREASUREMAPDETECTORDATA']._serialized_end=193
# @@protoc_insertion_point(module_scope)
