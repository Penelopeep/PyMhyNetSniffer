# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: DungeonCandidateTeamInfoNotify.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import DungeonCandidateTeamAvatar_pb2 as DungeonCandidateTeamAvatar__pb2
import DungeonCandidateTeamPlayerState_pb2 as DungeonCandidateTeamPlayerState__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$DungeonCandidateTeamInfoNotify.proto\x1a DungeonCandidateTeamAvatar.proto\x1a%DungeonCandidateTeamPlayerState.proto\"\xbc\x02\n\x1e\x44ungeonCandidateTeamInfoNotify\x12\x30\n\x0b\x61vatar_list\x18\x06 \x03(\x0b\x32\x1b.DungeonCandidateTeamAvatar\x12\x18\n\x10ready_player_uid\x18\x0e \x03(\r\x12\x12\n\nmatch_type\x18\x0b \x01(\r\x12M\n\x10player_state_map\x18\x05 \x03(\x0b\x32\x33.DungeonCandidateTeamInfoNotify.PlayerStateMapEntry\x12\x12\n\ndungeon_id\x18\x03 \x01(\r\x1aW\n\x13PlayerStateMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12/\n\x05value\x18\x02 \x01(\x0e\x32 .DungeonCandidateTeamPlayerState:\x02\x38\x01\x42\x13\n\x11layla.sleep.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'DungeonCandidateTeamInfoNotify_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\021layla.sleep.proto'
  _DUNGEONCANDIDATETEAMINFONOTIFY_PLAYERSTATEMAPENTRY._options = None
  _DUNGEONCANDIDATETEAMINFONOTIFY_PLAYERSTATEMAPENTRY._serialized_options = b'8\001'
  _globals['_DUNGEONCANDIDATETEAMINFONOTIFY']._serialized_start=114
  _globals['_DUNGEONCANDIDATETEAMINFONOTIFY']._serialized_end=430
  _globals['_DUNGEONCANDIDATETEAMINFONOTIFY_PLAYERSTATEMAPENTRY']._serialized_start=343
  _globals['_DUNGEONCANDIDATETEAMINFONOTIFY_PLAYERSTATEMAPENTRY']._serialized_end=430
# @@protoc_insertion_point(module_scope)
