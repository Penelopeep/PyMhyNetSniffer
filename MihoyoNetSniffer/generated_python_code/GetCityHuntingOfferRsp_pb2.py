# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: GetCityHuntingOfferRsp.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import HuntingOfferData_pb2 as HuntingOfferData__pb2
import HuntingPair_pb2 as HuntingPair__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cGetCityHuntingOfferRsp.proto\x1a\x16HuntingOfferData.proto\x1a\x11HuntingPair.proto\"\xd1\x01\n\x16GetCityHuntingOfferRsp\x12\x1f\n\x17\x63ur_week_finished_count\x18\x0c \x01(\r\x12\x19\n\x11next_refresh_time\x18\n \x01(\r\x12*\n\x14ongoing_hunting_pair\x18\x0f \x01(\x0b\x32\x0c.HuntingPair\x12\x0f\n\x07retcode\x18\r \x01(\x05\x12-\n\x12hunting_offer_list\x18\x01 \x03(\x0b\x32\x11.HuntingOfferData\x12\x0f\n\x07\x63ity_id\x18\x08 \x01(\rB\x13\n\x11layla.sleep.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'GetCityHuntingOfferRsp_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\021layla.sleep.proto'
  _globals['_GETCITYHUNTINGOFFERRSP']._serialized_start=76
  _globals['_GETCITYHUNTINGOFFERRSP']._serialized_end=285
# @@protoc_insertion_point(module_scope)
