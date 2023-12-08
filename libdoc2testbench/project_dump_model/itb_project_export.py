from enum import Enum
from typing import List, Optional

import attr


class ActivityStatus(Enum):
    """
    :cvar VALUE_11: ACTSTATUS_NOTPLANNED
    :cvar VALUE_12: ACTSTATUS_PLANNED
    :cvar VALUE_13: ACTSTATUS_ASSIGNED
    :cvar VALUE_14: ACTSTATUS_RUNNING
    :cvar VALUE_15: ACTSTATUS_CANCELED
    :cvar VALUE_16: ACTSTATUS_PERFORMED
    :cvar VALUE_23: ACTSTATUS_SKIPPED
    """

    ACTSTATUS_NOTPLANNED = 11
    ACTSTATUS_PLANNED = 12
    ACTSTATUS_ASSIGNED = 13
    ACTSTATUS_RUNNING = 14
    ACTSTATUS_CANCELED = 15
    ACTSTATUS_PERFORMED = 16
    ACTSTATUS_SKIPPED = 23


@attr.s(kw_only=True)
class AdvancedContent:
    class Meta:
        name = "advancedContent"

    external_identifier: str = attr.ib(
        metadata={
            "name": "externalIdentifier",
            "type": "Element",
            "required": True,
        }
    )
    content: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    content_type: str = attr.ib(
        metadata={
            "name": "contentType",
            "type": "Attribute",
            "required": True,
        }
    )


class AutomationStatus(Enum):
    """
    :cvar VALUE_6: AUTSTATUS_NOTPLANNED
    :cvar VALUE_7: AUTSTATUS_PLANNED
    :cvar VALUE_8: AUTSTATUS_INPROGRESS
    :cvar VALUE_9: AUTSTATUS_INREVIEW
    :cvar VALUE_10: AUTSTATUS_RELEASED
    """

    AUTSTATUS_NOTPLANNED = 6
    AUTSTATUS_PLANNED = 7
    AUTSTATUS_INPROGRESS = 8
    AUTSTATUS_INREVIEW = 9
    AUTSTATUS_RELEASED = 10


@attr.s(kw_only=True)
class BaselineDetails:
    class Meta:
        name = "baseline-details"

    name: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    project: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    last_update: str = attr.ib(
        metadata={
            "name": "lastUpdate",
            "type": "Element",
            "required": True,
        }
    )
    type_value: str = attr.ib(
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        }
    )
    repository_id: str = attr.ib(
        metadata={
            "name": "repository-id",
            "type": "Element",
            "required": True,
        }
    )


class BinaryDigit(Enum):
    """
    :cvar VALUE_0: FLOW
    :cvar VALUE_1: CHECK
    """

    FLOW = 0
    CHECK = 1


class CallParameterType(Enum):
    PARAMETER = "parameter"
    INSTANCES_ARRAY = "instances-array"
    REPRESENTATIVE = "representative"


@attr.s(kw_only=True)
class CalledLibrary:
    class Meta:
        name = "calledLibrary"

    pk: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    baseline_pk: str = attr.ib(
        metadata={
            "name": "baselinePK",
            "type": "Element",
            "required": True,
        }
    )


@attr.s(kw_only=True)
class ClassMapping:
    class Meta:
        name = "class-mapping"

    class_value: List[str] = attr.ib(
        factory=list,
        metadata={
            "name": "class",
            "type": "Element",
        },
    )


class DefaultCallTypeName(Enum):
    FLOW = "Flow"
    CHECK = "Check"


class DefaultValueType(Enum):
    EQUIVALENCE_CLASS = "equivalence-class"
    REPRESENTATIVE = "representative"
    INSTANCES_ARRAY = "instances-array"


class DefinitionType(Enum):
    """For interaction always 0.

    Test case interactions can have the values 2 or 3

    :cvar VALUE_0: DETAILED
    :cvar VALUE_2: ARRAY
    :cvar VALUE_3: ATOMIC
    """

    DETAILED = 0
    ARRAY = 2
    ATOMIC = 3


@attr.s(kw_only=True)
class ErrorIdReferences:
    class Meta:
        name = "error-id-references"

    error_id_reference: List[str] = attr.ib(
        factory=list,
        metadata={
            "name": "error-id-reference",
            "type": "Element",
        },
    )


@attr.s(kw_only=True)
class ExecLogfile:
    class Meta:
        name = "exec-logfile"

    filename: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    type_value: str = attr.ib(
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        }
    )
    file_pk: str = attr.ib(
        metadata={
            "name": "file-pk",
            "type": "Element",
            "required": True,
        }
    )
    result_file_pk: str = attr.ib(
        metadata={
            "name": "result-file-pk",
            "type": "Element",
            "required": True,
        }
    )
    charset: Optional[str] = attr.ib(
        default=None,
        metadata={
            "type": "Element",
        },
    )


class ExecutionStatus(Enum):
    """
    :cvar VALUE_21: EXEC_STATUS_NOTBLOCKED
    :cvar VALUE_22: EXEC_STATUS_BLOCKED
    """

    EXEC_STATUS_NOTBLOCKED = 21
    EXEC_STATUS_BLOCKED = 22


@attr.s(kw_only=True)
class ForeignLibraryLabel:
    class Meta:
        name = "foreignLibraryLabel"

    pk: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    name: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    library_pk: str = attr.ib(
        metadata={
            "name": "library-pk",
            "type": "Element",
            "required": True,
        }
    )
    project: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    owner: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@attr.s(kw_only=True)
class IdenticalVersionDatatype:
    class Meta:
        name = "identical-version-datatype"

    work_pk: str = attr.ib(
        metadata={
            "name": "workPK",
            "type": "Attribute",
            "required": True,
        }
    )
    vers_pk: str = attr.ib(
        metadata={
            "name": "versPK",
            "type": "Attribute",
            "required": True,
        }
    )
    is_changed_def_type: bool = attr.ib(
        metadata={
            "name": "isChangedDefType",
            "type": "Attribute",
            "required": True,
        }
    )


@attr.s(kw_only=True)
class IdenticalVersionMetawordParam:
    class Meta:
        name = "identical-version-metaword-param"

    work_param_pk: str = attr.ib(
        metadata={
            "name": "workParamPK",
            "type": "Attribute",
            "required": True,
        }
    )
    vers_param_pk: str = attr.ib(
        metadata={
            "name": "versParamPK",
            "type": "Attribute",
            "required": True,
        }
    )


class InteractionCallType(Enum):
    """
    :cvar VALUE_0: FLOW
    :cvar VALUE_1: CHECK
    """

    FLOW = 0
    CHECK = 1


class InteractionCallPhase(Enum):
    SETUP = "Setup"
    TEST_STEP = "TestStep"
    TEARDOWN = "Teardown"


@attr.s(kw_only=True)
class Keyword:
    class Meta:
        name = "keyword"

    pk: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    name: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


class KindOfDataType(Enum):
    REGULAR = "regular"
    REFERENCE = "reference"
    GLOBAL = "global"
    ACCEPTING_GLOBAL = "accepting-global"


@attr.s(kw_only=True)
class Label:
    """
    :ivar pk:
    :ivar name:
    :ivar owner: the user login
    """

    class Meta:
        name = "label"

    pk: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    name: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    owner: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@attr.s(kw_only=True)
class LibraryInformation:
    class Meta:
        name = "libraryInformation"

    library_pk: str = attr.ib(
        metadata={
            "name": "libraryPK",
            "type": "Element",
            "required": True,
        }
    )
    foreign_library_tov_pk: Optional[str] = attr.ib(
        default=None,
        metadata={
            "name": "foreignLibraryTovPK",
            "type": "Element",
        },
    )
    foreign_library_pk: Optional[str] = attr.ib(
        default=None,
        metadata={
            "name": "foreignLibraryPK",
            "type": "Element",
        },
    )
    source_project: Optional[str] = attr.ib(
        default=None,
        metadata={
            "name": "sourceProject",
            "type": "Element",
        },
    )
    source_test_object_version: Optional[str] = attr.ib(
        default=None,
        metadata={
            "name": "sourceTestObjectVersion",
            "type": "Element",
        },
    )


@attr.s(kw_only=True)
class LibraryLabel:
    class Meta:
        name = "libraryLabel"

    pk: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    name: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    library_pk: str = attr.ib(
        metadata={
            "name": "library-pk",
            "type": "Element",
            "required": True,
        }
    )
    owner: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@attr.s(kw_only=True)
class Message:
    class Meta:
        name = "message"

    object_value: str = attr.ib(
        metadata={
            "name": "object",
            "type": "Element",
            "required": True,
        }
    )
    pk: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    message: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


class MustField(Enum):
    """
    :cvar VALUE_0: FALSE
    :cvar VALUE_1: TRUE
    """

    FALSE = 0
    TRUE = 1


@attr.s(kw_only=True)
class OldVersions:
    class Meta:
        name = "old-versions"

    version: List["Version"] = attr.ib(
        factory=list,
        metadata={
            "type": "Element",
        },
    )


@attr.s(kw_only=True)
class Placeholder:
    class Meta:
        name = "placeholder"

    pk: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    name: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    description: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@attr.s(kw_only=True)
