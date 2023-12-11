from typing import Dict, List, Optional

from libdoc2testbench.pk_generator import PKGenerator
from libdoc2testbench.project_dump_model.itb_project_export import (
    Datatype,
    EquivalenceClass,
    Ref,
    Representative,
    Representatives,
)
from libdoc2testbench.project_dump_model.model_api import (
    create_equivalence_class,
    create_representative,
)
from libdoc2testbench.uid_generator import UidGenerator


class DatatypeStorage:
    def __init__(
        self,
        pk_generator: PKGenerator,
        uid_generator: UidGenerator,
    ) -> None:
        self._datatypes: Dict[str, Datatype] = {}
        self.pk_generator = pk_generator
        self.uid_generator = uid_generator

    def add_datatype(self, name: str, datatype: Datatype) -> None:
        self._datatypes[name] = datatype

    def get_datatypes(self) -> List[Datatype]:
        return dict(sorted(self._datatypes.items())).values()

    def get_datatype(self, name: str):
        return self._datatypes.get(name)

    def get_equivalence_class(
        self, datatype_name: str, name: str, create_eqc=True
    ) -> EquivalenceClass:
        datatype = self._datatypes.get(datatype_name)
        eqc = next(
            filter(lambda eq: eq.name == name, datatype.equivalence_classes.equivalence_class),
            None,
        )
        if not eqc and create_eqc:
            try:
                ordering = int(datatype.equivalence_classes.equivalence_class[-1].ordering) + 1024
            except:
                ordering = 0
            eqc = create_equivalence_class(
                pk=self.pk_generator.get_pk(),
                name=name,
                ordering=str(ordering),
                default_representative_ref=Ref(pk="-1"),
                representatives=Representatives(representative=[]),
            )
            datatype.equivalence_classes.equivalence_class.append(eqc)
        return eqc

    def _get_ec_representatives(self, ec: EquivalenceClass) -> List[Representative]:
        if not ec.representatives or not ec.representatives.representative:
            return []
        return ec.representatives.representative

    def add_equivalence_class_members(
        self, datatype_name: str, equivalence_class_name: str, members: List[str]
    ) -> None:
        equivalence_class = self.get_equivalence_class(datatype_name, equivalence_class_name)
        existing_representatives = [
            repr.name for repr in self._get_ec_representatives(equivalence_class)
        ]
        for member in members:
            if member in existing_representatives:
                continue
            try:
                ordering = int(equivalence_class.representatives.representative[-1]) + 1024
            except:
                ordering = 0
            equivalence_class.representatives.representative.append(
                create_representative(
                    pk=self.pk_generator.get_pk(), name=str(member), ordering=str(ordering)
                )
            )

    def get_representative(
        self, datatype_name: str, representative: str
    ) -> Optional[Representative]:
        datatype = self._datatypes.get(datatype_name)
        for eqc in datatype.equivalence_classes.equivalence_class:
            representatives = self._get_ec_representatives(eqc)
            filtered_representative = next(
                filter(lambda rpr: rpr.name == representative, representatives), None
            )
            if filtered_representative:
                return filtered_representative
        return None
