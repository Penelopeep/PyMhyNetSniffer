# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: GadgetInteractRsp.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import InteractType_pb2 as InteractType__pb2
import InterOpType_pb2 as InterOpType__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17GadgetInteractRsp.proto\x1a\x12InteractType.proto\x1a\x11InterOpType.proto\"\x91\x01\n\x11GadgetInteractRsp\x12#\n\x0cinteractType\x18\x03 \x01(\x0e\x32\r.InteractType\x12\x0f\n\x07retcode\x18\x0c \x01(\x05\x12\x10\n\x08gadgetId\x18\n \x01(\r\x12\x16\n\x0egadgetEntityId\x18\x02 \x01(\r\x12\x1c\n\x06opType\x18\x06 \x01(\x0e\x32\x0c.InterOpTypeB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'GadgetInteractRsp_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _globals['_GADGETINTERACTRSP']._serialized_start=67
  _globals['_GADGETINTERACTRSP']._serialized_end=212
# @@protoc_insertion_point(module_scope)
