from __future__ import annotations

from typing import TYPE_CHECKING

from attr import define


if TYPE_CHECKING:
    from typing import Sequence
    from crescent.internal.meta_struct import MetaStruct
    from crescent.internal.app_command import AppCommandMeta

__all__: Sequence[str] = (
    "Group",
    "SubGroup",
)


@define
class Group:
    name: str

    def sub_group(self, name: str) -> SubGroup:
        return SubGroup(
            name,
            self.name
        )

    def __call__(self, meta: MetaStruct[AppCommandMeta]) -> MetaStruct[AppCommandMeta]:
        meta.metadata.group = self.name
        return meta


@define
class SubGroup:
    name: str
    parent: str

    def __call__(self, meta: MetaStruct[AppCommandMeta]) -> MetaStruct[AppCommandMeta]:
        meta.metadata.group = self.parent
        meta.metadata.sub_group = self.name
        return meta