class PriorityMapping:
    class Meta:
        name = "priority-mapping"

    priority: List[str] = attr.ib(
        factory=list,
        metadata={
            "type": "Element",
        },
    )


class ProjectRole(Enum):
    TAUTEMA_TEST_MANAGER = "tautema-test-manager"
    TAUTEMA_TEST_DESIGNER = "tautema-test-designer"
    TAUTEMA_TEST_IMPLEMENTER = "tautema-test-implementer"
    TAUTEMA_TESTER = "tautema-tester"
    TEST_INTELLIGENCE = "test-intelligence"


class ProjectStatus(Enum):
    PLANNED = "planned"
    ACTIVE = "active"
    FINISHED = "finished"
    CLOSED = "closed"


@attr.s(kw_only=True)
class Ref:
    class Meta:
        name = "ref"

    pk: str = attr.ib(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


class ReferenceKind(Enum):
    """
    :cvar VALUE_1: REFERENCE
    :cvar VALUE_2: LINK
    :cvar VALUE_3: ATTACHMENT
    """

    REFERENCE = 1
    LINK = 2
    ATTACHMENT = 3


@attr.s(kw_only=True)
class ReferencedUserNames:
    """
    :ivar user_name: user login
    :ivar user_pk: number (long)
    """

    class Meta:
        name = "referenced-user-names"

    user_name: List[str] = attr.ib(
        factory=list,
        metadata={
            "name": "user-name",
            "type": "Element",
            "sequence": 1,
        },
    )
    user_pk: List[str] = attr.ib(
        factory=list,
        metadata={
            "name": "user-pk",
            "type": "Element",
            "sequence": 1,
        },
    )


class RepresentativeType(Enum):
    TEXT = "text"
    PLACEHOLDER = "placeholder"
    FILEREFERENCE = "filereference"
    ATTACHMENT = "attachment"
    HYPERLINK = "hyperlink"


class RequirementNodeType(Enum):
    """
    :cvar VALUE_0: REQUIREMENT
    :cvar VALUE_1: REQUIREMENT_FOLDER
    """

    REQUIREMENT = 0
    REQUIREMENT_FOLDER = 1


@attr.s(kw_only=True)
class RequirementRepository:
    class Meta:
        name = "requirement-repository"

    pk: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    name: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    login: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    password: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@attr.s(kw_only=True)
class Settings:
    class Meta:
        name = "settings"

    overwrite_exec_responsible: bool = attr.ib(
        metadata={
            "name": "overwrite-exec-responsible",
            "type": "Element",
            "required": True,
        }
    )
    optional_checkin: bool = attr.ib(
        metadata={
            "name": "optional-checkin",
            "type": "Element",
            "required": True,
        }
    )
    hide_exec_auto_checkin: Optional[bool] = attr.ib(
        default=None,
        metadata={
            "name": "hide-exec-auto-checkin",
            "type": "Element",
        },
    )
    extended_interactions_content: Optional[bool] = attr.ib(
        default=None,
        metadata={
            "name": "extended-interactions-content",
            "type": "Element",
        },
    )
    libraries_state: Optional[bool] = attr.ib(
        default=None,
        metadata={
            "name": "libraries-state",
            "type": "Element",
        },
    )
    global_datatypes_state: Optional[bool] = attr.ib(
        default=None,
        metadata={
            "name": "global-datatypes-state",
            "type": "Element",
        },
    )
    filter_sync_interval: int = attr.ib(
        metadata={
            "name": "filter-sync-interval",
            "type": "Element",
            "required": True,
        }
    )
    ignore_not_edited: bool = attr.ib(
        metadata={
            "name": "ignore-not-edited",
            "type": "Element",
            "required": True,
        }
    )
    ignore_not_planned: bool = attr.ib(
        metadata={
            "name": "ignore-not-planned",
            "type": "Element",
            "required": True,
        }
    )
    designers_may_manage_baselines: bool = attr.ib(
        metadata={
            "name": "designers-may-manage-baselines",
            "type": "Element",
            "required": True,
        }
    )
    designers_may_import_baselines: bool = attr.ib(
        metadata={
            "name": "designers-may-import-baselines",
            "type": "Element",
            "required": True,
        }
    )
    only_admins_manage_udfs: bool = attr.ib(
        metadata={
            "name": "only-admins-manage-udfs",
            "type": "Element",
            "required": True,
        }
    )
    variants_management_enabled: bool = attr.ib(
        metadata={
            "name": "variants-management-enabled",
            "type": "Element",
            "required": True,
        }
    )


class SpecificationStatus(Enum):
    """
    :cvar VALUE_1: SPECSTATUS_NOTPLANNED
    :cvar VALUE_2: SPECSTATUS_PLANNED
    :cvar VALUE_3: SPECSTATUS_INPROGRESS
    :cvar VALUE_4: SPECSTATUS_INREVIEW
    :cvar VALUE_5: SPECSTATUS_RELEASED
    """

    SPECSTATUS_NOTPLANNED = 1
    SPECSTATUS_PLANNED = 2
    SPECSTATUS_INPROGRESS = 3
    SPECSTATUS_INREVIEW = 4
    SPECSTATUS_RELEASED = 5


@attr.s(kw_only=True)
class StatusMapping:
    class Meta:
        name = "status-mapping"

    status: List[str] = attr.ib(
        factory=list,
        metadata={
            "type": "Element",
        },
    )


class TsePriority(Enum):
    """
    :cvar VALUE_0: NO_PRIORITY
    :cvar VALUE_1: LOW
    :cvar VALUE_2: MEDIUM
    :cvar VALUE_3: HIGH
    """

    NO_PRIORITY = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3


class UdfDefinitionType(Enum):
    """
    :cvar VALUE_0: SINGLE_LINE_TEXT
    :cvar VALUE_1: CHECK_BOX
    :cvar VALUE_2: MULTI_LINE_TEXT
    :cvar VALUE_3: CHECK_LIST
    :cvar VALUE_4: ITEMS_LIST
    """

    SINGLE_LINE_TEXT = 0
    CHECK_BOX = 1
    MULTI_LINE_TEXT = 2
    CHECK_LIST = 3
    ITEMS_LIST = 4


@attr.s(kw_only=True)
class UdfValue:
    class Meta:
        name = "udf-value"

    name: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    value: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


class UdfSyncOption(Enum):
    """
    :cvar VALUE_0: ITB_IS_SYNC_MASTER
    :cvar VALUE_1: DMS_IS_SYNC_MASTER
    :cvar VALUE_2: SYNC_MASTER_DEPENDS_ON_DEFECT_TIME_STAMPS
    """

    ITB_IS_SYNC_MASTER = 0
    DMS_IS_SYNC_MASTER = 1
    SYNC_MASTER_DEPENDS_ON_DEFECT_TIME_STAMPS = 2


class UdfType(Enum):
    """
    :cvar VALUE_0: TEXTFIELD
    :cvar VALUE_1: LIST_OF_VALUES
    :cvar VALUE_2: CHECK_BOX
    """

    TEXTFIELD = 0
    LIST_OF_VALUES = 1
    CHECK_BOX = 2


@attr.s(kw_only=True)
class Undefined:
    class Meta:
        name = "undefined"


class UseType(Enum):
    """
    :cvar VALUE_0: CALL_BY_REFERENCE
    :cvar VALUE_1: CALL_BY_VALUE
    """

    CALL_BY_REFERENCE = 0
    CALL_BY_VALUE = 1


@attr.s(kw_only=True)
class UserMapping:
    class Meta:
        name = "user-mapping"

    itblogin: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    dmlogin: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@attr.s(kw_only=True)
class VariantsDefinition:
    class Meta:
        name = "variantsDefinition"

    pk: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    name: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    status: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    description: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    html_description: str = attr.ib(
        metadata={
            "name": "html-description",
            "type": "Element",
            "required": True,
        }
    )


class VerdictStatus(Enum):
    """
    :cvar VALUE_17: VERDICT_STATUS_UNDEFINED
    :cvar VALUE_18: VERDICT_STATUS_TOVERIFY
    :cvar VALUE_19: VERDICT_STATUS_FAIL
    :cvar VALUE_20: VERDICT_STATUS_PASS
    """

    VERDICT_STATUS_UNDEFINED = 17
    VERDICT_STATUS_TOVERIFY = 18
    VERDICT_STATUS_FAIL = 19
    VERDICT_STATUS_PASS = 20


@attr.s(kw_only=True)
class DefectUserDefinedField:
    pk: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    name: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    ordering: int = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    must_field: MustField = attr.ib(
        metadata={
            "name": "mustField",
            "type": "Element",
            "required": True,
        }
    )
    udf_sync_option: UdfSyncOption = attr.ib(
        metadata={
            "name": "udfSyncOption",
            "type": "Element",
            "required": True,
        }
    )
    udf_type: UdfType = attr.ib(
        metadata={
            "name": "udfType",
            "type": "Element",
            "required": True,
        }
    )
    value: List[str] = attr.ib(
        factory=list,
        metadata={
            "type": "Element",
        },
    )


@attr.s(kw_only=True)
class UserDefinedFieldDefinition:
    """
    :ivar pk:
    :ivar name:
    :ivar ordering:
    :ivar must_field:
    :ivar udf_scopes: comma separated scopes of the UDF. Possible
        values: TestThemesInSpecification, TestCaseSetsInSpecification,
        TestCasesInSpecification, TestThemesInExecution,
        TestCaseSetsInExecution, TestCasesInExecution
    :ivar udf_type:
    :ivar value:
    """

    pk: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    name: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    ordering: int = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    must_field: MustField = attr.ib(
        metadata={
            "name": "mustField",
            "type": "Element",
            "required": True,
        }
    )
    udf_scopes: str = attr.ib(
        metadata={
            "name": "udfScopes",
            "type": "Element",
            "required": True,
        }
    )
    udf_type: UdfType = attr.ib(
        metadata={
            "name": "udfType",
            "type": "Element",
            "required": True,
        }
    )
    value: List[str] = attr.ib(
        factory=list,
        metadata={
            "type": "Element",
        },
    )


@attr.s(kw_only=True)
class Automation:
    class Meta:
        name = "automation"

    details: "AutomationDetails" = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    script_editor: str = attr.ib(
        metadata={
            "name": "script-editor",
            "type": "Element",
            "required": True,
        }
    )
    script_template: str = attr.ib(
        metadata={
            "name": "script-template",
            "type": "Element",
            "required": True,
        }
    )
    old_versions: Optional[OldVersions] = attr.ib(
        default=None,
        metadata={
            "name": "old-versions",
            "type": "Element",
        },
    )


@attr.s(kw_only=True)
class CalledLibraries:
    class Meta:
        name = "called-libraries"

    called_library: List[CalledLibrary] = attr.ib(
        factory=list,
        metadata={
            "name": "calledLibrary",
            "type": "Element",
        },
    )


@attr.s(kw_only=True)
class ConditionRef:
    class Meta:
        name = "condition-ref"

    condition_ref: Ref = attr.ib(
        metadata={
            "name": "condition-ref",
            "type": "Element",
            "required": True,
        }
    )


@attr.s(kw_only=True)
class DefaultCallType:
    class Meta:
        name = "default-call-type"

    name: DefaultCallTypeName = attr.ib(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    value: BinaryDigit = attr.ib(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@attr.s(kw_only=True)
class DefaultValue:
    class Meta:
        name = "default-value"

    type_value: str = attr.ib(
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        }
    )
    equivalence_class_ref: Optional[Ref] = attr.ib(
        default=None,
        metadata={
            "name": "equivalence-class-ref",
            "type": "Element",
        },
    )
    representative_ref: Optional[Ref] = attr.ib(
        default=None,
        metadata={
            "name": "representative-ref",
            "type": "Element",
        },
    )
    instances_array_ref: Optional[Ref] = attr.ib(
        default=None,
        metadata={
            "name": "instances-array-ref",
            "type": "Element",
        },
    )
    type_attribute: DefaultValueType = attr.ib(
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        }
    )


@attr.s(kw_only=True)
class ErrorIdRefs:
    class Meta:
        name = "error-id-refs"

    error_id_ref: List[Ref] = attr.ib(
        factory=list,
        metadata={
            "name": "error-id-ref",
            "type": "Element",
        },
    )


@attr.s(kw_only=True)
class Errors:
    class Meta:
        name = "errors"

    error: List[Message] = attr.ib(
        factory=list,
        metadata={
            "type": "Element",
        },
    )


@attr.s(kw_only=True)
class ExecLogfiles:
    class Meta:
        name = "exec-logfiles"

    exec_logfile: List[ExecLogfile] = attr.ib(
        factory=list,
        metadata={
            "name": "exec-logfile",
            "type": "Element",
        },
    )


@attr.s(kw_only=True)
class Field:
    """
    :ivar sequence_pk:
    :ivar name:
    :ivar datatype_ref: pk of the data type, -1 by generic parameters
    :ivar definition_type:
    """

    class Meta:
        name = "field"

    sequence_pk: str = attr.ib(
        metadata={
            "name": "sequence-pk",
            "type": "Element",
            "required": True,
        }
    )
    name: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    datatype_ref: Ref = attr.ib(
        metadata={
            "name": "datatype-ref",
            "type": "Element",
            "required": True,
        }
    )
    definition_type: DefinitionType = attr.ib(
        metadata={
            "name": "definition-type",
            "type": "Element",
            "required": True,
        }
    )


@attr.s(kw_only=True)
class ForeignLibraryLabelGroup:
    class Meta:
        name = "foreignLibraryLabelGroup"

    label: List[ForeignLibraryLabel] = attr.ib(
        factory=list,
        metadata={
            "type": "Element",
        },
    )


@attr.s(kw_only=True)
class IdenticalVersionDatatypeMapping:
    class Meta:
        name = "identical-version-datatype-mapping"

    identical_version_datatype: List[IdenticalVersionDatatype] = attr.ib(
        factory=list,
        metadata={
            "name": "identical-version-datatype",
            "type": "Element",
        },
    )


@attr.s(kw_only=True)
class IdenticalVersionMetaword:
    class Meta:
        name = "identical-version-metaword"

    identical_version_metaword_param: List[IdenticalVersionMetawordParam] = attr.ib(
        factory=list,
        metadata={
            "name": "identical-version-metaword-param",
            "type": "Element",
        },
    )
    work_pk: str = attr.ib(
        metadata={
            "name": "workPK",
            "type": "Attribute",
            "required": True,
        }
    )
    vers_pk: str = attr.ib(
        metadata={
            "name": "versPK",
            "type": "Attribute",
            "required": True,
        }
    )


@attr.s(kw_only=True)
class Keywords:
    class Meta:
        name = "keywords"

    content: List[object] = attr.ib(
        factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "keyword-ref",
                    "type": Ref,
                },
                {
                    "name": "named-keyword",
                    "type": str,
                },
                {
                    "name": "named-variants-marker",
                    "type": str,
                },
            ),
        },
    )


