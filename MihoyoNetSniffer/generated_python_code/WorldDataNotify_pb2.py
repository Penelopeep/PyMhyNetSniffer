# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WorldDataNotify.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import PropValue_pb2 as PropValue__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15WorldDataNotify.proto\x1a\x0fPropValue.proto\"\x8c\x01\n\x0fWorldDataNotify\x12\x38\n\x0cworldPropMap\x18\x03 \x03(\x0b\x32\".WorldDataNotify.WorldPropMapEntry\x1a?\n\x11WorldPropMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\x19\n\x05value\x18\x02 \x01(\x0b\x32\n.PropValue:\x02\x38\x01\x42\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'WorldDataNotify_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _WORLDDATANOTIFY_WORLDPROPMAPENTRY._options = None
  _WORLDDATANOTIFY_WORLDPROPMAPENTRY._serialized_options = b'8\001'
  _globals['_WORLDDATANOTIFY']._serialized_start=43
  _globals['_WORLDDATANOTIFY']._serialized_end=183
  _globals['_WORLDDATANOTIFY_WORLDPROPMAPENTRY']._serialized_start=120
  _globals['_WORLDDATANOTIFY_WORLDPROPMAPENTRY']._serialized_end=183
# @@protoc_insertion_point(module_scope)
