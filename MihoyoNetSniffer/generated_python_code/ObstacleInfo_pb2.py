# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ObstacleInfo.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import MathQuaternion_pb2 as MathQuaternion__pb2
import Vector_pb2 as Vector__pb2
import Vector3Int_pb2 as Vector3Int__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12ObstacleInfo.proto\x1a\x14MathQuaternion.proto\x1a\x0cVector.proto\x1a\x10Vector3Int.proto\"\xe6\x01\n\x0cObstacleInfo\x12&\n\x05shape\x18\x01 \x01(\x0e\x32\x17.ObstacleInfo.ShapeType\x12!\n\x08rotation\x18\r \x01(\x0b\x32\x0f.MathQuaternion\x12\x1c\n\x07\x65xtents\x18\x0b \x01(\x0b\x32\x0b.Vector3Int\x12\x13\n\x0bobstacle_id\x18\x02 \x01(\x05\x12\x17\n\x06\x63\x65nter\x18\t \x01(\x0b\x32\x07.Vector\"?\n\tShapeType\x12\x1a\n\x16OBSTACLE_SHAPE_CAPSULE\x10\x00\x12\x16\n\x12OBSTACLE_SHAPE_BOX\x10\x01\x42\x13\n\x11layla.sleep.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ObstacleInfo_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\021layla.sleep.proto'
  _globals['_OBSTACLEINFO']._serialized_start=77
  _globals['_OBSTACLEINFO']._serialized_end=307
  _globals['_OBSTACLEINFO_SHAPETYPE']._serialized_start=244
  _globals['_OBSTACLEINFO_SHAPETYPE']._serialized_end=307
# @@protoc_insertion_point(module_scope)