@attr.s(kw_only=True)
class KeywordsDefinition:
    class Meta:
        name = "keywords-definition"

    keyword: List[Keyword] = attr.ib(
        factory=list,
        metadata={
            "type": "Element",
        },
    )


@attr.s(kw_only=True)
class LabelsRef:
    class Meta:
        name = "labels-ref"

    label_ref: List[Ref] = attr.ib(
        factory=list,
        metadata={
            "name": "label-ref",
            "type": "Element",
        },
    )


@attr.s(kw_only=True)
class LibraryLabelGroup:
    class Meta:
        name = "libraryLabelGroup"

    label: List[LibraryLabel] = attr.ib(
        factory=list,
        metadata={
            "type": "Element",
        },
    )


@attr.s(kw_only=True)
class Marker:
    class Meta:
        name = "marker"

    marker_ref: List[Ref] = attr.ib(
        factory=list,
        metadata={
            "name": "marker-ref",
            "type": "Element",
        },
    )
    named_variants_marker: List[str] = attr.ib(
        factory=list,
        metadata={
            "name": "named-variants-marker",
            "type": "Element",
        },
    )


@attr.s(kw_only=True)
class PlaceholderValue:
    class Meta:
        name = "placeholderValue"

    pk: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    placeholder_ref: Ref = attr.ib(
        metadata={
            "name": "placeholder-ref",
            "type": "Element",
            "required": True,
        }
    )
    variants_definition_ref: Ref = attr.ib(
        metadata={
            "name": "variantsDefinition-ref",
            "type": "Element",
            "required": True,
        }
    )
    value: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@attr.s(kw_only=True)
class Placeholders:
    class Meta:
        name = "placeholders"

    placeholder: List[Placeholder] = attr.ib(
        factory=list,
        metadata={
            "type": "Element",
        },
    )


@attr.s(kw_only=True)
class Reference:
    class Meta:
        name = "reference"

    pk: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    filename: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    type_value: ReferenceKind = attr.ib(
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        }
    )
    version: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    attachment_pk: Optional[str] = attr.ib(
        default=None,
        metadata={
            "name": "attachment-pk",
            "type": "Element",
        },
    )
    attachment_path: Optional[str] = attr.ib(
        default=None,
        metadata={
            "name": "attachment-path",
            "type": "Element",
        },
    )
    attachment_filename: Optional[str] = attr.ib(
        default=None,
        metadata={
            "name": "attachment-filename",
            "type": "Element",
        },
    )
    attachment_lastedited: Optional[str] = attr.ib(
        default=None,
        metadata={
            "name": "attachment-lastedited",
            "type": "Element",
        },
    )
    attachment_lasteditor: Optional[str] = attr.ib(
        default=None,
        metadata={
            "name": "attachment-lasteditor",
            "type": "Element",
        },
    )
    attachment_file_pk: Optional[str] = attr.ib(
        default=None,
        metadata={
            "name": "attachment-file-pk",
            "type": "Element",
        },
    )
    old_versions: Optional[OldVersions] = attr.ib(
        default=None,
        metadata={
            "name": "old-versions",
            "type": "Element",
        },
    )


@attr.s(kw_only=True)
class RequirementProject:
    class Meta:
        name = "requirement-project"

    content: List[object] = attr.ib(
        factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "pk",
                    "type": str,
                },
                {
                    "name": "name",
                    "type": str,
                },
                {
                    "name": "repository-ref",
                    "type": Ref,
                },
            ),
        },
    )


