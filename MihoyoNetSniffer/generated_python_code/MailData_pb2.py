# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: MailData.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import MailCollectState_pb2 as MailCollectState__pb2
import MailItem_pb2 as MailItem__pb2
import MailTextContent_pb2 as MailTextContent__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eMailData.proto\x1a\x16MailCollectState.proto\x1a\x0eMailItem.proto\x1a\x15MailTextContent.proto\"\xa2\x02\n\x08MailData\x12\x0f\n\x07mail_id\x18\x01 \x01(\r\x12+\n\x11mail_text_content\x18\x04 \x01(\x0b\x32\x10.MailTextContent\x12\x1c\n\titem_list\x18\x07 \x03(\x0b\x32\t.MailItem\x12\x11\n\tsend_time\x18\x08 \x01(\r\x12\x13\n\x0b\x65xpire_time\x18\t \x01(\r\x12\x12\n\nimportance\x18\n \x01(\r\x12\x0f\n\x07is_read\x18\x0b \x01(\x08\x12\x19\n\x11is_attachment_got\x18\x0c \x01(\x08\x12\x11\n\tconfig_id\x18\r \x01(\r\x12\x15\n\rargument_list\x18\x0e \x03(\t\x12(\n\rcollect_state\x18\x0f \x01(\x0e\x32\x11.MailCollectStateB\x13\n\x11layla.sleep.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'MailData_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\021layla.sleep.proto'
  _globals['_MAILDATA']._serialized_start=82
  _globals['_MAILDATA']._serialized_end=372
# @@protoc_insertion_point(module_scope)
