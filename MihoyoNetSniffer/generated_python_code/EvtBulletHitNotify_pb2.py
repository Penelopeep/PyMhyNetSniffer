# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: EvtBulletHitNotify.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import Vector_pb2 as Vector__pb2
import ForwardType_pb2 as ForwardType__pb2
import HitColliderType_pb2 as HitColliderType__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18\x45vtBulletHitNotify.proto\x1a\x0cVector.proto\x1a\x11\x46orwardType.proto\x1a\x15HitColliderType.proto\"\x82\x02\n\x12\x45vtBulletHitNotify\x12\x1a\n\thitNormal\x18\x04 \x01(\x0b\x32\x07.Vector\x12\x13\n\x0bhitEntityId\x18\x0e \x01(\r\x12\x13\n\x0bhitBoxIndex\x18\x0f \x01(\x05\x12!\n\x0b\x66orwardType\x18\x06 \x01(\x0e\x32\x0c.ForwardType\x12\x10\n\x08\x65ntityId\x18\n \x01(\r\x12\x13\n\x0b\x66orwardPeer\x18\r \x01(\r\x12\x16\n\x0esingleBulletId\x18\x0c \x01(\r\x12)\n\x0fhitColliderType\x18\x08 \x01(\x0e\x32\x10.HitColliderType\x12\x19\n\x08hitPoint\x18\x01 \x01(\x0b\x32\x07.VectorB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'EvtBulletHitNotify_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _globals['_EVTBULLETHITNOTIFY']._serialized_start=85
  _globals['_EVTBULLETHITNOTIFY']._serialized_end=343
# @@protoc_insertion_point(module_scope)