@attr.s(kw_only=True)
class RequirementRefs:
    class Meta:
        name = "requirement-refs"

    requirement_ref: List[Ref] = attr.ib(
        factory=list,
        metadata={
            "name": "requirement-ref",
            "type": "Element",
        },
    )


@attr.s(kw_only=True)
class RequirementRepositories:
    class Meta:
        name = "requirement-repositories"

    requirement_repository: List[RequirementRepository] = attr.ib(
        factory=list,
        metadata={
            "name": "requirement-repository",
            "type": "Element",
        },
    )


@attr.s(kw_only=True)
class Roles:
    class Meta:
        name = "roles"

    role: List[ProjectRole] = attr.ib(
        factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 5,
        },
    )
    read_only: Optional[bool] = attr.ib(
        default=None,
        metadata={
            "name": "read-only",
            "type": "Attribute",
        },
    )


@attr.s(kw_only=True)
class SequencePath:
    class Meta:
        name = "sequence-path"

    sequence_ref: List[Ref] = attr.ib(
        factory=list,
        metadata={
            "name": "sequence-ref",
            "type": "Element",
        },
    )


@attr.s(kw_only=True)
class Testcycle:
    class Meta:
        name = "testcycle"

    pk: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    name: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    created_time: str = attr.ib(
        metadata={
            "name": "createdTime",
            "type": "Element",
            "required": True,
        }
    )
    startdate: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    enddate: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    status: ProjectStatus = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    visible_for_testers: Optional[bool] = attr.ib(
        default=None,
        metadata={
            "name": "visibleForTesters",
            "type": "Element",
        },
    )
    description: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    html_description: str = attr.ib(
        metadata={
            "name": "html-description",
            "type": "Element",
            "required": True,
        }
    )
    testing_intelligence: str = attr.ib(
        metadata={
            "name": "testingIntelligence",
            "type": "Element",
            "required": True,
        }
    )


@attr.s(kw_only=True)
class UdfDefinition:
    class Meta:
        name = "udf-definition"

    name: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    type_value: UdfDefinitionType = attr.ib(
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        }
    )
    repository_id: str = attr.ib(
        metadata={
            "name": "repository-id",
            "type": "Element",
            "required": True,
        }
    )


@attr.s(kw_only=True)
class Udfs:
    class Meta:
        name = "udfs"

    udf: List[UdfValue] = attr.ib(
        factory=list,
        metadata={
            "type": "Element",
        },
    )


@attr.s(kw_only=True)
class UserMappings:
    class Meta:
        name = "user-mappings"

    user_mapping: List[UserMapping] = attr.ib(
        factory=list,
        metadata={
            "name": "user-mapping",
            "type": "Element",
        },
    )


@attr.s(kw_only=True)
class UserDefinedField:
    class Meta:
        name = "userDefinedField"

    udfpk: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    value: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    udf_name: str = attr.ib(
        metadata={
            "name": "udfName",
            "type": "Element",
            "required": True,
        }
    )
    udf_type: UdfType = attr.ib(
        metadata={
            "name": "udfType",
            "type": "Element",
            "required": True,
        }
    )
    ordering: int = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@attr.s(kw_only=True)
class Value:
    class Meta:
        name = "value"

    default_value: Optional[bool] = attr.ib(
        default=None,
        metadata={
            "name": "default-value",
            "type": "Attribute",
        },
    )
    content: List[object] = attr.ib(
        factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "undefined",
                    "type": Undefined,
                },
                {
                    "name": "type",
                    "type": str,
                },
                {
                    "name": "ia-param-ref",
                    "type": Ref,
                },
                {
                    "name": "equivalence-class-ref",
                    "type": Ref,
                },
                {
                    "name": "instances-array-ref",
                    "type": Ref,
                },
                {
                    "name": "representative-ref",
                    "type": Ref,
                },
                {
                    "name": "dataType-ref",
                    "type": Ref,
                },
                {
                    "name": "representative",
                    "type": str,
                },
            ),
        },
    )


@attr.s(kw_only=True)
class VariantsDefinitions:
    class Meta:
        name = "variantsDefinitions"

    variants_definition: List[VariantsDefinition] = attr.ib(
        factory=list,
        metadata={
            "name": "variantsDefinition",
            "type": "Element",
        },
    )


@attr.s(kw_only=True)
class VariantsMarker:
    class Meta:
        name = "variantsMarker"

    pk: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    variants_definition_ref: Ref = attr.ib(
        metadata={
            "name": "variantsDefinition-ref",
            "type": "Element",
            "required": True,
        }
    )


@attr.s(kw_only=True)
class VisibilityGroup:
    class Meta:
        name = "visibilityGroup"

    label: List[Label] = attr.ib(
        factory=list,
        metadata={
            "type": "Element",
        },
    )


@attr.s(kw_only=True)
class Warnings:
    class Meta:
        name = "warnings"

    warning: List[Message] = attr.ib(
        factory=list,
        metadata={
            "type": "Element",
        },
    )


@attr.s(kw_only=True)
class DefectUserDefinedFields:
    defect_user_defined_field: List[DefectUserDefinedField] = attr.ib(
        factory=list,
        metadata={
            "name": "DefectUserDefinedField",
            "type": "Element",
        },
    )


@attr.s(kw_only=True)
class UserDefinedFieldsDefinition:
    user_defined_field: List[UserDefinedFieldDefinition] = attr.ib(
        factory=list,
        metadata={
            "name": "UserDefinedField",
            "type": "Element",
        },
    )


@attr.s(kw_only=True)
class CallParameter:
    class Meta:
        name = "call-parameter"

    pk: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    parameter_datatype_ref: Ref = attr.ib(
        metadata={
            "name": "parameter-datatype-ref",
            "type": "Element",
            "required": True,
        }
    )
    parent_parameter_ref: Optional[object] = attr.ib(
        default=None,
        metadata={
            "name": "parent-parameter-ref",
            "type": "Element",
        },
    )
    sequence_path: Optional[SequencePath] = attr.ib(
        default=None,
        metadata={
            "name": "sequence-path",
            "type": "Element",
        },
    )
    instances_array_ref: Optional[Ref] = attr.ib(
        default=None,
        metadata={
            "name": "instances-array-ref",
            "type": "Element",
        },
    )
    representative_ref: Optional[Ref] = attr.ib(
        default=None,
        metadata={
            "name": "representative-ref",
            "type": "Element",
        },
    )
    type_value: CallParameterType = attr.ib(
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        }
    )
    default_value: Optional[bool] = attr.ib(
        default=None,
        metadata={
            "name": "default-value",
            "type": "Attribute",
        },
    )


@attr.s(kw_only=True)
class Conditions:
    class Meta:
        name = "conditions"

    condition: List[ConditionRef] = attr.ib(
        factory=list,
        metadata={
            "type": "Element",
        },
    )


@attr.s(kw_only=True)
class DmSettings:
    """
    :ivar pk:
    :ivar system:
    :ivar project:
    :ivar readlogin:
    :ivar firstsync: a date
    :ivar syncinterval: in minutes
    :ivar statusattribute:
    :ivar statussyncoption:
    :ivar statusdefaultvalue:
    :ivar priorityattribute:
    :ivar prioritysyncoption:
    :ivar prioritydefaultvalue:
    :ivar classattribute:
    :ivar classsyncoption:
    :ivar classdefaultvalue:
    :ivar status_mapping:
    :ivar priority_mapping:
    :ivar class_mapping:
    :ivar user_mappings:
    """

    class Meta:
        name = "dm-settings"

    pk: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    system: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    project: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    readlogin: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    firstsync: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    syncinterval: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    statusattribute: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    statussyncoption: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    statusdefaultvalue: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    priorityattribute: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    prioritysyncoption: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    prioritydefaultvalue: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    classattribute: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    classsyncoption: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    classdefaultvalue: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    status_mapping: StatusMapping = attr.ib(
        metadata={
            "name": "status-mapping",
            "type": "Element",
            "required": True,
        }
    )
    priority_mapping: PriorityMapping = attr.ib(
        metadata={
            "name": "priority-mapping",
            "type": "Element",
            "required": True,
        }
    )
    class_mapping: ClassMapping = attr.ib(
        metadata={
            "name": "class-mapping",
            "type": "Element",
            "required": True,
        }
    )
    user_mappings: UserMappings = attr.ib(
        metadata={
            "name": "user-mappings",
            "type": "Element",
            "required": True,
        }
    )


