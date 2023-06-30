# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: efficient_paper.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='efficient_paper.proto',
  package='efficient_paper',
  syntax='proto2',
  serialized_pb=_b('\n\x15\x65\x66\x66icient_paper.proto\x12\x0f\x65\x66\x66icient_paper\"\xa7\x01\n\tPaperInfo\x12%\n\x05paper\x18\x01 \x01(\x0b\x32\x16.efficient_paper.Paper\x12)\n\x03pub\x18\x02 \x01(\x0b\x32\x1c.efficient_paper.Publication\x12#\n\x04\x63ode\x18\x03 \x01(\x0b\x32\x15.efficient_paper.Code\x12#\n\x04note\x18\x04 \x01(\x0b\x32\x15.efficient_paper.Note\"k\n\x05Paper\x12\x1a\n\x05title\x18\x01 \x01(\t:\x0bpaper title\x12\x12\n\x04\x61\x62\x62r\x18\x02 \x01(\t:\x04\x61\x62\x62r\x12\x0b\n\x03url\x18\x03 \x01(\t\x12\x0f\n\x07\x61uthors\x18\x04 \x03(\t\x12\x14\n\x0cinstitutions\x18\x05 \x03(\t\"*\n\x0bPublication\x12\r\n\x05where\x18\x01 \x01(\t\x12\x0c\n\x04year\x18\x02 \x01(\x05\"*\n\x04\x43ode\x12\x15\n\x04type\x18\x01 \x01(\t:\x07Pytorch\x12\x0b\n\x03url\x18\x02 \x01(\t\"\x13\n\x04Note\x12\x0b\n\x03url\x18\x01 \x01(\t')
)




_PAPERINFO = _descriptor.Descriptor(
  name='PaperInfo',
  full_name='efficient_paper.PaperInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='paper', full_name='efficient_paper.PaperInfo.paper', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pub', full_name='efficient_paper.PaperInfo.pub', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='code', full_name='efficient_paper.PaperInfo.code', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='note', full_name='efficient_paper.PaperInfo.note', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=43,
  serialized_end=210,
)


_PAPER = _descriptor.Descriptor(
  name='Paper',
  full_name='efficient_paper.Paper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='efficient_paper.Paper.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("paper title").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='abbr', full_name='efficient_paper.Paper.abbr', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("abbr").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='url', full_name='efficient_paper.Paper.url', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='authors', full_name='efficient_paper.Paper.authors', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='institutions', full_name='efficient_paper.Paper.institutions', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=212,
  serialized_end=319,
)


_PUBLICATION = _descriptor.Descriptor(
  name='Publication',
  full_name='efficient_paper.Publication',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='where', full_name='efficient_paper.Publication.where', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='year', full_name='efficient_paper.Publication.year', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=321,
  serialized_end=363,
)


_CODE = _descriptor.Descriptor(
  name='Code',
  full_name='efficient_paper.Code',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='efficient_paper.Code.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("Pytorch").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='url', full_name='efficient_paper.Code.url', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=365,
  serialized_end=407,
)


_NOTE = _descriptor.Descriptor(
  name='Note',
  full_name='efficient_paper.Note',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='efficient_paper.Note.url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=409,
  serialized_end=428,
)

_PAPERINFO.fields_by_name['paper'].message_type = _PAPER
_PAPERINFO.fields_by_name['pub'].message_type = _PUBLICATION
_PAPERINFO.fields_by_name['code'].message_type = _CODE
_PAPERINFO.fields_by_name['note'].message_type = _NOTE
DESCRIPTOR.message_types_by_name['PaperInfo'] = _PAPERINFO
DESCRIPTOR.message_types_by_name['Paper'] = _PAPER
DESCRIPTOR.message_types_by_name['Publication'] = _PUBLICATION
DESCRIPTOR.message_types_by_name['Code'] = _CODE
DESCRIPTOR.message_types_by_name['Note'] = _NOTE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PaperInfo = _reflection.GeneratedProtocolMessageType('PaperInfo', (_message.Message,), dict(
  DESCRIPTOR = _PAPERINFO,
  __module__ = 'efficient_paper_pb2'
  # @@protoc_insertion_point(class_scope:efficient_paper.PaperInfo)
  ))
_sym_db.RegisterMessage(PaperInfo)

Paper = _reflection.GeneratedProtocolMessageType('Paper', (_message.Message,), dict(
  DESCRIPTOR = _PAPER,
  __module__ = 'efficient_paper_pb2'
  # @@protoc_insertion_point(class_scope:efficient_paper.Paper)
  ))
_sym_db.RegisterMessage(Paper)

Publication = _reflection.GeneratedProtocolMessageType('Publication', (_message.Message,), dict(
  DESCRIPTOR = _PUBLICATION,
  __module__ = 'efficient_paper_pb2'
  # @@protoc_insertion_point(class_scope:efficient_paper.Publication)
  ))
_sym_db.RegisterMessage(Publication)

Code = _reflection.GeneratedProtocolMessageType('Code', (_message.Message,), dict(
  DESCRIPTOR = _CODE,
  __module__ = 'efficient_paper_pb2'
  # @@protoc_insertion_point(class_scope:efficient_paper.Code)
  ))
_sym_db.RegisterMessage(Code)

Note = _reflection.GeneratedProtocolMessageType('Note', (_message.Message,), dict(
  DESCRIPTOR = _NOTE,
  __module__ = 'efficient_paper_pb2'
  # @@protoc_insertion_point(class_scope:efficient_paper.Note)
  ))
_sym_db.RegisterMessage(Note)


# @@protoc_insertion_point(module_scope)
