# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: BatchBuyGoodsRsp.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import BuyGoodsParam_pb2 as BuyGoodsParam__pb2
import ShopGoods_pb2 as ShopGoods__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16\x42\x61tchBuyGoodsRsp.proto\x1a\x13\x42uyGoodsParam.proto\x1a\x0fShopGoods.proto\"~\n\x10\x42\x61tchBuyGoodsRsp\x12&\n\x0e\x62uy_goods_list\x18\t \x03(\x0b\x32\x0e.BuyGoodsParam\x12\x1e\n\ngoods_list\x18\x0f \x03(\x0b\x32\n.ShopGoods\x12\x0f\n\x07retcode\x18\x0b \x01(\x05\x12\x11\n\tshop_type\x18\r \x01(\rB\x13\n\x11layla.sleep.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'BatchBuyGoodsRsp_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\021layla.sleep.proto'
  _globals['_BATCHBUYGOODSRSP']._serialized_start=64
  _globals['_BATCHBUYGOODSRSP']._serialized_end=190
# @@protoc_insertion_point(module_scope)
