# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: AsterActivityDetailInfo.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import AsterLargeDetailInfo_pb2 as AsterLargeDetailInfo__pb2
import AsterLittleDetailInfo_pb2 as AsterLittleDetailInfo__pb2
import AsterMidDetailInfo_pb2 as AsterMidDetailInfo__pb2
import AsterProgressDetailInfo_pb2 as AsterProgressDetailInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1d\x41sterActivityDetailInfo.proto\x1a\x1a\x41sterLargeDetailInfo.proto\x1a\x1b\x41sterLittleDetailInfo.proto\x1a\x18\x41sterMidDetailInfo.proto\x1a\x1d\x41sterProgressDetailInfo.proto\"\xcf\x02\n\x17\x41sterActivityDetailInfo\x12\x1a\n\x12\x63ontent_close_time\x18\x0b \x01(\r\x12&\n\taster_mid\x18\x01 \x01(\x0b\x32\x13.AsterMidDetailInfo\x12,\n\x0c\x61ster_little\x18\n \x01(\x0b\x32\x16.AsterLittleDetailInfo\x12\x19\n\x11is_content_closed\x18\x06 \x01(\x08\x12\x30\n\x0e\x61ster_progress\x18\x03 \x01(\x0b\x32\x18.AsterProgressDetailInfo\x12*\n\x0b\x61ster_large\x18\x04 \x01(\x0b\x32\x15.AsterLargeDetailInfo\x12\x13\n\x0bJIIJEJPKLNK\x18\x0e \x01(\r\x12\x13\n\x0bKENCBMFCJDH\x18\r \x01(\r\x12\x1f\n\x17is_special_reward_taken\x18\t \x01(\x08\x42\x13\n\x11layla.sleep.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'AsterActivityDetailInfo_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\021layla.sleep.proto'
  _globals['_ASTERACTIVITYDETAILINFO']._serialized_start=148
  _globals['_ASTERACTIVITYDETAILINFO']._serialized_end=483
# @@protoc_insertion_point(module_scope)
