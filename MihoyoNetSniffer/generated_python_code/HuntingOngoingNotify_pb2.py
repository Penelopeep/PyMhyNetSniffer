# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: HuntingOngoingNotify.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import HuntingPair_pb2 as HuntingPair__pb2
import Vector_pb2 as Vector__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1aHuntingOngoingNotify.proto\x1a\x11HuntingPair.proto\x1a\x0cVector.proto\"\xae\x01\n\x14HuntingOngoingNotify\x12\x1e\n\rnext_position\x18\x07 \x01(\x0b\x32\x07.Vector\x12\"\n\x0chunting_pair\x18\x0b \x01(\x0b\x32\x0c.HuntingPair\x12\x11\n\tfail_time\x18\x01 \x01(\r\x12\x19\n\x11\x66inish_clue_count\x18\n \x01(\r\x12\x10\n\x08is_final\x18\t \x01(\x08\x12\x12\n\nis_started\x18\x05 \x01(\x08\x42\x13\n\x11layla.sleep.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'HuntingOngoingNotify_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\021layla.sleep.proto'
  _globals['_HUNTINGONGOINGNOTIFY']._serialized_start=64
  _globals['_HUNTINGONGOINGNOTIFY']._serialized_end=238
# @@protoc_insertion_point(module_scope)
