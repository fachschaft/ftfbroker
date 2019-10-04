# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from ftfbroker.protobuf.common.metaData_pb2 import (
    MetaDataV1 as ftfbroker___protobuf___common___metaData_pb2___MetaDataV1,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Optional as typing___Optional,
    overload as typing___overload,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int


class RocketchatMensa(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def meta_v1(self) -> ftfbroker___protobuf___common___metaData_pb2___MetaDataV1: ...

    @property
    def payload_v1(self) -> RocketchatMensaV1: ...

    def __init__(self,
        *,
        meta_v1 : typing___Optional[ftfbroker___protobuf___common___metaData_pb2___MetaDataV1] = None,
        payload_v1 : typing___Optional[RocketchatMensaV1] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: builtin___bytes) -> RocketchatMensa: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"meta",u"meta_v1",u"payload",u"payload_v1"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"meta",u"meta_v1",u"payload",u"payload_v1"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"meta",b"meta",u"meta_v1",b"meta_v1",u"payload",b"payload",u"payload_v1",b"payload_v1"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"meta",b"meta",u"meta_v1",b"meta_v1",u"payload",b"payload",u"payload_v1",b"payload_v1"]) -> None: ...
    @typing___overload
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"meta",b"meta"]) -> typing_extensions___Literal["meta_v1"]: ...
    @typing___overload
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"payload",b"payload"]) -> typing_extensions___Literal["payload_v1"]: ...

class RocketchatMensaV1(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    def __init__(self,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: builtin___bytes) -> RocketchatMensaV1: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
