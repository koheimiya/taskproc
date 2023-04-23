from __future__ import annotations
from typing import Protocol, TypeVar, NewType
from datetime import datetime


Json = NewType('Json', str)
T = TypeVar('T')
D = TypeVar('D')


class DBProtocol(Protocol[T, D]):
    def save(self, key: Json, obj: T) -> datetime: ...
    def load(self, key: Json) -> T: ...
    def load_timestamp(self, key: Json) -> datetime: ...
    def add_dep(self, key: Json, dep: D) -> None: ...
    def load_deps(self, key: Json) -> list[D]: ...
    def reset_deps(self, key: Json) -> None: ...
    def delete(self, key: Json) -> None: ...
    def clear(self) -> None: ...
    def list_keys(self) -> list[str]: ...