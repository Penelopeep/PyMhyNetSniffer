# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: FriendBrief.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import FriendOnlineState_pb2 as FriendOnlineState__pb2
import FriendEnterHomeOption_pb2 as FriendEnterHomeOption__pb2
import ProfilePicture_pb2 as ProfilePicture__pb2
import PlatformType_pb2 as PlatformType__pb2
import SocialShowAvatarInfo_pb2 as SocialShowAvatarInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x46riendBrief.proto\x1a\x17\x46riendOnlineState.proto\x1a\x1b\x46riendEnterHomeOption.proto\x1a\x14ProfilePicture.proto\x1a\x12PlatformType.proto\x1a\x1aSocialShowAvatarInfo.proto\"\xc0\x04\n\x0b\x46riendBrief\x12\x0b\n\x03uid\x18\x01 \x01(\r\x12\x10\n\x08nickname\x18\x02 \x01(\t\x12\r\n\x05level\x18\x03 \x01(\r\x12\x10\n\x08\x61vatarId\x18\x04 \x01(\r\x12\x12\n\nworldLevel\x18\x05 \x01(\r\x12\x11\n\tsignature\x18\x06 \x01(\t\x12\'\n\x0bonlineState\x18\x07 \x01(\x0e\x32\x12.FriendOnlineState\x12\r\n\x05param\x18\x08 \x01(\r\x12\x19\n\x11isMpModeAvailable\x18\n \x01(\x08\x12\x10\n\x08onlineId\x18\x0b \x01(\t\x12\x16\n\x0elastActiveTime\x18\x0c \x01(\r\x12\x12\n\nnameCardId\x18\r \x01(\r\x12\x13\n\x0bmpPlayerNum\x18\x0e \x01(\r\x12\x17\n\x0fisChatNoDisturb\x18\x0f \x01(\x08\x12\x14\n\x0c\x63hatSequence\x18\x10 \x01(\r\x12\x12\n\nremarkName\x18\x11 \x01(\t\x12\x31\n\x12showAvatarInfoList\x18\x16 \x03(\x0b\x32\x15.SocialShowAvatarInfo\x12\x35\n\x15\x66riendEnterHomeOption\x18\x17 \x01(\x0e\x32\x16.FriendEnterHomeOption\x12\'\n\x0eprofilePicture\x18\x18 \x01(\x0b\x32\x0f.ProfilePicture\x12\x14\n\x0cisGameSource\x18\x19 \x01(\x08\x12\x13\n\x0bisPsnSource\x18\x1a \x01(\x08\x12#\n\x0cplatformType\x18\x1b \x01(\x0e\x32\r.PlatformTypeB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'FriendBrief_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _globals['_FRIENDBRIEF']._serialized_start=146
  _globals['_FRIENDBRIEF']._serialized_end=722
# @@protoc_insertion_point(module_scope)
