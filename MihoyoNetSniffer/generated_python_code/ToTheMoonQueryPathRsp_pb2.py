# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ToTheMoonQueryPathRsp.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import Vector_pb2 as Vector__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bToTheMoonQueryPathRsp.proto\x1a\x0cVector.proto\"\x95\x02\n\x15ToTheMoonQueryPathRsp\x12\r\n\x05index\x18\x05 \x03(\x03\x12\x18\n\x07\x63orners\x18\x03 \x03(\x0b\x32\x07.Vector\x12\x10\n\x08query_id\x18\x0f \x01(\x05\x12\x0f\n\x07retcode\x18\n \x01(\x05\x12\r\n\x05level\x18\x08 \x03(\x05\x12;\n\x0cquery_status\x18\x0e \x01(\x0e\x32%.ToTheMoonQueryPathRsp.PathStatusType\"d\n\x0ePathStatusType\x12\x19\n\x15PATH_STATUS_TYPE_FAIL\x10\x00\x12\x19\n\x15PATH_STATUS_TYPE_SUCC\x10\x01\x12\x1c\n\x18PATH_STATUS_TYPE_PARTIAL\x10\x02\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ToTheMoonQueryPathRsp_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _TOTHEMOONQUERYPATHRSP._serialized_start=46
  _TOTHEMOONQUERYPATHRSP._serialized_end=323
  _TOTHEMOONQUERYPATHRSP_PATHSTATUSTYPE._serialized_start=223
  _TOTHEMOONQUERYPATHRSP_PATHSTATUSTYPE._serialized_end=323
# @@protoc_insertion_point(module_scope)