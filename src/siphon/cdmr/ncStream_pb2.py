# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ncStream.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0encStream.proto\"\xe4\x01\n\tAttribute\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1d\n\x04type\x18\x02 \x01(\x0e\x32\x0f.Attribute.Type\x12\x0b\n\x03len\x18\x03 \x01(\r\x12\x0c\n\x04\x64\x61ta\x18\x04 \x01(\x0c\x12\r\n\x05sdata\x18\x05 \x03(\t\x12\x10\n\x08unsigned\x18\x06 \x01(\x08\x12\x1b\n\x08\x64\x61taType\x18\x07 \x01(\x0e\x32\t.DataType\"Q\n\x04Type\x12\n\n\x06STRING\x10\x00\x12\x08\n\x04\x42YTE\x10\x01\x12\t\n\x05SHORT\x10\x02\x12\x07\n\x03INT\x10\x03\x12\x08\n\x04LONG\x10\x04\x12\t\n\x05\x46LOAT\x10\x05\x12\n\n\x06\x44OUBLE\x10\x06\"a\n\tDimension\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06length\x18\x02 \x01(\x04\x12\x13\n\x0bisUnlimited\x18\x03 \x01(\x08\x12\x0e\n\x06isVlen\x18\x04 \x01(\x08\x12\x11\n\tisPrivate\x18\x05 \x01(\x08\"\x9c\x01\n\x08Variable\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1b\n\x08\x64\x61taType\x18\x02 \x01(\x0e\x32\t.DataType\x12\x19\n\x05shape\x18\x03 \x03(\x0b\x32\n.Dimension\x12\x18\n\x04\x61tts\x18\x04 \x03(\x0b\x32\n.Attribute\x12\x10\n\x08unsigned\x18\x05 \x01(\x08\x12\x0c\n\x04\x64\x61ta\x18\x06 \x01(\x0c\x12\x10\n\x08\x65numType\x18\x07 \x01(\t\"\xa1\x01\n\tStructure\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1b\n\x08\x64\x61taType\x18\x02 \x01(\x0e\x32\t.DataType\x12\x19\n\x05shape\x18\x03 \x03(\x0b\x32\n.Dimension\x12\x18\n\x04\x61tts\x18\x04 \x03(\x0b\x32\n.Attribute\x12\x17\n\x04vars\x18\x05 \x03(\x0b\x32\t.Variable\x12\x1b\n\x07structs\x18\x06 \x03(\x0b\x32\n.Structure\"h\n\x0b\x45numTypedef\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\"\n\x03map\x18\x02 \x03(\x0b\x32\x15.EnumTypedef.EnumType\x1a\'\n\x08\x45numType\x12\x0c\n\x04\x63ode\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\t\"\xb8\x01\n\x05Group\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x18\n\x04\x64ims\x18\x02 \x03(\x0b\x32\n.Dimension\x12\x17\n\x04vars\x18\x03 \x03(\x0b\x32\t.Variable\x12\x1b\n\x07structs\x18\x04 \x03(\x0b\x32\n.Structure\x12\x18\n\x04\x61tts\x18\x05 \x03(\x0b\x32\n.Attribute\x12\x16\n\x06groups\x18\x06 \x03(\x0b\x32\x06.Group\x12\x1f\n\tenumTypes\x18\x07 \x03(\x0b\x32\x0c.EnumTypedef\"\\\n\x06Header\x12\x10\n\x08location\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x14\n\x04root\x18\x04 \x01(\x0b\x32\x06.Group\x12\x0f\n\x07version\x18\x05 \x01(\r\"&\n\x05\x45rror\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\r\"4\n\x05Range\x12\r\n\x05start\x18\x01 \x01(\x04\x12\x0c\n\x04size\x18\x02 \x01(\x04\x12\x0e\n\x06stride\x18\x03 \x01(\x04\" \n\x07Section\x12\x15\n\x05range\x18\x01 \x03(\x0b\x32\x06.Range\"\xca\x01\n\x04\x44\x61ta\x12\x0f\n\x07varName\x18\x01 \x01(\t\x12\x1b\n\x08\x64\x61taType\x18\x02 \x01(\x0e\x32\t.DataType\x12\x19\n\x07section\x18\x03 \x01(\x0b\x32\x08.Section\x12\x10\n\x06\x62igend\x18\x04 \x01(\x08H\x00\x12\x0f\n\x07version\x18\x05 \x01(\r\x12\x1b\n\x08\x63ompress\x18\x06 \x01(\x0e\x32\t.Compress\x12\r\n\x05vdata\x18\x07 \x01(\x08\x12\x18\n\x10uncompressedSize\x18\x08 \x01(\rB\x10\n\x0e\x62igend_present\"q\n\rStructureData\x12\x0e\n\x06member\x18\x01 \x03(\r\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\x12\x11\n\theapCount\x18\x03 \x03(\r\x12\r\n\x05sdata\x18\x04 \x03(\t\x12\r\n\x05nrows\x18\x05 \x01(\x04\x12\x11\n\trowLength\x18\x06 \x01(\r\"\x81\x02\n\x07\x44\x61taCol\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1b\n\x08\x64\x61taType\x18\x02 \x01(\x0e\x32\t.DataType\x12\x19\n\x07section\x18\x03 \x01(\x0b\x32\x08.Section\x12\x0e\n\x06\x62igend\x18\x04 \x01(\x08\x12\x0f\n\x07version\x18\x05 \x01(\r\x12\x0e\n\x06isVlen\x18\x07 \x01(\x08\x12\x0e\n\x06nelems\x18\t \x01(\r\x12\x10\n\x08primdata\x18\n \x01(\x0c\x12\x12\n\nstringdata\x18\x0b \x03(\t\x12\r\n\x05vlens\x18\x0c \x03(\r\x12\x12\n\nopaquedata\x18\r \x03(\x0c\x12&\n\nstructdata\x18\x0e \x01(\x0b\x32\x12.ArrayStructureCol\"1\n\x11\x41rrayStructureCol\x12\x1c\n\nmemberData\x18\x01 \x03(\x0b\x32\x08.DataCol\"\x85\x02\n\x07\x44\x61taRow\x12\x10\n\x08\x66ullName\x18\x01 \x01(\t\x12\x1b\n\x08\x64\x61taType\x18\x02 \x01(\x0e\x32\t.DataType\x12\x19\n\x07section\x18\x03 \x01(\x0b\x32\x08.Section\x12\x0e\n\x06\x62igend\x18\x04 \x01(\x08\x12\x0f\n\x07version\x18\x05 \x01(\r\x12\x0e\n\x06isVlen\x18\x07 \x01(\x08\x12\x0e\n\x06nelems\x18\t \x01(\r\x12\x10\n\x08primdata\x18\n \x01(\x0c\x12\x12\n\nstringdata\x18\x0b \x03(\t\x12\r\n\x05vlens\x18\x0c \x03(\r\x12\x12\n\nopaquedata\x18\r \x03(\x0c\x12&\n\nstructdata\x18\x0e \x01(\x0b\x32\x12.ArrayStructureRow\"W\n\x06Member\x12\x11\n\tshortName\x18\x01 \x01(\t\x12\x1b\n\x08\x64\x61taType\x18\x02 \x01(\x0e\x32\t.DataType\x12\r\n\x05shape\x18\x03 \x03(\r\x12\x0e\n\x06isVlen\x18\x04 \x01(\x08\"\xae\x01\n\x11\x41rrayStructureRow\x12\x18\n\x07members\x18\x01 \x03(\x0b\x32\x07.Member\x12\r\n\x05nrows\x18\x05 \x01(\x04\x12\x11\n\trowLength\x18\x06 \x01(\r\x12\x0f\n\x07\x66ixdata\x18\n \x01(\x0c\x12\x12\n\nstringdata\x18\x0b \x03(\t\x12\x10\n\x08\x62ytedata\x18\r \x03(\x0c\x12&\n\nstructdata\x18\x0e \x03(\x0b\x32\x12.ArrayStructureRow*\xd5\x01\n\x08\x44\x61taType\x12\x08\n\x04\x43HAR\x10\x00\x12\x08\n\x04\x42YTE\x10\x01\x12\t\n\x05SHORT\x10\x02\x12\x07\n\x03INT\x10\x03\x12\x08\n\x04LONG\x10\x04\x12\t\n\x05\x46LOAT\x10\x05\x12\n\n\x06\x44OUBLE\x10\x06\x12\n\n\x06STRING\x10\x07\x12\r\n\tSTRUCTURE\x10\x08\x12\x0c\n\x08SEQUENCE\x10\t\x12\t\n\x05\x45NUM1\x10\n\x12\t\n\x05\x45NUM2\x10\x0b\x12\t\n\x05\x45NUM4\x10\x0c\x12\n\n\x06OPAQUE\x10\r\x12\t\n\x05UBYTE\x10\x0e\x12\n\n\x06USHORT\x10\x0f\x12\x08\n\x04UINT\x10\x10\x12\t\n\x05ULONG\x10\x11*!\n\x08\x43ompress\x12\x08\n\x04NONE\x10\x00\x12\x0b\n\x07\x44\x45\x46LATE\x10\x01\x42 \n\x0fucar.nc2.streamB\rNcStreamProtob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ncStream_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\017ucar.nc2.streamB\rNcStreamProto'
  _DATATYPE._serialized_start=2348
  _DATATYPE._serialized_end=2561
  _COMPRESS._serialized_start=2563
  _COMPRESS._serialized_end=2596
  _ATTRIBUTE._serialized_start=19
  _ATTRIBUTE._serialized_end=247
  _ATTRIBUTE_TYPE._serialized_start=166
  _ATTRIBUTE_TYPE._serialized_end=247
  _DIMENSION._serialized_start=249
  _DIMENSION._serialized_end=346
  _VARIABLE._serialized_start=349
  _VARIABLE._serialized_end=505
  _STRUCTURE._serialized_start=508
  _STRUCTURE._serialized_end=669
  _ENUMTYPEDEF._serialized_start=671
  _ENUMTYPEDEF._serialized_end=775
  _ENUMTYPEDEF_ENUMTYPE._serialized_start=736
  _ENUMTYPEDEF_ENUMTYPE._serialized_end=775
  _GROUP._serialized_start=778
  _GROUP._serialized_end=962
  _HEADER._serialized_start=964
  _HEADER._serialized_end=1056
  _ERROR._serialized_start=1058
  _ERROR._serialized_end=1096
  _RANGE._serialized_start=1098
  _RANGE._serialized_end=1150
  _SECTION._serialized_start=1152
  _SECTION._serialized_end=1184
  _DATA._serialized_start=1187
  _DATA._serialized_end=1389
  _STRUCTUREDATA._serialized_start=1391
  _STRUCTUREDATA._serialized_end=1504
  _DATACOL._serialized_start=1507
  _DATACOL._serialized_end=1764
  _ARRAYSTRUCTURECOL._serialized_start=1766
  _ARRAYSTRUCTURECOL._serialized_end=1815
  _DATAROW._serialized_start=1818
  _DATAROW._serialized_end=2079
  _MEMBER._serialized_start=2081
  _MEMBER._serialized_end=2168
  _ARRAYSTRUCTUREROW._serialized_start=2171
  _ARRAYSTRUCTUREROW._serialized_end=2345
# @@protoc_insertion_point(module_scope)
