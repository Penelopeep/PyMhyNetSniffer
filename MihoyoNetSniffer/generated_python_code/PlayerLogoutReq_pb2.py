# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: PlayerLogoutReq.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15PlayerLogoutReq.proto\"\x8b\x02\n\x0fPlayerLogoutReq\x12\'\n\x06reason\x18\t \x01(\x0e\x32\x17.PlayerLogoutReq.Reason\"\xce\x01\n\x06Reason\x12\x15\n\x11REASON_DISCONNECT\x10\x00\x12\x15\n\x11REASON_CLIENT_REQ\x10\x01\x12\x12\n\x0eREASON_TIMEOUT\x10\x02\x12\x14\n\x10REASON_ADMIN_REQ\x10\x03\x12\x17\n\x13REASON_SERVER_CLOSE\x10\x04\x12\x13\n\x0fREASON_GM_CLEAR\x10\x05\x12\x1a\n\x16REASON_PLAYER_TRANSFER\x10\x06\x12\"\n\x1eREASON_CLIENT_CHECKSUM_INVALID\x10\x07\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'PlayerLogoutReq_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PLAYERLOGOUTREQ._serialized_start=26
  _PLAYERLOGOUTREQ._serialized_end=293
  _PLAYERLOGOUTREQ_REASON._serialized_start=87
  _PLAYERLOGOUTREQ_REASON._serialized_end=293
# @@protoc_insertion_point(module_scope)