@attr.s(kw_only=True)
class ErrorId:
    """
    :ivar pk:
    :ivar name:
    :ivar title:
    :ivar description:
    :ivar status:
    :ivar priority:
    :ivar classification:
    :ivar tester:
    :ivar last_edited:
    :ivar created: a date
    :ivar used_in_cycles:
    :ivar last_editor: user login (or null)
    :ivar dm_system:
    :ivar dm_project:
    :ivar identical_version_pk:
    :ivar error_id_references:
    :ivar udfs:
    :ivar old_versions:
    """

    class Meta:
        name = "error-id"

    pk: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    name: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    title: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    description: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    status: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    priority: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    classification: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    tester: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    last_edited: str = attr.ib(
        metadata={
            "name": "lastEdited",
            "type": "Element",
            "required": True,
        }
    )
    created: List[str] = attr.ib(
        factory=list,
        metadata={
            "type": "Element",
        },
    )
    used_in_cycles: List[str] = attr.ib(
        factory=list,
        metadata={
            "name": "used-in-cycles",
            "type": "Element",
        },
    )
    last_editor: str = attr.ib(
        metadata={
            "name": "lastEditor",
            "type": "Element",
            "required": True,
        }
    )
    dm_system: str = attr.ib(
        metadata={
            "name": "dmSystem",
            "type": "Element",
            "required": True,
        }
    )
    dm_project: str = attr.ib(
        metadata={
            "name": "dmProject",
            "type": "Element",
            "required": True,
        }
    )
    identical_version_pk: str = attr.ib(
        metadata={
            "name": "identicalVersionPK",
            "type": "Element",
            "required": True,
        }
    )
    error_id_references: ErrorIdReferences = attr.ib(
        metadata={
            "name": "error-id-references",
            "type": "Element",
            "required": True,
        }
    )
    udfs: List[Udfs] = attr.ib(
        factory=list,
        metadata={
            "type": "Element",
        },
    )
    old_versions: Optional[OldVersions] = attr.ib(
        default=None,
        metadata={
            "name": "old-versions",
            "type": "Element",
        },
    )


@attr.s(kw_only=True)
class Fields:
    class Meta:
        name = "fields"

    field_value: List[Field] = attr.ib(
        factory=list,
        metadata={
            "name": "field",
            "type": "Element",
        },
    )


@attr.s(kw_only=True)
class IdenticalVersionMetawordMapping:
    class Meta:
        name = "identical-version-metaword-mapping"

    identical_version_metaword: List[IdenticalVersionMetaword] = attr.ib(
        factory=list,
        metadata={
            "name": "identical-version-metaword",
            "type": "Element",
        },
    )


@attr.s(kw_only=True)
class Labels:
    class Meta:
        name = "labels"

    public: VisibilityGroup = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    private: VisibilityGroup = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@attr.s(kw_only=True)
class LibraryLabels:
    class Meta:
        name = "libraryLabels"

    local: LibraryLabelGroup = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    foreign: ForeignLibraryLabelGroup = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@attr.s(kw_only=True)
class Parameter:
    """
    :ivar pk:
    :ivar name:
    :ivar datatype_ref: pk of the data type, -1 by generic parameters
    :ivar definition_type:
    :ivar use_type:
    :ivar default_value:
    :ivar signature_uid:
    """

    class Meta:
        name = "parameter"

    pk: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    name: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    datatype_ref: Ref = attr.ib(
        metadata={
            "name": "datatype-ref",
            "type": "Element",
            "required": True,
        }
    )
    definition_type: DefinitionType = attr.ib(
        metadata={
            "name": "definition-type",
            "type": "Element",
            "required": True,
        }
    )
    use_type: UseType = attr.ib(
        metadata={
            "name": "use-type",
            "type": "Element",
            "required": True,
        }
    )
    default_value: Optional[DefaultValue] = attr.ib(
        default=None,
        metadata={
            "name": "default-value",
            "type": "Element",
        },
    )
    signature_uid: Optional[str] = attr.ib(
        default=None,
        metadata={
            "name": "signature-uid",
            "type": "Element",
        },
    )


@attr.s(kw_only=True)
class PlaceholderValues:
    class Meta:
        name = "placeholderValues"

    placeholder_value: List[PlaceholderValue] = attr.ib(
        factory=list,
        metadata={
            "name": "placeholderValue",
            "type": "Element",
        },
    )


@attr.s(kw_only=True)
class ProjectUser:
    class Meta:
        name = "project-user"

    content: List[object] = attr.ib(
        factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "name",
                    "type": str,
                },
                {
                    "name": "roles",
                    "type": Roles,
                },
            ),
        },
    )


@attr.s(kw_only=True)
class References:
    class Meta:
        name = "references"

    reference: List[Reference] = attr.ib(
        factory=list,
        metadata={
            "type": "Element",
        },
    )
    reference_ref: List[Ref] = attr.ib(
        factory=list,
        metadata={
            "name": "reference-ref",
            "type": "Element",
        },
    )
    reference_name: List[str] = attr.ib(
        factory=list,
        metadata={
            "name": "reference-name",
            "type": "Element",
        },
    )
    type_value: List[str] = attr.ib(
        factory=list,
        metadata={
            "name": "type",
            "type": "Element",
        },
    )


@attr.s(kw_only=True)
class RequirementProjects:
    class Meta:
        name = "requirement-projects"

    project: List[RequirementProject] = attr.ib(
        factory=list,
        metadata={
            "type": "Element",
        },
    )


@attr.s(kw_only=True)
class RequirementUdfs:
    class Meta:
        name = "requirement-udfs"

    udf: List[UdfDefinition] = attr.ib(
        factory=list,
        metadata={
            "type": "Element",
        },
    )


@attr.s(kw_only=True)
class TestElementVersionInfo:
    class Meta:
        name = "test-element-version-info"

    pk: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    name: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    user: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    comment: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    date: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    status: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    type_value: str = attr.ib(
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        }
    )
    labels: LabelsRef = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@attr.s(kw_only=True)
class Testcycles:
    class Meta:
        name = "testcycles"

    testcycle: List[Testcycle] = attr.ib(
        factory=list,
        metadata={
            "type": "Element",
        },
    )


@attr.s(kw_only=True)
class UserDefinedFields:
    class Meta:
        name = "userDefinedFields"

    user_defined_field: List[UserDefinedField] = attr.ib(
        factory=list,
        metadata={
            "name": "userDefinedField",
            "type": "Element",
        },
    )


@attr.s(kw_only=True)
class Values:
    class Meta:
        name = "values"

    value: List[Value] = attr.ib(
        factory=list,
        metadata={
            "type": "Element",
        },
    )


@attr.s(kw_only=True)
class VariantsMarkers:
    class Meta:
        name = "variantsMarkers"

    variants_marker: List[VariantsMarker] = attr.ib(
        factory=list,
        metadata={
            "name": "variantsMarker",
            "type": "Element",
        },
    )


@attr.s(kw_only=True)
class ConditionVersion(TestElementVersionInfo):
    class Meta:
        name = "condition-version"

    element: "Condition" = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@attr.s(kw_only=True)
class DatatypeVersion(TestElementVersionInfo):
    class Meta:
        name = "datatype-version"

    element: "Datatype" = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@attr.s(kw_only=True)
class ErrorIds:
    class Meta:
        name = "error-ids"

    error_id: List[ErrorId] = attr.ib(
        factory=list,
        metadata={
            "name": "error-id",
            "type": "Element",
        },
    )


@attr.s(kw_only=True)
class Instance:
    class Meta:
        name = "instance"

    pk: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    ordering: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    values: Values = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@attr.s(kw_only=True)
class InteractionVersion(TestElementVersionInfo):
    class Meta:
        name = "interaction-version"

    element: "Interaction" = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@attr.s(kw_only=True)
class ParameterCombinationExec:
    class Meta:
        name = "parameter-combination-exec"

    specification_parameter_combination_ref: Ref = attr.ib(
        metadata={
            "name": "specification-parameter-combination-ref",
            "type": "Element",
            "required": True,
        }
    )
    status: ActivityStatus = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    execution_status: ExecutionStatus = attr.ib(
        metadata={
            "name": "execution-status",
            "type": "Element",
            "required": True,
        }
    )
    verdict: VerdictStatus = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    comment: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    html_comment: str = attr.ib(
        metadata={
            "name": "html-comment",
            "type": "Element",
            "required": True,
        }
    )
    ordering: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    uid: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    tester: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    actual_time: str = attr.ib(
        metadata={
            "name": "actual-time",
            "type": "Element",
            "required": True,
        }
    )
    planned_time: str = attr.ib(
        metadata={
            "name": "planned-time",
            "type": "Element",
            "required": True,
        }
    )
    error_ids: ErrorIdRefs = attr.ib(
        metadata={
            "name": "error-ids",
            "type": "Element",
            "required": True,
        }
    )
    keywords: Keywords = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    user_defined_fields: UserDefinedFields = attr.ib(
        metadata={
            "name": "userDefinedFields",
            "type": "Element",
            "required": True,
        }
    )
    values: Values = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    references: References = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@attr.s(kw_only=True)
class ParameterCombinationSpec:
    class Meta:
        name = "parameter-combination-spec"

    pk: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    comment: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    html_comment: str = attr.ib(
        metadata={
            "name": "html-comment",
            "type": "Element",
            "required": True,
        }
    )
    ordering: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    uid: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    keywords: Keywords = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    edited_requirements: RequirementRefs = attr.ib(
        metadata={
            "name": "edited-requirements",
            "type": "Element",
            "required": True,
        }
    )
    non_edited_requirements: RequirementRefs = attr.ib(
        metadata={
            "name": "non-edited-requirements",
            "type": "Element",
            "required": True,
        }
    )
    user_defined_fields: UserDefinedFields = attr.ib(
        metadata={
            "name": "userDefinedFields",
            "type": "Element",
            "required": True,
        }
    )
    values: Values = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@attr.s(kw_only=True)
