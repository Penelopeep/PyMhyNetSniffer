# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: SocialDetail.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import Birthday_pb2 as Birthday__pb2
import FriendEnterHomeOption_pb2 as FriendEnterHomeOption__pb2
import FriendOnlineState_pb2 as FriendOnlineState__pb2
import ProfilePicture_pb2 as ProfilePicture__pb2
import SocialShowAvatarInfo_pb2 as SocialShowAvatarInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12SocialDetail.proto\x1a\x0e\x42irthday.proto\x1a\x1b\x46riendEnterHomeOption.proto\x1a\x17\x46riendOnlineState.proto\x1a\x14ProfilePicture.proto\x1a\x1aSocialShowAvatarInfo.proto\"\xc1\x05\n\x0cSocialDetail\x12\x0b\n\x03uid\x18\x01 \x01(\r\x12\x10\n\x08nickname\x18\x02 \x01(\t\x12\r\n\x05level\x18\x03 \x01(\r\x12\x11\n\tavatar_id\x18\x04 \x01(\r\x12\x11\n\tsignature\x18\x05 \x01(\t\x12\x1b\n\x08\x62irthday\x18\x06 \x01(\x0b\x32\t.Birthday\x12\x13\n\x0bworld_level\x18\x07 \x01(\r\x12\x15\n\rreserved_list\x18\x08 \x03(\r\x12(\n\x0conline_state\x18\t \x01(\x0e\x32\x12.FriendOnlineState\x12\r\n\x05param\x18\n \x01(\r\x12\x11\n\tis_friend\x18\x0b \x01(\x08\x12\x1c\n\x14is_mp_mode_available\x18\x0c \x01(\x08\x12\x11\n\tonline_id\x18\r \x01(\t\x12\x14\n\x0cname_card_id\x18\x0e \x01(\r\x12\x17\n\x0fis_in_blacklist\x18\x0f \x01(\x08\x12\x1a\n\x12is_chat_no_disturb\x18\x10 \x01(\x08\x12\x13\n\x0bremark_name\x18\x11 \x01(\t\x12\x1e\n\x16\x66inish_achievement_num\x18\x12 \x01(\r\x12\x19\n\x11tower_floor_index\x18\x13 \x01(\r\x12\x19\n\x11tower_level_index\x18\x14 \x01(\r\x12\x16\n\x0eis_show_avatar\x18\x15 \x01(\x08\x12\x34\n\x15show_avatar_info_list\x18\x16 \x03(\x0b\x32\x15.SocialShowAvatarInfo\x12\x1e\n\x16show_name_card_id_list\x18\x17 \x03(\r\x12\x38\n\x18\x66riend_enter_home_option\x18\x18 \x01(\x0e\x32\x16.FriendEnterHomeOption\x12(\n\x0fprofile_picture\x18\x19 \x01(\x0b\x32\x0f.ProfilePicture\x12\x0f\n\x07ip_code\x18\x1a \x01(\tB\x13\n\x11layla.sleep.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'SocialDetail_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\021layla.sleep.proto'
  _globals['_SOCIALDETAIL']._serialized_start=143
  _globals['_SOCIALDETAIL']._serialized_end=848
# @@protoc_insertion_point(module_scope)
