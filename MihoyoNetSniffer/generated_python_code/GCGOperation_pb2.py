# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: GCGOperation.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import GCGOperationAttack_pb2 as GCGOperationAttack__pb2
import GCGOperationOnStageSelect_pb2 as GCGOperationOnStageSelect__pb2
import GCGOperationPass_pb2 as GCGOperationPass__pb2
import GCGOperationPlayCard_pb2 as GCGOperationPlayCard__pb2
import GCGOperationReboot_pb2 as GCGOperationReboot__pb2
import GCGOperationRedraw_pb2 as GCGOperationRedraw__pb2
import GCGOperationReroll_pb2 as GCGOperationReroll__pb2
import GCGOperationSurrender_pb2 as GCGOperationSurrender__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12GCGOperation.proto\x1a\x18GCGOperationAttack.proto\x1a\x1fGCGOperationOnStageSelect.proto\x1a\x16GCGOperationPass.proto\x1a\x1aGCGOperationPlayCard.proto\x1a\x18GCGOperationReboot.proto\x1a\x18GCGOperationRedraw.proto\x1a\x18GCGOperationReroll.proto\x1a\x1bGCGOperationSurrender.proto\"\xfb\x02\n\x0cGCGOperation\x12(\n\top_redraw\x18\x03 \x01(\x0b\x32\x13.GCGOperationRedrawH\x00\x12\x38\n\x12op_select_on_stage\x18\t \x01(\x0b\x32\x1a.GCGOperationOnStageSelectH\x00\x12(\n\top_reroll\x18\x04 \x01(\x0b\x32\x13.GCGOperationRerollH\x00\x12(\n\top_attack\x18\x07 \x01(\x0b\x32\x13.GCGOperationAttackH\x00\x12$\n\x07op_pass\x18\x06 \x01(\x0b\x32\x11.GCGOperationPassH\x00\x12-\n\x0cop_play_card\x18\x0f \x01(\x0b\x32\x15.GCGOperationPlayCardH\x00\x12(\n\top_reboot\x18\x05 \x01(\x0b\x32\x13.GCGOperationRebootH\x00\x12.\n\x0cop_surrender\x18\n \x01(\x0b\x32\x16.GCGOperationSurrenderH\x00\x42\x04\n\x02opb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'GCGOperation_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GCGOPERATION._serialized_start=241
  _GCGOPERATION._serialized_end=620
# @@protoc_insertion_point(module_scope)