class ParameterValues:
    class Meta:
        name = "parameter-values"

    call_parameter: List[CallParameter] = attr.ib(
        factory=list,
        metadata={
            "name": "call-parameter",
            "type": "Element",
        },
    )


@attr.s(kw_only=True)
class Parameters:
    class Meta:
        name = "parameters"

    parameter: List[Parameter] = attr.ib(
        factory=list,
        metadata={
            "type": "Element",
        },
    )


@attr.s(kw_only=True)
class ProjectDetails:
    """
    :ivar name:
    :ivar id:
    :ivar testobjectname:
    :ivar state: planned, active, finished, closed
    :ivar customername:
    :ivar customeradress:
    :ivar contactperson:
    :ivar testlab:
    :ivar checklocation:
    :ivar visible_for_testers:
    :ivar startdate:
    :ivar enddate:
    :ivar status:
    :ivar description:
    :ivar html_description:
    :ivar testing_intelligence:
    :ivar created_time:
    :ivar settings:
    :ivar requirement_repositories:
    :ivar requirement_projects:
    :ivar requirement_udfs:
    """

    class Meta:
        name = "project-details"

    name: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    id: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    testobjectname: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    state: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    customername: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    customeradress: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    contactperson: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    testlab: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    checklocation: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    visible_for_testers: Optional[bool] = attr.ib(
        default=None,
        metadata={
            "name": "visibleForTesters",
            "type": "Element",
        },
    )
    startdate: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    enddate: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    status: ProjectStatus = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    description: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    html_description: str = attr.ib(
        metadata={
            "name": "html-description",
            "type": "Element",
            "required": True,
        }
    )
    testing_intelligence: str = attr.ib(
        metadata={
            "name": "testingIntelligence",
            "type": "Element",
            "required": True,
        }
    )
    created_time: str = attr.ib(
        metadata={
            "name": "createdTime",
            "type": "Element",
            "required": True,
        }
    )
    settings: Settings = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    requirement_repositories: RequirementRepositories = attr.ib(
        metadata={
            "name": "requirement-repositories",
            "type": "Element",
            "required": True,
        }
    )
    requirement_projects: RequirementProjects = attr.ib(
        metadata={
            "name": "requirement-projects",
            "type": "Element",
            "required": True,
        }
    )
    requirement_udfs: RequirementUdfs = attr.ib(
        metadata={
            "name": "requirement-udfs",
            "type": "Element",
            "required": True,
        }
    )


@attr.s(kw_only=True)
class Representative:
    class Meta:
        name = "representative"

    pk: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    name: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    ordering: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    type_value: Optional[RepresentativeType] = attr.ib(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
        },
    )
    placeholder_ref: Optional[Ref] = attr.ib(
        default=None,
        metadata={
            "name": "placeholder-ref",
            "type": "Element",
        },
    )
    attachment_pk: Optional[str] = attr.ib(
        default=None,
        metadata={
            "name": "attachment-pk",
            "type": "Element",
        },
    )
    attachment_path: Optional[str] = attr.ib(
        default=None,
        metadata={
            "name": "attachment-path",
            "type": "Element",
        },
    )
    attachment_filename: Optional[str] = attr.ib(
        default=None,
        metadata={
            "name": "attachment-filename",
            "type": "Element",
        },
    )
    attachment_lastedited: Optional[str] = attr.ib(
        default=None,
        metadata={
            "name": "attachment-lastedited",
            "type": "Element",
        },
    )
    attachment_contentpath: Optional[str] = attr.ib(
        default=None,
        metadata={
            "name": "attachment-contentpath",
            "type": "Element",
        },
    )
    attachment_lasteditor: Optional[str] = attr.ib(
        default=None,
        metadata={
            "name": "attachment-lasteditor",
            "type": "Element",
        },
    )
    attachment_file_pk: Optional[str] = attr.ib(
        default=None,
        metadata={
            "name": "attachment-file-pk",
            "type": "Element",
        },
    )
    values: Values = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@attr.s(kw_only=True)
class SubdivisionVersion(TestElementVersionInfo):
    class Meta:
        name = "subdivision-version"

    element: "Subdivision" = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@attr.s(kw_only=True)
