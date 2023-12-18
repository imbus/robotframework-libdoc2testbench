from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional


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


@dataclass
class AdvancedContent:
    class Meta:
        name = "advancedContent"

    external_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "externalIdentifier",
            "type": "Element",
            "required": True,
        },
    )
    content: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "contentType",
            "type": "Attribute",
            "required": True,
        },
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


@dataclass
class BaselineDetails:
    class Meta:
        name = "baseline-details"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    project: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    last_update: Optional[str] = field(
        default=None,
        metadata={
            "name": "lastUpdate",
            "type": "Element",
            "required": True,
        },
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    repository_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "repository-id",
            "type": "Element",
            "required": True,
        },
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


@dataclass
class CalledLibrary:
    class Meta:
        name = "calledLibrary"

    pk: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    baseline_pk: Optional[str] = field(
        default=None,
        metadata={
            "name": "baselinePK",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class ClassMapping:
    class Meta:
        name = "class-mapping"

    class_value: List[str] = field(
        default_factory=list,
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


@dataclass
class ErrorIdReferences:
    class Meta:
        name = "error-id-references"

    error_id_reference: List[str] = field(
        default_factory=list,
        metadata={
            "name": "error-id-reference",
            "type": "Element",
        },
    )


@dataclass
class ExecLogfile:
    class Meta:
        name = "exec-logfile"

    filename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    file_pk: Optional[str] = field(
        default=None,
        metadata={
            "name": "file-pk",
            "type": "Element",
            "required": True,
        },
    )
    result_file_pk: Optional[str] = field(
        default=None,
        metadata={
            "name": "result-file-pk",
            "type": "Element",
            "required": True,
        },
    )
    charset: Optional[str] = field(
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


@dataclass
class ForeignLibraryLabel:
    class Meta:
        name = "foreignLibraryLabel"

    pk: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    library_pk: Optional[str] = field(
        default=None,
        metadata={
            "name": "library-pk",
            "type": "Element",
            "required": True,
        },
    )
    project: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    owner: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class IdenticalVersionDatatype:
    class Meta:
        name = "identical-version-datatype"

    work_pk: Optional[str] = field(
        default=None,
        metadata={
            "name": "workPK",
            "type": "Attribute",
            "required": True,
        },
    )
    vers_pk: Optional[str] = field(
        default=None,
        metadata={
            "name": "versPK",
            "type": "Attribute",
            "required": True,
        },
    )
    is_changed_def_type: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isChangedDefType",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class IdenticalVersionMetawordParam:
    class Meta:
        name = "identical-version-metaword-param"

    work_param_pk: Optional[str] = field(
        default=None,
        metadata={
            "name": "workParamPK",
            "type": "Attribute",
            "required": True,
        },
    )
    vers_param_pk: Optional[str] = field(
        default=None,
        metadata={
            "name": "versParamPK",
            "type": "Attribute",
            "required": True,
        },
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


@dataclass
class Keyword:
    class Meta:
        name = "keyword"

    pk: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


class KindOfDataType(Enum):
    REGULAR = "regular"
    REFERENCE = "reference"
    GLOBAL = "global"
    ACCEPTING_GLOBAL = "accepting-global"


@dataclass
class Label:
    """
    :ivar pk:
    :ivar name:
    :ivar owner: the user login
    """

    class Meta:
        name = "label"

    pk: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    owner: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class LibraryInformation:
    class Meta:
        name = "libraryInformation"

    library_pk: Optional[str] = field(
        default=None,
        metadata={
            "name": "libraryPK",
            "type": "Element",
            "required": True,
        },
    )
    foreign_library_tov_pk: Optional[str] = field(
        default=None,
        metadata={
            "name": "foreignLibraryTovPK",
            "type": "Element",
        },
    )
    foreign_library_pk: Optional[str] = field(
        default=None,
        metadata={
            "name": "foreignLibraryPK",
            "type": "Element",
        },
    )
    source_project: Optional[str] = field(
        default=None,
        metadata={
            "name": "sourceProject",
            "type": "Element",
        },
    )
    source_test_object_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "sourceTestObjectVersion",
            "type": "Element",
        },
    )


@dataclass
class LibraryLabel:
    class Meta:
        name = "libraryLabel"

    pk: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    library_pk: Optional[str] = field(
        default=None,
        metadata={
            "name": "library-pk",
            "type": "Element",
            "required": True,
        },
    )
    owner: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Message:
    class Meta:
        name = "message"

    object_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "object",
            "type": "Element",
            "required": True,
        },
    )
    pk: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


class MustField(Enum):
    """
    :cvar VALUE_0: FALSE
    :cvar VALUE_1: TRUE
    """

    FALSE = 0
    TRUE = 1


@dataclass
class OldVersions:
    class Meta:
        name = "old-versions"

    version: List["Version"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Placeholder:
    class Meta:
        name = "placeholder"

    pk: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class PriorityMapping:
    class Meta:
        name = "priority-mapping"

    priority: List[str] = field(
        default_factory=list,
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


@dataclass
class Ref:
    class Meta:
        name = "ref"

    pk: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


class ReferenceKind(Enum):
    """
    :cvar VALUE_0: REFERENCE
    :cvar VALUE_1: LINK
    :cvar VALUE_2: ATTACHMENT
    """

    REFERENCE = 0
    LINK = 1
    ATTACHMENT = 2


@dataclass
class ReferencedUserNames:
    """
    :ivar user_name: user login
    :ivar user_pk: number (long)
    """

    class Meta:
        name = "referenced-user-names"

    user_name: List[str] = field(
        default_factory=list,
        metadata={
            "name": "user-name",
            "type": "Element",
            "sequence": 1,
        },
    )
    user_pk: List[str] = field(
        default_factory=list,
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


@dataclass
class RequirementRepository:
    class Meta:
        name = "requirement-repository"

    pk: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    login: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    password: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Settings:
    class Meta:
        name = "settings"

    overwrite_exec_responsible: Optional[bool] = field(
        default=None,
        metadata={
            "name": "overwrite-exec-responsible",
            "type": "Element",
            "required": True,
        },
    )
    optional_checkin: Optional[bool] = field(
        default=None,
        metadata={
            "name": "optional-checkin",
            "type": "Element",
            "required": True,
        },
    )
    hide_exec_auto_checkin: Optional[bool] = field(
        default=None,
        metadata={
            "name": "hide-exec-auto-checkin",
            "type": "Element",
        },
    )
    extended_interactions_content: Optional[bool] = field(
        default=None,
        metadata={
            "name": "extended-interactions-content",
            "type": "Element",
        },
    )
    libraries_state: Optional[bool] = field(
        default=None,
        metadata={
            "name": "libraries-state",
            "type": "Element",
        },
    )
    global_datatypes_state: Optional[bool] = field(
        default=None,
        metadata={
            "name": "global-datatypes-state",
            "type": "Element",
        },
    )
    filter_sync_interval: Optional[int] = field(
        default=None,
        metadata={
            "name": "filter-sync-interval",
            "type": "Element",
            "required": True,
        },
    )
    ignore_not_edited: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ignore-not-edited",
            "type": "Element",
            "required": True,
        },
    )
    ignore_not_planned: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ignore-not-planned",
            "type": "Element",
            "required": True,
        },
    )
    designers_may_manage_baselines: Optional[bool] = field(
        default=None,
        metadata={
            "name": "designers-may-manage-baselines",
            "type": "Element",
            "required": True,
        },
    )
    designers_may_import_baselines: Optional[bool] = field(
        default=None,
        metadata={
            "name": "designers-may-import-baselines",
            "type": "Element",
            "required": True,
        },
    )
    only_admins_manage_udfs: Optional[bool] = field(
        default=None,
        metadata={
            "name": "only-admins-manage-udfs",
            "type": "Element",
            "required": True,
        },
    )
    variants_management_enabled: Optional[bool] = field(
        default=None,
        metadata={
            "name": "variants-management-enabled",
            "type": "Element",
            "required": True,
        },
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


@dataclass
class StatusMapping:
    class Meta:
        name = "status-mapping"

    status: List[str] = field(
        default_factory=list,
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


@dataclass
class UdfValue:
    class Meta:
        name = "udf-value"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
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


@dataclass
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


@dataclass
class UserMapping:
    class Meta:
        name = "user-mapping"

    itblogin: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    dmlogin: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class VariantsDefinition:
    class Meta:
        name = "variantsDefinition"

    pk: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    status: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    html_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "html-description",
            "type": "Element",
            "required": True,
        },
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


@dataclass
class DefectUserDefinedField:
    pk: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    ordering: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    must_field: Optional[MustField] = field(
        default=None,
        metadata={
            "name": "mustField",
            "type": "Element",
            "required": True,
        },
    )
    udf_sync_option: Optional[UdfSyncOption] = field(
        default=None,
        metadata={
            "name": "udfSyncOption",
            "type": "Element",
            "required": True,
        },
    )
    udf_type: Optional[UdfType] = field(
        default=None,
        metadata={
            "name": "udfType",
            "type": "Element",
            "required": True,
        },
    )
    value: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
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

    pk: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    ordering: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    must_field: Optional[MustField] = field(
        default=None,
        metadata={
            "name": "mustField",
            "type": "Element",
            "required": True,
        },
    )
    udf_scopes: Optional[str] = field(
        default=None,
        metadata={
            "name": "udfScopes",
            "type": "Element",
            "required": True,
        },
    )
    udf_type: Optional[UdfType] = field(
        default=None,
        metadata={
            "name": "udfType",
            "type": "Element",
            "required": True,
        },
    )
    value: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Automation:
    class Meta:
        name = "automation"

    details: Optional["AutomationDetails"] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    script_editor: Optional[str] = field(
        default=None,
        metadata={
            "name": "script-editor",
            "type": "Element",
            "required": True,
        },
    )
    script_template: Optional[str] = field(
        default=None,
        metadata={
            "name": "script-template",
            "type": "Element",
            "required": True,
        },
    )
    old_versions: Optional[OldVersions] = field(
        default=None,
        metadata={
            "name": "old-versions",
            "type": "Element",
        },
    )


@dataclass
class CalledLibraries:
    class Meta:
        name = "called-libraries"

    called_library: List[CalledLibrary] = field(
        default_factory=list,
        metadata={
            "name": "calledLibrary",
            "type": "Element",
        },
    )


@dataclass
class ConditionRef:
    class Meta:
        name = "condition-ref"

    condition_ref: Optional[Ref] = field(
        default=None,
        metadata={
            "name": "condition-ref",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class DefaultCallType:
    class Meta:
        name = "default-call-type"

    name: Optional[DefaultCallTypeName] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    value: Optional[BinaryDigit] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class DefaultValue:
    class Meta:
        name = "default-value"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    equivalence_class_ref: Optional[Ref] = field(
        default=None,
        metadata={
            "name": "equivalence-class-ref",
            "type": "Element",
        },
    )
    representative_ref: Optional[Ref] = field(
        default=None,
        metadata={
            "name": "representative-ref",
            "type": "Element",
        },
    )
    instances_array_ref: Optional[Ref] = field(
        default=None,
        metadata={
            "name": "instances-array-ref",
            "type": "Element",
        },
    )
    type_attribute: Optional[DefaultValueType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ErrorIdRefs:
    class Meta:
        name = "error-id-refs"

    error_id_ref: List[Ref] = field(
        default_factory=list,
        metadata={
            "name": "error-id-ref",
            "type": "Element",
        },
    )


@dataclass
class Errors:
    class Meta:
        name = "errors"

    error: List[Message] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ExecLogfiles:
    class Meta:
        name = "exec-logfiles"

    exec_logfile: List[ExecLogfile] = field(
        default_factory=list,
        metadata={
            "name": "exec-logfile",
            "type": "Element",
        },
    )


@dataclass
class Field:
    """
    :ivar sequence_pk:
    :ivar name:
    :ivar datatype_ref: pk of the data type, -1 by generic parameters
    :ivar definition_type:
    """

    class Meta:
        name = "field"

    sequence_pk: Optional[str] = field(
        default=None,
        metadata={
            "name": "sequence-pk",
            "type": "Element",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    datatype_ref: Optional[Ref] = field(
        default=None,
        metadata={
            "name": "datatype-ref",
            "type": "Element",
            "required": True,
        },
    )
    definition_type: Optional[DefinitionType] = field(
        default=None,
        metadata={
            "name": "definition-type",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class ForeignLibraryLabelGroup:
    class Meta:
        name = "foreignLibraryLabelGroup"

    label: List[ForeignLibraryLabel] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class IdenticalVersionDatatypeMapping:
    class Meta:
        name = "identical-version-datatype-mapping"

    identical_version_datatype: List[IdenticalVersionDatatype] = field(
        default_factory=list,
        metadata={
            "name": "identical-version-datatype",
            "type": "Element",
        },
    )


@dataclass
class IdenticalVersionMetaword:
    class Meta:
        name = "identical-version-metaword"

    identical_version_metaword_param: List[IdenticalVersionMetawordParam] = field(
        default_factory=list,
        metadata={
            "name": "identical-version-metaword-param",
            "type": "Element",
        },
    )
    work_pk: Optional[str] = field(
        default=None,
        metadata={
            "name": "workPK",
            "type": "Attribute",
            "required": True,
        },
    )
    vers_pk: Optional[str] = field(
        default=None,
        metadata={
            "name": "versPK",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Keywords:
    class Meta:
        name = "keywords"

    content: List[object] = field(
        default_factory=list,
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


@dataclass
class KeywordsDefinition:
    class Meta:
        name = "keywords-definition"

    keyword: List[Keyword] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class LabelsRef:
    class Meta:
        name = "labels-ref"

    label_ref: List[Ref] = field(
        default_factory=list,
        metadata={
            "name": "label-ref",
            "type": "Element",
        },
    )


@dataclass
class LibraryLabelGroup:
    class Meta:
        name = "libraryLabelGroup"

    label: List[LibraryLabel] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Marker:
    class Meta:
        name = "marker"

    marker_ref: List[Ref] = field(
        default_factory=list,
        metadata={
            "name": "marker-ref",
            "type": "Element",
        },
    )
    named_variants_marker: List[str] = field(
        default_factory=list,
        metadata={
            "name": "named-variants-marker",
            "type": "Element",
        },
    )


@dataclass
class PlaceholderValue:
    class Meta:
        name = "placeholderValue"

    pk: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    placeholder_ref: Optional[Ref] = field(
        default=None,
        metadata={
            "name": "placeholder-ref",
            "type": "Element",
            "required": True,
        },
    )
    variants_definition_ref: Optional[Ref] = field(
        default=None,
        metadata={
            "name": "variantsDefinition-ref",
            "type": "Element",
            "required": True,
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Placeholders:
    class Meta:
        name = "placeholders"

    placeholder: List[Placeholder] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Reference:
    class Meta:
        name = "reference"

    pk: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    filename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    type_value: Optional[ReferenceKind] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    attachment_pk: Optional[str] = field(
        default=None,
        metadata={
            "name": "attachment-pk",
            "type": "Element",
        },
    )
    attachment_path: Optional[str] = field(
        default=None,
        metadata={
            "name": "attachment-path",
            "type": "Element",
        },
    )
    attachment_filename: Optional[str] = field(
        default=None,
        metadata={
            "name": "attachment-filename",
            "type": "Element",
        },
    )
    attachment_lastedited: Optional[str] = field(
        default=None,
        metadata={
            "name": "attachment-lastedited",
            "type": "Element",
        },
    )
    attachment_lasteditor: Optional[str] = field(
        default=None,
        metadata={
            "name": "attachment-lasteditor",
            "type": "Element",
        },
    )
    attachment_file_pk: Optional[str] = field(
        default=None,
        metadata={
            "name": "attachment-file-pk",
            "type": "Element",
        },
    )
    old_versions: Optional[OldVersions] = field(
        default=None,
        metadata={
            "name": "old-versions",
            "type": "Element",
        },
    )


@dataclass
class RequirementProject:
    class Meta:
        name = "requirement-project"

    content: List[object] = field(
        default_factory=list,
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


@dataclass
class RequirementRefs:
    class Meta:
        name = "requirement-refs"

    requirement_ref: List[Ref] = field(
        default_factory=list,
        metadata={
            "name": "requirement-ref",
            "type": "Element",
        },
    )


@dataclass
class RequirementRepositories:
    class Meta:
        name = "requirement-repositories"

    requirement_repository: List[RequirementRepository] = field(
        default_factory=list,
        metadata={
            "name": "requirement-repository",
            "type": "Element",
        },
    )


@dataclass
class Roles:
    class Meta:
        name = "roles"

    role: List[ProjectRole] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 5,
        },
    )
    read_only: Optional[bool] = field(
        default=None,
        metadata={
            "name": "read-only",
            "type": "Attribute",
        },
    )


@dataclass
class SequencePath:
    class Meta:
        name = "sequence-path"

    sequence_ref: List[Ref] = field(
        default_factory=list,
        metadata={
            "name": "sequence-ref",
            "type": "Element",
        },
    )


@dataclass
class Testcycle:
    class Meta:
        name = "testcycle"

    pk: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    created_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "createdTime",
            "type": "Element",
            "required": True,
        },
    )
    startdate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    enddate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    status: Optional[ProjectStatus] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    visible_for_testers: Optional[bool] = field(
        default=None,
        metadata={
            "name": "visibleForTesters",
            "type": "Element",
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    html_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "html-description",
            "type": "Element",
            "required": True,
        },
    )
    testing_intelligence: Optional[str] = field(
        default=None,
        metadata={
            "name": "testingIntelligence",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class UdfDefinition:
    class Meta:
        name = "udf-definition"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    type_value: Optional[UdfDefinitionType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    repository_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "repository-id",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Udfs:
    class Meta:
        name = "udfs"

    udf: List[UdfValue] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class UserMappings:
    class Meta:
        name = "user-mappings"

    user_mapping: List[UserMapping] = field(
        default_factory=list,
        metadata={
            "name": "user-mapping",
            "type": "Element",
        },
    )


@dataclass
class UserDefinedField:
    class Meta:
        name = "userDefinedField"

    udfpk: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    udf_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "udfName",
            "type": "Element",
            "required": True,
        },
    )
    udf_type: Optional[UdfType] = field(
        default=None,
        metadata={
            "name": "udfType",
            "type": "Element",
            "required": True,
        },
    )
    ordering: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Value:
    class Meta:
        name = "value"

    default_value: Optional[bool] = field(
        default=None,
        metadata={
            "name": "default-value",
            "type": "Attribute",
        },
    )
    content: List[object] = field(
        default_factory=list,
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


@dataclass
class VariantsDefinitions:
    class Meta:
        name = "variantsDefinitions"

    variants_definition: List[VariantsDefinition] = field(
        default_factory=list,
        metadata={
            "name": "variantsDefinition",
            "type": "Element",
        },
    )


@dataclass
class VariantsMarker:
    class Meta:
        name = "variantsMarker"

    pk: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    variants_definition_ref: Optional[Ref] = field(
        default=None,
        metadata={
            "name": "variantsDefinition-ref",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class VisibilityGroup:
    class Meta:
        name = "visibilityGroup"

    label: List[Label] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Warnings:
    class Meta:
        name = "warnings"

    warning: List[Message] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class DefectUserDefinedFields:
    defect_user_defined_field: List[DefectUserDefinedField] = field(
        default_factory=list,
        metadata={
            "name": "DefectUserDefinedField",
            "type": "Element",
        },
    )


@dataclass
class UserDefinedFieldsDefinition:
    user_defined_field: List[UserDefinedFieldDefinition] = field(
        default_factory=list,
        metadata={
            "name": "UserDefinedField",
            "type": "Element",
        },
    )


@dataclass
class CallParameter:
    class Meta:
        name = "call-parameter"

    pk: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    parameter_datatype_ref: Optional[Ref] = field(
        default=None,
        metadata={
            "name": "parameter-datatype-ref",
            "type": "Element",
            "required": True,
        },
    )
    parent_parameter_ref: Optional[object] = field(
        default=None,
        metadata={
            "name": "parent-parameter-ref",
            "type": "Element",
        },
    )
    sequence_path: Optional[SequencePath] = field(
        default=None,
        metadata={
            "name": "sequence-path",
            "type": "Element",
        },
    )
    instances_array_ref: Optional[Ref] = field(
        default=None,
        metadata={
            "name": "instances-array-ref",
            "type": "Element",
        },
    )
    representative_ref: Optional[Ref] = field(
        default=None,
        metadata={
            "name": "representative-ref",
            "type": "Element",
        },
    )
    type_value: Optional[CallParameterType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        },
    )
    default_value: Optional[bool] = field(
        default=None,
        metadata={
            "name": "default-value",
            "type": "Attribute",
        },
    )


@dataclass
class Conditions:
    class Meta:
        name = "conditions"

    condition: List[ConditionRef] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
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

    pk: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    system: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    project: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    readlogin: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    firstsync: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    syncinterval: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    statusattribute: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    statussyncoption: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    statusdefaultvalue: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    priorityattribute: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    prioritysyncoption: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    prioritydefaultvalue: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    classattribute: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    classsyncoption: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    classdefaultvalue: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    status_mapping: Optional[StatusMapping] = field(
        default=None,
        metadata={
            "name": "status-mapping",
            "type": "Element",
            "required": True,
        },
    )
    priority_mapping: Optional[PriorityMapping] = field(
        default=None,
        metadata={
            "name": "priority-mapping",
            "type": "Element",
            "required": True,
        },
    )
    class_mapping: Optional[ClassMapping] = field(
        default=None,
        metadata={
            "name": "class-mapping",
            "type": "Element",
            "required": True,
        },
    )
    user_mappings: Optional[UserMappings] = field(
        default=None,
        metadata={
            "name": "user-mappings",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
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

    pk: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    status: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    priority: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    classification: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    tester: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    last_edited: Optional[str] = field(
        default=None,
        metadata={
            "name": "lastEdited",
            "type": "Element",
            "required": True,
        },
    )
    created: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    used_in_cycles: List[str] = field(
        default_factory=list,
        metadata={
            "name": "used-in-cycles",
            "type": "Element",
        },
    )
    last_editor: Optional[str] = field(
        default=None,
        metadata={
            "name": "lastEditor",
            "type": "Element",
            "required": True,
        },
    )
    dm_system: Optional[str] = field(
        default=None,
        metadata={
            "name": "dmSystem",
            "type": "Element",
            "required": True,
        },
    )
    dm_project: Optional[str] = field(
        default=None,
        metadata={
            "name": "dmProject",
            "type": "Element",
            "required": True,
        },
    )
    identical_version_pk: Optional[str] = field(
        default=None,
        metadata={
            "name": "identicalVersionPK",
            "type": "Element",
            "required": True,
        },
    )
    error_id_references: Optional[ErrorIdReferences] = field(
        default=None,
        metadata={
            "name": "error-id-references",
            "type": "Element",
            "required": True,
        },
    )
    udfs: List[Udfs] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    old_versions: Optional[OldVersions] = field(
        default=None,
        metadata={
            "name": "old-versions",
            "type": "Element",
        },
    )


@dataclass
class Fields:
    class Meta:
        name = "fields"

    field_value: List[Field] = field(
        default_factory=list,
        metadata={
            "name": "field",
            "type": "Element",
        },
    )


@dataclass
class IdenticalVersionMetawordMapping:
    class Meta:
        name = "identical-version-metaword-mapping"

    identical_version_metaword: List[IdenticalVersionMetaword] = field(
        default_factory=list,
        metadata={
            "name": "identical-version-metaword",
            "type": "Element",
        },
    )


@dataclass
class Labels:
    class Meta:
        name = "labels"

    public: Optional[VisibilityGroup] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    private: Optional[VisibilityGroup] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class LibraryLabels:
    class Meta:
        name = "libraryLabels"

    local: Optional[LibraryLabelGroup] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    foreign: Optional[ForeignLibraryLabelGroup] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
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

    pk: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    datatype_ref: Optional[Ref] = field(
        default=None,
        metadata={
            "name": "datatype-ref",
            "type": "Element",
            "required": True,
        },
    )
    definition_type: Optional[DefinitionType] = field(
        default=None,
        metadata={
            "name": "definition-type",
            "type": "Element",
            "required": True,
        },
    )
    use_type: Optional[UseType] = field(
        default=None,
        metadata={
            "name": "use-type",
            "type": "Element",
            "required": True,
        },
    )
    default_value: Optional[DefaultValue] = field(
        default=None,
        metadata={
            "name": "default-value",
            "type": "Element",
        },
    )
    signature_uid: Optional[str] = field(
        default=None,
        metadata={
            "name": "signature-uid",
            "type": "Element",
        },
    )


@dataclass
class PlaceholderValues:
    class Meta:
        name = "placeholderValues"

    placeholder_value: List[PlaceholderValue] = field(
        default_factory=list,
        metadata={
            "name": "placeholderValue",
            "type": "Element",
        },
    )


@dataclass
class ProjectUser:
    class Meta:
        name = "project-user"

    content: List[object] = field(
        default_factory=list,
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


@dataclass
class References:
    class Meta:
        name = "references"

    reference: List[Reference] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    reference_ref: List[Ref] = field(
        default_factory=list,
        metadata={
            "name": "reference-ref",
            "type": "Element",
        },
    )
    reference_name: List[str] = field(
        default_factory=list,
        metadata={
            "name": "reference-name",
            "type": "Element",
        },
    )
    type_value: List[str] = field(
        default_factory=list,
        metadata={
            "name": "type",
            "type": "Element",
        },
    )


@dataclass
class RequirementProjects:
    class Meta:
        name = "requirement-projects"

    project: List[RequirementProject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class RequirementUdfs:
    class Meta:
        name = "requirement-udfs"

    udf: List[UdfDefinition] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class TestElementVersionInfo:
    class Meta:
        name = "test-element-version-info"

    pk: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    user: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    date: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    status: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    labels: Optional[LabelsRef] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Testcycles:
    class Meta:
        name = "testcycles"

    testcycle: List[Testcycle] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class UserDefinedFields:
    class Meta:
        name = "userDefinedFields"

    user_defined_field: List[UserDefinedField] = field(
        default_factory=list,
        metadata={
            "name": "userDefinedField",
            "type": "Element",
        },
    )


@dataclass
class Values:
    class Meta:
        name = "values"

    value: List[Value] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class VariantsMarkers:
    class Meta:
        name = "variantsMarkers"

    variants_marker: List[VariantsMarker] = field(
        default_factory=list,
        metadata={
            "name": "variantsMarker",
            "type": "Element",
        },
    )


@dataclass
class ConditionVersion(TestElementVersionInfo):
    class Meta:
        name = "condition-version"

    element: Optional["Condition"] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class DatatypeVersion(TestElementVersionInfo):
    class Meta:
        name = "datatype-version"

    element: Optional["Datatype"] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class ErrorIds:
    class Meta:
        name = "error-ids"

    error_id: List[ErrorId] = field(
        default_factory=list,
        metadata={
            "name": "error-id",
            "type": "Element",
        },
    )


@dataclass
class Instance:
    class Meta:
        name = "instance"

    pk: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    ordering: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    values: Optional[Values] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class InteractionVersion(TestElementVersionInfo):
    class Meta:
        name = "interaction-version"

    element: Optional["Interaction"] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class ParameterCombinationExec:
    class Meta:
        name = "parameter-combination-exec"

    specification_parameter_combination_ref: Optional[Ref] = field(
        default=None,
        metadata={
            "name": "specification-parameter-combination-ref",
            "type": "Element",
            "required": True,
        },
    )
    status: Optional[ActivityStatus] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    execution_status: Optional[ExecutionStatus] = field(
        default=None,
        metadata={
            "name": "execution-status",
            "type": "Element",
            "required": True,
        },
    )
    verdict: Optional[VerdictStatus] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    html_comment: Optional[str] = field(
        default=None,
        metadata={
            "name": "html-comment",
            "type": "Element",
            "required": True,
        },
    )
    ordering: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    uid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    tester: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    actual_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "actual-time",
            "type": "Element",
            "required": True,
        },
    )
    planned_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "planned-time",
            "type": "Element",
            "required": True,
        },
    )
    error_ids: Optional[ErrorIdRefs] = field(
        default=None,
        metadata={
            "name": "error-ids",
            "type": "Element",
            "required": True,
        },
    )
    keywords: Optional[Keywords] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    user_defined_fields: Optional[UserDefinedFields] = field(
        default=None,
        metadata={
            "name": "userDefinedFields",
            "type": "Element",
            "required": True,
        },
    )
    values: Optional[Values] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    references: Optional[References] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class ParameterCombinationSpec:
    class Meta:
        name = "parameter-combination-spec"

    pk: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    html_comment: Optional[str] = field(
        default=None,
        metadata={
            "name": "html-comment",
            "type": "Element",
            "required": True,
        },
    )
    ordering: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    uid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    keywords: Optional[Keywords] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    edited_requirements: Optional[RequirementRefs] = field(
        default=None,
        metadata={
            "name": "edited-requirements",
            "type": "Element",
            "required": True,
        },
    )
    non_edited_requirements: Optional[RequirementRefs] = field(
        default=None,
        metadata={
            "name": "non-edited-requirements",
            "type": "Element",
            "required": True,
        },
    )
    user_defined_fields: Optional[UserDefinedFields] = field(
        default=None,
        metadata={
            "name": "userDefinedFields",
            "type": "Element",
            "required": True,
        },
    )
    values: Optional[Values] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class ParameterValues:
    class Meta:
        name = "parameter-values"

    call_parameter: List[CallParameter] = field(
        default_factory=list,
        metadata={
            "name": "call-parameter",
            "type": "Element",
        },
    )


@dataclass
class Parameters:
    class Meta:
        name = "parameters"

    parameter: List[Parameter] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
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

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    testobjectname: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    state: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    customername: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    customeradress: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    contactperson: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    testlab: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    checklocation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    visible_for_testers: Optional[bool] = field(
        default=None,
        metadata={
            "name": "visibleForTesters",
            "type": "Element",
        },
    )
    startdate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    enddate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    status: Optional[ProjectStatus] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    html_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "html-description",
            "type": "Element",
            "required": True,
        },
    )
    testing_intelligence: Optional[str] = field(
        default=None,
        metadata={
            "name": "testingIntelligence",
            "type": "Element",
            "required": True,
        },
    )
    created_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "createdTime",
            "type": "Element",
            "required": True,
        },
    )
    settings: Optional[Settings] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    requirement_repositories: Optional[RequirementRepositories] = field(
        default=None,
        metadata={
            "name": "requirement-repositories",
            "type": "Element",
            "required": True,
        },
    )
    requirement_projects: Optional[RequirementProjects] = field(
        default=None,
        metadata={
            "name": "requirement-projects",
            "type": "Element",
            "required": True,
        },
    )
    requirement_udfs: Optional[RequirementUdfs] = field(
        default=None,
        metadata={
            "name": "requirement-udfs",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Representative:
    class Meta:
        name = "representative"

    pk: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    ordering: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    type_value: Optional[RepresentativeType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
        },
    )
    placeholder_ref: Optional[Ref] = field(
        default=None,
        metadata={
            "name": "placeholder-ref",
            "type": "Element",
        },
    )
    attachment_pk: Optional[str] = field(
        default=None,
        metadata={
            "name": "attachment-pk",
            "type": "Element",
        },
    )
    attachment_path: Optional[str] = field(
        default=None,
        metadata={
            "name": "attachment-path",
            "type": "Element",
        },
    )
    attachment_filename: Optional[str] = field(
        default=None,
        metadata={
            "name": "attachment-filename",
            "type": "Element",
        },
    )
    attachment_lastedited: Optional[str] = field(
        default=None,
        metadata={
            "name": "attachment-lastedited",
            "type": "Element",
        },
    )
    attachment_contentpath: Optional[str] = field(
        default=None,
        metadata={
            "name": "attachment-contentpath",
            "type": "Element",
        },
    )
    attachment_lasteditor: Optional[str] = field(
        default=None,
        metadata={
            "name": "attachment-lasteditor",
            "type": "Element",
        },
    )
    attachment_file_pk: Optional[str] = field(
        default=None,
        metadata={
            "name": "attachment-file-pk",
            "type": "Element",
        },
    )
    values: Optional[Values] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class SubdivisionVersion(TestElementVersionInfo):
    class Meta:
        name = "subdivision-version"

    element: Optional["Subdivision"] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class TestElement:
    class Meta:
        name = "test-element"

    version: Optional[TestElementVersionInfo] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    pk: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    uid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    locker: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    html_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "html-description",
            "type": "Element",
        },
    )
    history_pk: Optional[str] = field(
        default=None,
        metadata={
            "name": "historyPK",
            "type": "Element",
            "required": True,
        },
    )
    identical_version_pk: Optional[str] = field(
        default=None,
        metadata={
            "name": "identicalVersionPK",
            "type": "Element",
            "required": True,
        },
    )
    references: Optional[References] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    library_pk: Optional[str] = field(
        default=None,
        metadata={
            "name": "libraryPK",
            "type": "Element",
        },
    )
    parent_uid: Optional[str] = field(
        default=None,
        metadata={
            "name": "parentUID",
            "type": "Element",
        },
    )


@dataclass
class Userroles:
    class Meta:
        name = "userroles"

    user: List[ProjectUser] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConditionVersions:
    class Meta:
        name = "condition-versions"

    version: List[ConditionVersion] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class DatatypeVersions:
    class Meta:
        name = "datatype-versions"

    version: List[DatatypeVersion] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Instances:
    class Meta:
        name = "instances"

    instance: List[Instance] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class InteractionCall:
    class Meta:
        name = "interaction-call"

    interaction_ref: Optional[Ref] = field(
        default=None,
        metadata={
            "name": "interaction-ref",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    html_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "html-description",
            "type": "Element",
            "required": True,
        },
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    html_comment: Optional[str] = field(
        default=None,
        metadata={
            "name": "html-comment",
            "type": "Element",
            "required": True,
        },
    )
    type_value: Optional[InteractionCallType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    phase: Optional[InteractionCallPhase] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    parameter_values: Optional[ParameterValues] = field(
        default=None,
        metadata={
            "name": "parameter-values",
            "type": "Element",
            "required": True,
        },
    )
    marker: Optional[Marker] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class InteractionVersions:
    class Meta:
        name = "interaction-versions"

    version: List[InteractionVersion] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ParameterCombinationsExec:
    class Meta:
        name = "parameter-combinations-exec"

    parameter_combination: List[ParameterCombinationExec] = field(
        default_factory=list,
        metadata={
            "name": "parameter-combination",
            "type": "Element",
        },
    )


@dataclass
class ParameterCombinationsSpec:
    class Meta:
        name = "parameter-combinations-spec"

    parameter_combination: List[ParameterCombinationSpec] = field(
        default_factory=list,
        metadata={
            "name": "parameter-combination",
            "type": "Element",
        },
    )


@dataclass
class Representatives:
    class Meta:
        name = "representatives"

    representative: List[Representative] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class SubdivisionVersions:
    class Meta:
        name = "subdivision-versions"

    version: List[SubdivisionVersion] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class CallSequence:
    class Meta:
        name = "call-sequence"

    interaction_call: List[InteractionCall] = field(
        default_factory=list,
        metadata={
            "name": "interaction-call",
            "type": "Element",
        },
    )


@dataclass
class Condition(TestElement):
    class Meta:
        name = "condition"

    old_versions: Optional[ConditionVersions] = field(
        default=None,
        metadata={
            "name": "old-versions",
            "type": "Element",
        },
    )
    type_value: str = field(
        init=False,
        default="condition",
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )


@dataclass
class EquivalenceClass:
    class Meta:
        name = "equivalence-class"

    pk: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    ordering: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    default_representative_ref: Optional[Ref] = field(
        default=None,
        metadata={
            "name": "default-representative-ref",
            "type": "Element",
            "required": True,
        },
    )
    representatives: Optional[Representatives] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Execution:
    class Meta:
        name = "execution"

    testcycle_ref: Optional[Ref] = field(
        default=None,
        metadata={
            "name": "testcycle-ref",
            "type": "Element",
            "required": True,
        },
    )
    specification_ref: Optional[Ref] = field(
        default=None,
        metadata={
            "name": "specification-ref",
            "type": "Element",
            "required": True,
        },
    )
    details: Optional["ExecutionDetails"] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    execution_status: Optional[ExecutionStatus] = field(
        default=None,
        metadata={
            "name": "execution-status",
            "type": "Element",
            "required": True,
        },
    )
    verdict: Optional[VerdictStatus] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    planned_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "planned-time",
            "type": "Element",
            "required": True,
        },
    )
    actual_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "actual-time",
            "type": "Element",
            "required": True,
        },
    )
    script_path: Optional[str] = field(
        default=None,
        metadata={
            "name": "script-path",
            "type": "Element",
            "required": True,
        },
    )
    execution_engine: Optional[str] = field(
        default=None,
        metadata={
            "name": "execution-engine",
            "type": "Element",
            "required": True,
        },
    )
    protocol_location: Optional[str] = field(
        default=None,
        metadata={
            "name": "protocol-location",
            "type": "Element",
            "required": True,
        },
    )
    verdict_evaluator: Optional[str] = field(
        default=None,
        metadata={
            "name": "verdict-evaluator",
            "type": "Element",
            "required": True,
        },
    )
    comments: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    html_comments: Optional[str] = field(
        default=None,
        metadata={
            "name": "html-comments",
            "type": "Element",
            "required": True,
        },
    )
    keywords: Optional[Keywords] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    user_defined_fields: Optional[UserDefinedFields] = field(
        default=None,
        metadata={
            "name": "userDefinedFields",
            "type": "Element",
            "required": True,
        },
    )
    exec_logfiles: Optional[ExecLogfiles] = field(
        default=None,
        metadata={
            "name": "exec-logfiles",
            "type": "Element",
            "required": True,
        },
    )
    parameter_combinations: Optional[ParameterCombinationsExec] = field(
        default=None,
        metadata={
            "name": "parameter-combinations",
            "type": "Element",
        },
    )
    old_versions: Optional[OldVersions] = field(
        default=None,
        metadata={
            "name": "old-versions",
            "type": "Element",
        },
    )


@dataclass
class InstancesArray:
    class Meta:
        name = "instances-array"

    pk: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    ordering: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    instances: Optional[Instances] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Subdivision(TestElement):
    class Meta:
        name = "subdivision"

    library_information: Optional[LibraryInformation] = field(
        default=None,
        metadata={
            "name": "libraryInformation",
            "type": "Element",
        },
    )
    called_libraries: Optional[CalledLibraries] = field(
        default=None,
        metadata={
            "name": "called-libraries",
            "type": "Element",
        },
    )
    old_versions: Optional[SubdivisionVersions] = field(
        default=None,
        metadata={
            "name": "old-versions",
            "type": "Element",
        },
    )
    element: List[TestElement] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    type_value: str = field(
        init=False,
        default="subdivision",
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )


@dataclass
class EquivalenceClasses:
    class Meta:
        name = "equivalence-classes"

    equivalence_class: List[EquivalenceClass] = field(
        default_factory=list,
        metadata={
            "name": "equivalence-class",
            "type": "Element",
        },
    )


@dataclass
class ExecutionCycles:
    class Meta:
        name = "execution-cycles"

    execution: List[Execution] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class InstancesArrays:
    class Meta:
        name = "instances-arrays"

    instances_array: List[InstancesArray] = field(
        default_factory=list,
        metadata={
            "name": "instances-array",
            "type": "Element",
        },
    )


@dataclass
class Interaction(TestElement):
    class Meta:
        name = "interaction"

    status: SpecificationStatus = field(
        default=SpecificationStatus.SPECSTATUS_INPROGRESS,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    default_call_type: Optional[DefaultCallType] = field(
        default=None,
        metadata={
            "name": "default-call-type",
            "type": "Element",
            "required": True,
        },
    )
    advanced_content: Optional[AdvancedContent] = field(
        default=None,
        metadata={
            "name": "advancedContent",
            "type": "Element",
        },
    )
    preconditions: Optional[Conditions] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    postconditions: Optional[Conditions] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    parameters: Optional[Parameters] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    call_sequence: Optional[CallSequence] = field(
        default=None,
        metadata={
            "name": "call-sequence",
            "type": "Element",
            "required": True,
        },
    )
    identical_version_metaword_mapping: Optional[IdenticalVersionMetawordMapping] = field(
        default=None,
        metadata={
            "name": "identical-version-metaword-mapping",
            "type": "Element",
        },
    )
    old_versions: Optional[InteractionVersions] = field(
        default=None,
        metadata={
            "name": "old-versions",
            "type": "Element",
        },
    )
    type_value: str = field(
        init=False,
        default="interaction",
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )


@dataclass
class TestElements:
    class Meta:
        name = "test-elements"

    element: List[Subdivision] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Datatype(TestElement):
    class Meta:
        name = "datatype"

    status: Optional[SpecificationStatus] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    kind: Optional[KindOfDataType] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    fields: Optional[Fields] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    instances_arrays: Optional[InstancesArrays] = field(
        default=None,
        metadata={
            "name": "instances-arrays",
            "type": "Element",
            "required": True,
        },
    )
    equivalence_classes: Optional[EquivalenceClasses] = field(
        default=None,
        metadata={
            "name": "equivalence-classes",
            "type": "Element",
            "required": True,
        },
    )
    identical_version_datatype_mapping: Optional[IdenticalVersionDatatypeMapping] = field(
        default=None,
        metadata={
            "name": "identical-version-datatype-mapping",
            "type": "Element",
        },
    )
    old_versions: Optional[DatatypeVersions] = field(
        default=None,
        metadata={
            "name": "old-versions",
            "type": "Element",
        },
    )
    element: List[Interaction] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    type_value: str = field(
        init=False,
        default="datatype",
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )


@dataclass
class Specification:
    class Meta:
        name = "specification"

    details: Optional["SpecificationDetails"] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    html_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "html-description",
            "type": "Element",
            "required": True,
        },
    )
    review_comments: Optional[str] = field(
        default=None,
        metadata={
            "name": "review-comments",
            "type": "Element",
        },
    )
    html_review_comments: Optional[str] = field(
        default=None,
        metadata={
            "name": "html-review-comments",
            "type": "Element",
        },
    )
    keywords: Optional[Keywords] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    edited_requirements: Optional[RequirementRefs] = field(
        default=None,
        metadata={
            "name": "edited-requirements",
            "type": "Element",
            "required": True,
        },
    )
    non_edited_requirements: Optional[RequirementRefs] = field(
        default=None,
        metadata={
            "name": "non-edited-requirements",
            "type": "Element",
            "required": True,
        },
    )
    user_defined_fields: Optional[UserDefinedFields] = field(
        default=None,
        metadata={
            "name": "userDefinedFields",
            "type": "Element",
            "required": True,
        },
    )
    interaction: Optional[Interaction] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    parameter_combinations: Optional[ParameterCombinationsSpec] = field(
        default=None,
        metadata={
            "name": "parameter-combinations",
            "type": "Element",
        },
    )
    old_versions: Optional[OldVersions] = field(
        default=None,
        metadata={
            "name": "old-versions",
            "type": "Element",
        },
    )


@dataclass
class Testcase:
    class Meta:
        name = "testcase"

    pk: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    order_pos: Optional[str] = field(
        default=None,
        metadata={
            "name": "order-pos",
            "type": "Element",
            "required": True,
        },
    )
    uid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    specification: Optional[Specification] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    automation: Optional[Automation] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    execution_cycles: Optional[ExecutionCycles] = field(
        default=None,
        metadata={
            "name": "execution-cycles",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Testtheme:
    class Meta:
        name = "testtheme"

    pk: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    order_pos: Optional[str] = field(
        default=None,
        metadata={
            "name": "order-pos",
            "type": "Element",
            "required": True,
        },
    )
    uid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    specification: Optional[Specification] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    automation: Optional[Automation] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    execution_cycles: Optional[ExecutionCycles] = field(
        default=None,
        metadata={
            "name": "execution-cycles",
            "type": "Element",
            "required": True,
        },
    )
    children: Optional["TestthemeChildren"] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Version:
    class Meta:
        name = "version"

    content: List[object] = field(
        default_factory=list,
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


@dataclass
class Details:
    class Meta:
        name = "details"

    version: Optional[Version] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    pk: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    identical_version_pk: Optional[str] = field(
        default=None,
        metadata={
            "name": "identicalVersionPK",
            "type": "Element",
            "required": True,
        },
    )
    locker: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    responsible: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    reviewer: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    priority: Optional[TsePriority] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Requirement:
    class Meta:
        name = "requirement"

    pk: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    extended_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "extended-id",
            "type": "Element",
            "required": True,
        },
    )
    version: Optional[Version] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    owner: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    status: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    priority: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    repository_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "repository-id",
            "type": "Element",
            "required": True,
        },
    )
    udfs: Optional[Udfs] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class RequirementNode:
    class Meta:
        name = "requirement-node"

    requirement_pk: Optional[str] = field(
        default=None,
        metadata={
            "name": "requirement-pk",
            "type": "Element",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    version: Optional[Version] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    type_value: Optional[RequirementNodeType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    children: Optional["RequirementChildren"] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class TestthemeChildren:
    class Meta:
        name = "testtheme-children"

    testtheme: List[Testtheme] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    testcase: List[Testcase] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Testthemes:
    class Meta:
        name = "testthemes"

    testtheme: List[Testtheme] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class AutomationDetails(Details):
    class Meta:
        name = "automation-details"

    status: Optional[AutomationStatus] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    target_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "target-date",
            "type": "Element",
            "required": True,
        },
    )
    references: Optional[References] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class ExecutionDetails(Details):
    class Meta:
        name = "execution-details"

    status: Optional[ActivityStatus] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    target_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "target-date",
            "type": "Element",
            "required": True,
        },
    )
    references: Optional[References] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class RequirementChildren:
    class Meta:
        name = "requirement-children"

    requirement_node: List[RequirementNode] = field(
        default_factory=list,
        metadata={
            "name": "requirement-node",
            "type": "Element",
        },
    )


@dataclass
class Requirements:
    class Meta:
        name = "requirements"

    requirement: List[Requirement] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class SpecificationDetails(Details):
    class Meta:
        name = "specification-details"

    status: Optional[SpecificationStatus] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    target_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "target-date",
            "type": "Element",
            "required": True,
        },
    )
    references: Optional[References] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Baseline:
    class Meta:
        name = "baseline"

    details: Optional[BaselineDetails] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    children: Optional[RequirementChildren] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    project_pk_ref: Optional[Ref] = field(
        default=None,
        metadata={
            "name": "project-pk-ref",
            "type": "Element",
        },
    )
    project: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Baselines:
    class Meta:
        name = "baselines"

    baseline: List[Baseline] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Testobjectversion:
    class Meta:
        name = "testobjectversion"

    pk: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    startdate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    enddate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    status: Optional[ProjectStatus] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    created_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "createdTime",
            "type": "Element",
            "required": True,
        },
    )
    visible_for_testers: Optional[bool] = field(
        default=None,
        metadata={
            "name": "visibleForTesters",
            "type": "Element",
        },
    )
    cloning_visibility: Optional[str] = field(
        default=None,
        metadata={
            "name": "cloningVisibility",
            "type": "Element",
        },
    )
    base_tov: Optional[str] = field(
        default=None,
        metadata={
            "name": "baseTOV",
            "type": "Element",
        },
    )
    source_tov_ref: Optional[Ref] = field(
        default=None,
        metadata={
            "name": "sourceTOV-ref",
            "type": "Element",
        },
    )
    variants_definition_ref: Optional[Ref] = field(
        default=None,
        metadata={
            "name": "variantsDefinition-ref",
            "type": "Element",
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    html_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "html-description",
            "type": "Element",
            "required": True,
        },
    )
    testing_intelligence: Optional[str] = field(
        default=None,
        metadata={
            "name": "testingIntelligence",
            "type": "Element",
            "required": True,
        },
    )
    baselines: Optional[Baselines] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    placeholders: Optional[Placeholders] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    variants_definitions: Optional[VariantsDefinitions] = field(
        default=None,
        metadata={
            "name": "variantsDefinitions",
            "type": "Element",
            "required": True,
        },
    )
    variants_markers: Optional[VariantsMarkers] = field(
        default=None,
        metadata={
            "name": "variantsMarkers",
            "type": "Element",
            "required": True,
        },
    )
    placeholder_values: Optional[PlaceholderValues] = field(
        default=None,
        metadata={
            "name": "placeholderValues",
            "type": "Element",
            "required": True,
        },
    )
    testcycles: Optional[Testcycles] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    testthemes: Optional[Testthemes] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    test_elements: Optional[TestElements] = field(
        default=None,
        metadata={
            "name": "test-elements",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Testobjectversions:
    class Meta:
        name = "testobjectversions"

    testobjectversion: List[Testobjectversion] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ProjectDump:
    class Meta:
        name = "project-dump"

    details: Optional[ProjectDetails] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    userroles: Optional[Userroles] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    user_defined_fields: Optional[UserDefinedFieldsDefinition] = field(
        default=None,
        metadata={
            "name": "UserDefinedFields",
            "type": "Element",
        },
    )
    defect_user_defined_fields: Optional[DefectUserDefinedFields] = field(
        default=None,
        metadata={
            "name": "DefectUserDefinedFields",
            "type": "Element",
        },
    )
    keywords: Optional[KeywordsDefinition] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    labels: Optional[Labels] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    library_labels: Optional[LibraryLabels] = field(
        default=None,
        metadata={
            "name": "library-labels",
            "type": "Element",
        },
    )
    dm_settings: Optional[DmSettings] = field(
        default=None,
        metadata={
            "name": "dm-settings",
            "type": "Element",
        },
    )
    error_ids: Optional[ErrorIds] = field(
        default=None,
        metadata={
            "name": "error-ids",
            "type": "Element",
        },
    )
    references: Optional[References] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    requirement_baselines: Optional[Baselines] = field(
        default=None,
        metadata={
            "name": "requirement-baselines",
            "type": "Element",
        },
    )
    testobjectversions: Optional[Testobjectversions] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    requirements: Optional[Requirements] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    referenced_user_names: Optional[ReferencedUserNames] = field(
        default=None,
        metadata={
            "name": "referenced-user-names",
            "type": "Element",
        },
    )
    errors: Optional[Errors] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    warnings: Optional[Warnings] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    build_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "build-number",
            "type": "Attribute",
            "required": True,
        },
    )
    repository: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
