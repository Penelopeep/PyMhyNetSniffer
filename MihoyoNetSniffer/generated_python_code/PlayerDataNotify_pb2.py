# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: PlayerDataNotify.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import PropValue_pb2 as PropValue__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16PlayerDataNotify.proto\x1a\x0fPropValue.proto\"\xd9\x01\n\x10PlayerDataNotify\x12\x13\n\x0bserver_time\x18\t \x01(\x04\x12\x11\n\tnick_name\x18\x06 \x01(\t\x12\x30\n\x08prop_map\x18\x08 \x03(\x0b\x32\x1e.PlayerDataNotify.PropMapEntry\x12\x1c\n\x14is_first_login_today\x18\x0b \x01(\x08\x12\x11\n\tregion_id\x18\x0f \x01(\r\x1a:\n\x0cPropMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\x19\n\x05value\x18\x02 \x01(\x0b\x32\n.PropValue:\x02\x38\x01\x42\x13\n\x11layla.sleep.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'PlayerDataNotify_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\021layla.sleep.proto'
  _PLAYERDATANOTIFY_PROPMAPENTRY._options = None
  _PLAYERDATANOTIFY_PROPMAPENTRY._serialized_options = b'8\001'
  _globals['_PLAYERDATANOTIFY']._serialized_start=44
  _globals['_PLAYERDATANOTIFY']._serialized_end=261
  _globals['_PLAYERDATANOTIFY_PROPMAPENTRY']._serialized_start=203
  _globals['_PLAYERDATANOTIFY_PROPMAPENTRY']._serialized_end=261
# @@protoc_insertion_point(module_scope)