class TestElement:
    class Meta:
        name = "test-element"

    version: Optional[TestElementVersionInfo] = attr.ib(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    pk: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    name: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    uid: Optional[str] = attr.ib(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    locker: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    description: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    html_description: Optional[str] = attr.ib(
        default=None,
        metadata={
            "name": "html-description",
            "type": "Element",
        },
    )
    history_pk: str = attr.ib(
        metadata={
            "name": "historyPK",
            "type": "Element",
            "required": True,
        }
    )
    identical_version_pk: str = attr.ib(
        metadata={
            "name": "identicalVersionPK",
            "type": "Element",
            "required": True,
        }
    )
    references: Optional[References] = attr.ib(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    library_pk: Optional[str] = attr.ib(
        default=None,
        metadata={
            "name": "libraryPK",
            "type": "Element",
        },
    )
    parent_uid: Optional[str] = attr.ib(
        default=None,
        metadata={
            "name": "parentUID",
            "type": "Element",
        },
    )


@attr.s(kw_only=True)
class Userroles:
    class Meta:
        name = "userroles"

    user: List[ProjectUser] = attr.ib(
        factory=list,
        metadata={
            "type": "Element",
        },
    )


@attr.s(kw_only=True)
class ConditionVersions:
    class Meta:
        name = "condition-versions"

    version: List[ConditionVersion] = attr.ib(
        factory=list,
        metadata={
            "type": "Element",
        },
    )


@attr.s(kw_only=True)
class DatatypeVersions:
    class Meta:
        name = "datatype-versions"

    version: List[DatatypeVersion] = attr.ib(
        factory=list,
        metadata={
            "type": "Element",
        },
    )


@attr.s(kw_only=True)
class Instances:
    class Meta:
        name = "instances"

    instance: List[Instance] = attr.ib(
        factory=list,
        metadata={
            "type": "Element",
        },
    )


@attr.s(kw_only=True)
class InteractionCall:
    class Meta:
        name = "interaction-call"

    interaction_ref: Ref = attr.ib(
        metadata={
            "name": "interaction-ref",
            "type": "Element",
            "required": True,
        }
    )
    description: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    html_description: str = attr.ib(
        metadata={
            "name": "html-description",
            "type": "Element",
            "required": True,
        }
    )
    comment: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    html_comment: str = attr.ib(
        metadata={
            "name": "html-comment",
            "type": "Element",
            "required": True,
        }
    )
    type_value: InteractionCallType = attr.ib(
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        }
    )
    phase: InteractionCallPhase = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    parameter_values: ParameterValues = attr.ib(
        metadata={
            "name": "parameter-values",
            "type": "Element",
            "required": True,
        }
    )
    marker: Optional[Marker] = attr.ib(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@attr.s(kw_only=True)
class InteractionVersions:
    class Meta:
        name = "interaction-versions"

    version: List[InteractionVersion] = attr.ib(
        factory=list,
        metadata={
            "type": "Element",
        },
    )


@attr.s(kw_only=True)
class ParameterCombinationsExec:
    class Meta:
        name = "parameter-combinations-exec"

    parameter_combination: List[ParameterCombinationExec] = attr.ib(
        factory=list,
        metadata={
            "name": "parameter-combination",
            "type": "Element",
        },
    )


@attr.s(kw_only=True)
class ParameterCombinationsSpec:
    class Meta:
        name = "parameter-combinations-spec"

    parameter_combination: List[ParameterCombinationSpec] = attr.ib(
        factory=list,
        metadata={
            "name": "parameter-combination",
            "type": "Element",
        },
    )


@attr.s(kw_only=True)
class Representatives:
    class Meta:
        name = "representatives"

    representative: List[Representative] = attr.ib(
        factory=list,
        metadata={
            "type": "Element",
        },
    )


@attr.s(kw_only=True)
class SubdivisionVersions:
    class Meta:
        name = "subdivision-versions"

    version: List[SubdivisionVersion] = attr.ib(
        factory=list,
        metadata={
            "type": "Element",
        },
    )


@attr.s(kw_only=True)
class CallSequence:
    class Meta:
        name = "call-sequence"

    interaction_call: List[InteractionCall] = attr.ib(
        factory=list,
        metadata={
            "name": "interaction-call",
            "type": "Element",
        },
    )


@attr.s(kw_only=True)
class Condition(TestElement):
    class Meta:
        name = "condition"

    old_versions: Optional[ConditionVersions] = attr.ib(
        default=None,
        metadata={
            "name": "old-versions",
            "type": "Element",
        },
    )
    type_value: str = attr.ib(
        init=False,
        default="condition",
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )


@attr.s(kw_only=True)
class EquivalenceClass:
    class Meta:
        name = "equivalence-class"

    pk: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    name: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    description: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    ordering: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    default_representative_ref: Ref = attr.ib(
        metadata={
            "name": "default-representative-ref",
            "type": "Element",
            "required": True,
        }
    )
    representatives: Representatives = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@attr.s(kw_only=True)
class Execution:
    class Meta:
        name = "execution"

    testcycle_ref: Ref = attr.ib(
        metadata={
            "name": "testcycle-ref",
            "type": "Element",
            "required": True,
        }
    )
    specification_ref: Ref = attr.ib(
        metadata={
            "name": "specification-ref",
            "type": "Element",
            "required": True,
        }
    )
    details: "ExecutionDetails" = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    execution_status: ExecutionStatus = attr.ib(
        metadata={
            "name": "execution-status",
            "type": "Element",
            "required": True,
        }
    )
    verdict: VerdictStatus = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    planned_time: str = attr.ib(
        metadata={
            "name": "planned-time",
            "type": "Element",
            "required": True,
        }
    )
    actual_time: str = attr.ib(
        metadata={
            "name": "actual-time",
            "type": "Element",
            "required": True,
        }
    )
    script_path: str = attr.ib(
        metadata={
            "name": "script-path",
            "type": "Element",
            "required": True,
        }
    )
    execution_engine: str = attr.ib(
        metadata={
            "name": "execution-engine",
            "type": "Element",
            "required": True,
        }
    )
    protocol_location: str = attr.ib(
        metadata={
            "name": "protocol-location",
            "type": "Element",
            "required": True,
        }
    )
    verdict_evaluator: str = attr.ib(
        metadata={
            "name": "verdict-evaluator",
            "type": "Element",
            "required": True,
        }
    )
    comments: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    html_comments: str = attr.ib(
        metadata={
            "name": "html-comments",
            "type": "Element",
            "required": True,
        }
    )
    keywords: Keywords = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    user_defined_fields: UserDefinedFields = attr.ib(
        metadata={
            "name": "userDefinedFields",
            "type": "Element",
            "required": True,
        }
    )
    exec_logfiles: ExecLogfiles = attr.ib(
        metadata={
            "name": "exec-logfiles",
            "type": "Element",
            "required": True,
        }
    )
    parameter_combinations: Optional[ParameterCombinationsExec] = attr.ib(
        default=None,
        metadata={
            "name": "parameter-combinations",
            "type": "Element",
        },
    )
    old_versions: Optional[OldVersions] = attr.ib(
        default=None,
        metadata={
            "name": "old-versions",
            "type": "Element",
        },
    )


@attr.s(kw_only=True)
class InstancesArray:
    class Meta:
        name = "instances-array"

    pk: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    name: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    description: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    ordering: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    instances: Instances = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@attr.s(kw_only=True)
class Subdivision(TestElement):
    class Meta:
        name = "subdivision"

    library_information: Optional[LibraryInformation] = attr.ib(
        default=None,
        metadata={
            "name": "libraryInformation",
            "type": "Element",
        },
    )
    called_libraries: Optional[CalledLibraries] = attr.ib(
        default=None,
        metadata={
            "name": "called-libraries",
            "type": "Element",
        },
    )
    old_versions: Optional[SubdivisionVersions] = attr.ib(
        default=None,
        metadata={
            "name": "old-versions",
            "type": "Element",
        },
    )
    element: List[TestElement] = attr.ib(
        factory=list,
        metadata={
            "type": "Element",
        },
    )
    type_value: str = attr.ib(
        init=False,
        default="subdivision",
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )


@attr.s(kw_only=True)
class EquivalenceClasses:
    class Meta:
        name = "equivalence-classes"

    equivalence_class: List[EquivalenceClass] = attr.ib(
        factory=list,
        metadata={
            "name": "equivalence-class",
            "type": "Element",
        },
    )


@attr.s(kw_only=True)
class ExecutionCycles:
    class Meta:
        name = "execution-cycles"

    execution: List[Execution] = attr.ib(
        factory=list,
        metadata={
            "type": "Element",
        },
    )


@attr.s(kw_only=True)
class InstancesArrays:
    class Meta:
        name = "instances-arrays"

    instances_array: List[InstancesArray] = attr.ib(
        factory=list,
        metadata={
            "name": "instances-array",
            "type": "Element",
        },
    )


@attr.s(kw_only=True)
class Interaction(TestElement):
    class Meta:
        name = "interaction"

    status: SpecificationStatus = attr.ib(
        default=SpecificationStatus.SPECSTATUS_INPROGRESS,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    default_call_type: DefaultCallType = attr.ib(
        metadata={
            "name": "default-call-type",
            "type": "Element",
            "required": True,
        }
    )
    advanced_content: Optional[AdvancedContent] = attr.ib(
        default=None,
        metadata={
            "name": "advancedContent",
            "type": "Element",
        },
    )
    preconditions: Conditions = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    postconditions: Conditions = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    parameters: Parameters = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    call_sequence: CallSequence = attr.ib(
        metadata={
            "name": "call-sequence",
            "type": "Element",
            "required": True,
        }
    )
    identical_version_metaword_mapping: Optional[IdenticalVersionMetawordMapping] = attr.ib(
        default=None,
        metadata={
            "name": "identical-version-metaword-mapping",
            "type": "Element",
        },
    )
    old_versions: Optional[InteractionVersions] = attr.ib(
        default=None,
        metadata={
            "name": "old-versions",
            "type": "Element",
        },
    )
    type_value: str = attr.ib(
        init=False,
        default="interaction",
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )


@attr.s(kw_only=True)
class TestElements:
    class Meta:
        name = "test-elements"

    element: List[Subdivision] = attr.ib(
        factory=list,
        metadata={
            "type": "Element",
        },
    )


@attr.s(kw_only=True)
class Datatype(TestElement):
    class Meta:
        name = "datatype"

    status: SpecificationStatus = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    kind: Optional[KindOfDataType] = attr.ib(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    fields: Fields = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    instances_arrays: InstancesArrays = attr.ib(
        metadata={
            "name": "instances-arrays",
            "type": "Element",
            "required": True,
        }
    )
    equivalence_classes: EquivalenceClasses = attr.ib(
        metadata={
            "name": "equivalence-classes",
            "type": "Element",
            "required": True,
        }
    )
    identical_version_datatype_mapping: Optional[IdenticalVersionDatatypeMapping] = attr.ib(
        default=None,
        metadata={
            "name": "identical-version-datatype-mapping",
            "type": "Element",
        },
    )
    old_versions: Optional[DatatypeVersions] = attr.ib(
        default=None,
        metadata={
            "name": "old-versions",
            "type": "Element",
        },
    )
    element: List[Interaction] = attr.ib(
        factory=list,
        metadata={
            "type": "Element",
        },
    )
    type_value: str = attr.ib(
        init=False,
        default="datatype",
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )


@attr.s(kw_only=True)
class Specification:
    class Meta:
        name = "specification"

    details: "SpecificationDetails" = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    description: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    html_description: str = attr.ib(
        metadata={
            "name": "html-description",
            "type": "Element",
            "required": True,
        }
    )
    review_comments: Optional[str] = attr.ib(
        default=None,
        metadata={
            "name": "review-comments",
            "type": "Element",
        },
    )
    html_review_comments: Optional[str] = attr.ib(
        default=None,
        metadata={
            "name": "html-review-comments",
            "type": "Element",
        },
    )
    keywords: Keywords = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    edited_requirements: RequirementRefs = attr.ib(
        metadata={
            "name": "edited-requirements",
            "type": "Element",
            "required": True,
        }
    )
    non_edited_requirements: RequirementRefs = attr.ib(
        metadata={
            "name": "non-edited-requirements",
            "type": "Element",
            "required": True,
        }
    )
    user_defined_fields: UserDefinedFields = attr.ib(
        metadata={
            "name": "userDefinedFields",
            "type": "Element",
            "required": True,
        }
    )
    interaction: Optional[Interaction] = attr.ib(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    parameter_combinations: Optional[ParameterCombinationsSpec] = attr.ib(
        default=None,
        metadata={
            "name": "parameter-combinations",
            "type": "Element",
        },
    )
    old_versions: Optional[OldVersions] = attr.ib(
        default=None,
        metadata={
            "name": "old-versions",
            "type": "Element",
        },
    )


@attr.s(kw_only=True)
class Testcase:
    class Meta:
        name = "testcase"

    pk: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    name: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    order_pos: str = attr.ib(
        metadata={
            "name": "order-pos",
            "type": "Element",
            "required": True,
        }
    )
    uid: Optional[str] = attr.ib(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    specification: Specification = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    automation: Automation = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    execution_cycles: ExecutionCycles = attr.ib(
        metadata={
            "name": "execution-cycles",
            "type": "Element",
            "required": True,
        }
    )


@attr.s(kw_only=True)
class Testtheme:
    class Meta:
        name = "testtheme"

    pk: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    name: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    order_pos: str = attr.ib(
        metadata={
            "name": "order-pos",
            "type": "Element",
            "required": True,
        }
    )
    uid: Optional[str] = attr.ib(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    specification: Specification = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    automation: Automation = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    execution_cycles: ExecutionCycles = attr.ib(
        metadata={
            "name": "execution-cycles",
            "type": "Element",
            "required": True,
        }
    )
    children: "TestthemeChildren" = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@attr.s(kw_only=True)
class Version:
    class Meta:
        name = "version"

    content: List[object] = attr.ib(
        factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "pk",
                    "type": str,
                },
                {
                    "name": "name",
                    "type": str,
                },
                {
                    "name": "user",
                    "type": str,
                },
                {
                    "name": "comment",
                    "type": str,
                },
                {
                    "name": "date",
                    "type": str,
                },
                {
                    "name": "status",
                    "type": str,
                },
                {
                    "name": "verdict",
                    "type": str,
                },
                {
                    "name": "exec-status",
                    "type": str,
                },
                {
                    "name": "type",
                    "type": str,
                },
                {
                    "name": "labels",
                    "type": LabelsRef,
                },
                {
                    "name": "reference",
                    "type": Reference,
                },
                {
                    "name": "error-id",
                    "type": ErrorId,
                },
                {
                    "name": "element",
                    "type": TestElement,
                },
                {
                    "name": "specification",
                    "type": Specification,
                },
                {
                    "name": "automation",
                    "type": Automation,
                },
                {
                    "name": "execution",
                    "type": Execution,
                },
            ),
        },
    )


@attr.s(kw_only=True)
class Details:
    class Meta:
        name = "details"

    version: Version = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    pk: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    identical_version_pk: str = attr.ib(
        metadata={
            "name": "identicalVersionPK",
            "type": "Element",
            "required": True,
        }
    )
    locker: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    responsible: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    reviewer: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    priority: TsePriority = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@attr.s(kw_only=True)
class Requirement:
    class Meta:
        name = "requirement"

    pk: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    name: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    id: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    extended_id: str = attr.ib(
        metadata={
            "name": "extended-id",
            "type": "Element",
            "required": True,
        }
    )
    version: Version = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    owner: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    status: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    priority: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    repository_id: str = attr.ib(
        metadata={
            "name": "repository-id",
            "type": "Element",
            "required": True,
        }
    )
    udfs: Optional[Udfs] = attr.ib(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@attr.s(kw_only=True)
class RequirementNode:
    class Meta:
        name = "requirement-node"

    requirement_pk: str = attr.ib(
        metadata={
            "name": "requirement-pk",
            "type": "Element",
            "required": True,
        }
    )
    name: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    id: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    version: Version = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    type_value: RequirementNodeType = attr.ib(
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        }
    )
    children: "RequirementChildren" = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@attr.s(kw_only=True)
class TestthemeChildren:
    class Meta:
        name = "testtheme-children"

    testtheme: List[Testtheme] = attr.ib(
        factory=list,
        metadata={
            "type": "Element",
        },
    )
    testcase: List[Testcase] = attr.ib(
        factory=list,
        metadata={
            "type": "Element",
        },
    )


@attr.s(kw_only=True)
class Testthemes:
    class Meta:
        name = "testthemes"

    testtheme: List[Testtheme] = attr.ib(
        factory=list,
        metadata={
            "type": "Element",
        },
    )


@attr.s(kw_only=True)
class AutomationDetails(Details):
    class Meta:
        name = "automation-details"

    status: AutomationStatus = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    target_date: str = attr.ib(
        metadata={
            "name": "target-date",
            "type": "Element",
            "required": True,
        }
    )
    references: References = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@attr.s(kw_only=True)
class ExecutionDetails(Details):
    class Meta:
        name = "execution-details"

    status: ActivityStatus = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    target_date: str = attr.ib(
        metadata={
            "name": "target-date",
            "type": "Element",
            "required": True,
        }
    )
    references: References = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@attr.s(kw_only=True)
class RequirementChildren:
    class Meta:
        name = "requirement-children"

    requirement_node: List[RequirementNode] = attr.ib(
        factory=list,
        metadata={
            "name": "requirement-node",
            "type": "Element",
        },
    )


@attr.s(kw_only=True)
class Requirements:
    class Meta:
        name = "requirements"

    requirement: List[Requirement] = attr.ib(
        factory=list,
        metadata={
            "type": "Element",
        },
    )


@attr.s(kw_only=True)
class SpecificationDetails(Details):
    class Meta:
        name = "specification-details"

    status: SpecificationStatus = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    target_date: str = attr.ib(
        metadata={
            "name": "target-date",
            "type": "Element",
            "required": True,
        }
    )
    references: References = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@attr.s(kw_only=True)
class Baseline:
    class Meta:
        name = "baseline"

    details: Optional[BaselineDetails] = attr.ib(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    children: Optional[RequirementChildren] = attr.ib(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    project_pk_ref: Optional[Ref] = attr.ib(
        default=None,
        metadata={
            "name": "project-pk-ref",
            "type": "Element",
        },
    )
    project: Optional[str] = attr.ib(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    name: Optional[str] = attr.ib(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@attr.s(kw_only=True)
class Baselines:
    class Meta:
        name = "baselines"

    baseline: List[Baseline] = attr.ib(
        factory=list,
        metadata={
            "type": "Element",
        },
    )


@attr.s(kw_only=True)
class Testobjectversion:
    class Meta:
        name = "testobjectversion"

    pk: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    id: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    startdate: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    enddate: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    status: ProjectStatus = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    created_time: str = attr.ib(
        metadata={
            "name": "createdTime",
            "type": "Element",
            "required": True,
        }
    )
    visible_for_testers: Optional[bool] = attr.ib(
        default=None,
        metadata={
            "name": "visibleForTesters",
            "type": "Element",
        },
    )
    cloning_visibility: Optional[str] = attr.ib(
        default=None,
        metadata={
            "name": "cloningVisibility",
            "type": "Element",
        },
    )
    base_tov: Optional[str] = attr.ib(
        default=None,
        metadata={
            "name": "baseTOV",
            "type": "Element",
        },
    )
    source_tov_ref: Optional[Ref] = attr.ib(
        default=None,
        metadata={
            "name": "sourceTOV-ref",
            "type": "Element",
        },
    )
    variants_definition_ref: Optional[Ref] = attr.ib(
        default=None,
        metadata={
            "name": "variantsDefinition-ref",
            "type": "Element",
        },
    )
    description: str = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    html_description: str = attr.ib(
        metadata={
            "name": "html-description",
            "type": "Element",
            "required": True,
        }
    )
    testing_intelligence: str = attr.ib(
        metadata={
            "name": "testingIntelligence",
            "type": "Element",
            "required": True,
        }
    )
    baselines: Baselines = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    placeholders: Placeholders = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    variants_definitions: VariantsDefinitions = attr.ib(
        metadata={
            "name": "variantsDefinitions",
            "type": "Element",
            "required": True,
        }
    )
    variants_markers: VariantsMarkers = attr.ib(
        metadata={
            "name": "variantsMarkers",
            "type": "Element",
            "required": True,
        }
    )
    placeholder_values: PlaceholderValues = attr.ib(
        metadata={
            "name": "placeholderValues",
            "type": "Element",
            "required": True,
        }
    )
    testcycles: Testcycles = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    testthemes: Testthemes = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    test_elements: TestElements = attr.ib(
        metadata={
            "name": "test-elements",
            "type": "Element",
            "required": True,
        }
    )


@attr.s(kw_only=True)
class Testobjectversions:
    class Meta:
        name = "testobjectversions"

    testobjectversion: List[Testobjectversion] = attr.ib(
        factory=list,
        metadata={
            "type": "Element",
        },
    )


@attr.s(kw_only=True)
class ProjectDump:
    class Meta:
        name = "project-dump"

    details: ProjectDetails = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    userroles: Optional[Userroles] = attr.ib(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    user_defined_fields: Optional[UserDefinedFieldsDefinition] = attr.ib(
        default=None,
        metadata={
            "name": "UserDefinedFields",
            "type": "Element",
        },
    )
    defect_user_defined_fields: Optional[DefectUserDefinedFields] = attr.ib(
        default=None,
        metadata={
            "name": "DefectUserDefinedFields",
            "type": "Element",
        },
    )
    keywords: Optional[KeywordsDefinition] = attr.ib(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    labels: Optional[Labels] = attr.ib(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    library_labels: Optional[LibraryLabels] = attr.ib(
        default=None,
        metadata={
            "name": "library-labels",
            "type": "Element",
        },
    )
    dm_settings: Optional[DmSettings] = attr.ib(
        default=None,
        metadata={
            "name": "dm-settings",
            "type": "Element",
        },
    )
    error_ids: Optional[ErrorIds] = attr.ib(
        default=None,
        metadata={
            "name": "error-ids",
            "type": "Element",
        },
    )
    references: Optional[References] = attr.ib(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    requirement_baselines: Optional[Baselines] = attr.ib(
        default=None,
        metadata={
            "name": "requirement-baselines",
            "type": "Element",
        },
    )
    testobjectversions: Testobjectversions = attr.ib(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    requirements: Optional[Requirements] = attr.ib(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    referenced_user_names: Optional[ReferencedUserNames] = attr.ib(
        default=None,
        metadata={
            "name": "referenced-user-names",
            "type": "Element",
        },
    )
    errors: Optional[Errors] = attr.ib(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    warnings: Optional[Warnings] = attr.ib(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    version: str = attr.ib(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    build_number: str = attr.ib(
        metadata={
            "name": "build-number",
            "type": "Attribute",
            "required": True,
        }
    )
    repository: Optional[str] = attr.ib(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
