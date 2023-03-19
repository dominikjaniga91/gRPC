# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: epam/ping-pong.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
  name='epam/ping-pong.proto',
  package='epam',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x16\x63lient/ping-pong.proto\x12\x06\x63lient\"\x1e\n\x0bPingRequest\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x1f\n\x0cPongResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2G\n\x0ePingPongServer\x12\x35\n\x08pingPong\x12\x13.epam.PingRequest\x1a\x14.epam.PongResponseb\x06proto3'
)

_PINGREQUEST = _descriptor.Descriptor(
  name='PingRequest',
  full_name='epam.PingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='epam.PingRequest.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=28,
  serialized_end=54,
)

_PONGRESPONSE = _descriptor.Descriptor(
  name='PongResponse',
  full_name='epam.PongResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='epam.PongResponse.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=56,
  serialized_end=108,
)

DESCRIPTOR.message_types_by_name['PingRequest'] = _PINGREQUEST
DESCRIPTOR.message_types_by_name['PongResponse'] = _PONGRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PingRequest = _reflection.GeneratedProtocolMessageType('PingRequest', (_message.Message,), {
  'DESCRIPTOR' : _PINGREQUEST,
  '__module__' : 'epam.ping_pong_pb2'
  # @@protoc_insertion_point(class_scope:unary.Message)
})
_sym_db.RegisterMessage(PingRequest)

PongResponse = _reflection.GeneratedProtocolMessageType('MessageResponse', (_message.Message,), {
  'DESCRIPTOR' : _PONGRESPONSE,
  '__module__' : 'epam.ping_pong_pb2'
  # @@protoc_insertion_point(class_scope:unary.MessageResponse)
})
_sym_db.RegisterMessage(PongResponse)