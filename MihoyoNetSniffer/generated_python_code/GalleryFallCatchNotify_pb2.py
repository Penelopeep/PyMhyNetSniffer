# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: GalleryFallCatchNotify.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cGalleryFallCatchNotify.proto\"\x80\x02\n\x16GalleryFallCatchNotify\x12\x11\n\ttime_cost\x18\r \x01(\r\x12\x11\n\tcur_score\x18\x06 \x01(\r\x12\x11\n\tadd_score\x18\x01 \x01(\r\x12L\n\x14\x62\x61ll_catch_count_map\x18\x04 \x03(\x0b\x32..GalleryFallCatchNotify.BallCatchCountMapEntry\x12\x12\n\ngallery_id\x18\x0b \x01(\r\x12\x11\n\tis_ground\x18\x0c \x01(\x08\x1a\x38\n\x16\x42\x61llCatchCountMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x42\x13\n\x11layla.sleep.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'GalleryFallCatchNotify_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\021layla.sleep.proto'
  _GALLERYFALLCATCHNOTIFY_BALLCATCHCOUNTMAPENTRY._options = None
  _GALLERYFALLCATCHNOTIFY_BALLCATCHCOUNTMAPENTRY._serialized_options = b'8\001'
  _globals['_GALLERYFALLCATCHNOTIFY']._serialized_start=33
  _globals['_GALLERYFALLCATCHNOTIFY']._serialized_end=289
  _globals['_GALLERYFALLCATCHNOTIFY_BALLCATCHCOUNTMAPENTRY']._serialized_start=233
  _globals['_GALLERYFALLCATCHNOTIFY_BALLCATCHCOUNTMAPENTRY']._serialized_end=289
# @@protoc_insertion_point(module_scope)
