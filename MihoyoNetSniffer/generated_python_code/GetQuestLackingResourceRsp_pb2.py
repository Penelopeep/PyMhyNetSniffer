# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: GetQuestLackingResourceRsp.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n GetQuestLackingResourceRsp.proto\"\xf1\x02\n\x1aGetQuestLackingResourceRsp\x12\x45\n\x0elacked_npc_map\x18\x06 \x03(\x0b\x32-.GetQuestLackingResourceRsp.LackedNpcMapEntry\x12\x19\n\x11lacked_place_list\x18\x0f \x03(\r\x12\x10\n\x08quest_id\x18\x08 \x01(\r\x12\x0f\n\x07retcode\x18\x0e \x01(\x05\x12I\n\x10lacked_place_map\x18\x05 \x03(\x0b\x32/.GetQuestLackingResourceRsp.LackedPlaceMapEntry\x12\x17\n\x0flacked_npc_list\x18\x04 \x03(\r\x1a\x33\n\x11LackedNpcMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a\x35\n\x13LackedPlaceMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x42\x13\n\x11layla.sleep.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'GetQuestLackingResourceRsp_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\021layla.sleep.proto'
  _GETQUESTLACKINGRESOURCERSP_LACKEDNPCMAPENTRY._options = None
  _GETQUESTLACKINGRESOURCERSP_LACKEDNPCMAPENTRY._serialized_options = b'8\001'
  _GETQUESTLACKINGRESOURCERSP_LACKEDPLACEMAPENTRY._options = None
  _GETQUESTLACKINGRESOURCERSP_LACKEDPLACEMAPENTRY._serialized_options = b'8\001'
  _globals['_GETQUESTLACKINGRESOURCERSP']._serialized_start=37
  _globals['_GETQUESTLACKINGRESOURCERSP']._serialized_end=406
  _globals['_GETQUESTLACKINGRESOURCERSP_LACKEDNPCMAPENTRY']._serialized_start=300
  _globals['_GETQUESTLACKINGRESOURCERSP_LACKEDNPCMAPENTRY']._serialized_end=351
  _globals['_GETQUESTLACKINGRESOURCERSP_LACKEDPLACEMAPENTRY']._serialized_start=353
  _globals['_GETQUESTLACKINGRESOURCERSP_LACKEDPLACEMAPENTRY']._serialized_end=406
# @@protoc_insertion_point(module_scope)
