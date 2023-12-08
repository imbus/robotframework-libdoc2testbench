from typing import List, Optional, Union

from libdoc2testbench.project_dump_model.itb_project_export import (
    Baselines,
    BinaryDigit,
    CallSequence,
    Conditions,
    Datatype,
    DefaultCallType,
    DefaultCallTypeName,
    EquivalenceClass,
    EquivalenceClasses,
    Fields,
    InstancesArrays,
    Interaction,
    OldVersions,
    Parameters,
    Placeholders,
    PlaceholderValues,
    ProjectDetails,
    ProjectDump,
    ProjectStatus,
    Ref,
    Reference,
    ReferenceKind,
    References,
    Representative,
    Representatives,
    RequirementProjects,
    RequirementRepositories,
    RequirementUdfs,
    Settings,
    SpecificationStatus,
    Subdivision,
    Testcycles,
    TestElement,
    TestElements,
    Testobjectversion,
    Testobjectversions,
    Testthemes,
    Values,
    VariantsDefinitions,
    VariantsMarkers,
)


def create_subdivision(
    name: str,
    uid: str,
    pk: str,
    locker: str = "",
    description: str = "",
    html_description: str = "",
    history_pk: str = "-1",
    identical_version_pk: str = "-1",
    references: Union[References, None] = None,
    element: Optional[List[TestElement]] = None,
) -> Subdivision:
    if element is None:
        element = []
    return Subdivision(
        name=name,
        uid=uid,
        pk=pk,
        locker=locker,
        description=description,
        html_description=html_description,
        history_pk=history_pk,
        identical_version_pk=identical_version_pk,
        references=references,
        element=element,
    )


def create_interaction(
    name: str,
    pk: str,
    uid: str,
    locker: str = "",
    description: str = "",
    history_pk: str = "-1",
    identical_version_pk: str = "-1",
    status: SpecificationStatus = SpecificationStatus.SPECSTATUS_INPROGRESS,
    default_call_type: DefaultCallType = DefaultCallType(
        name=DefaultCallTypeName.FLOW, value=BinaryDigit.FLOW
    ),
    preconditions: Conditions = Conditions(),
    postconditions: Conditions = Conditions(),
    parameters: Parameters = Parameters(),
    call_sequence: CallSequence = CallSequence(),
    references: References = References(),
) -> Interaction:
    return Interaction(
        name=name,
        pk=pk,
        uid=uid,
        locker=locker,
        description=description,
        history_pk=history_pk,
        identical_version_pk=identical_version_pk,
        status=status,
        default_call_type=default_call_type,
        preconditions=preconditions,
        postconditions=postconditions,
        parameters=parameters,
        call_sequence=call_sequence,
        references=references,
    )


def create_representative(
    pk: str, name: str, ordering: str, values: Values = Values()
) -> Representative:
    return Representative(pk=pk, name=name, ordering=ordering, values=values)


def create_equivalence_class(
    pk: str,
    name: str,
    ordering: str,
    default_representative_ref: Ref,
    description: str = "",
    representatives: Representatives = Representatives(),
) -> EquivalenceClass:
    return EquivalenceClass(
        pk=pk,
        name=name,
        description=description,
        ordering=ordering,
        default_representative_ref=default_representative_ref,
        representatives=representatives,
    )


def create_datatype(
    name: str,
    pk: str,
    uid: str,
    locker: str = "",
    description: str = "",
    history_pk: str = "-1",
    identical_version_pk: str = "-1",
    status: SpecificationStatus = SpecificationStatus.SPECSTATUS_INPROGRESS,
    fields: Fields = Fields(),
    instances_arrays: InstancesArrays = InstancesArrays(),
    equivalence_classes: EquivalenceClasses = EquivalenceClasses(),
) -> Datatype:
    return Datatype(
        name=name,
        pk=pk,
        uid=uid,
        locker=locker,
        description=description,
        history_pk=history_pk,
        identical_version_pk=identical_version_pk,
        status=status,
        fields=fields,
        instances_arrays=instances_arrays,
        equivalence_classes=equivalence_classes,
    )


def create_settings(
    overwrite_exec_responsible: bool = False,
    optional_checkin: bool = False,
    filter_sync_interval: int = 30,
    ignore_not_edited: bool = False,
    ignore_not_planned: bool = True,
    designers_may_manage_baselines: bool = False,
    designers_may_import_baselines: bool = False,
    only_admins_manage_udfs: bool = False,
    variants_management_enabled: bool = False,
) -> Settings:
    return Settings(
        overwrite_exec_responsible=overwrite_exec_responsible,
        optional_checkin=optional_checkin,
        filter_sync_interval=filter_sync_interval,
        ignore_not_edited=ignore_not_edited,
        ignore_not_planned=ignore_not_planned,
        designers_may_manage_baselines=designers_may_manage_baselines,
        designers_may_import_baselines=designers_may_import_baselines,
        only_admins_manage_udfs=only_admins_manage_udfs,
        variants_management_enabled=variants_management_enabled,
    )


def create_project_details(
    name: str,
    testobjectname: str,
    html_description: str = "",
    description: str = "",
    created_time: str = "",
    id: str = "",
    state: str = "active",
    customername: str = "",
    customeradress: str = "",
    contactperson: str = "",
    testlab: str = "",
    checklocation: str = "",
    startdate: str = "",
    enddate: str = "",
    status: ProjectStatus = ProjectStatus.ACTIVE,
    testing_intelligence: str = "false",
    settings: Settings = create_settings(),
    requirement_repositories: RequirementRepositories = RequirementRepositories(),
    requirement_projects: RequirementProjects = RequirementProjects(),
    requirement_udfs: RequirementUdfs = RequirementUdfs(),
) -> ProjectDetails:
    return ProjectDetails(
        name=name,
        id=id,
        testobjectname=testobjectname,
        state=state,
        customername=customername,
        customeradress=customeradress,
        contactperson=contactperson,
        testlab=testlab,
        checklocation=checklocation,
        startdate=startdate,
        enddate=enddate,
        status=status,
        description=description,
        html_description=html_description,
        testing_intelligence=testing_intelligence,
        created_time=created_time,
        settings=settings,
        requirement_repositories=requirement_repositories,
        requirement_projects=requirement_projects,
        requirement_udfs=requirement_udfs,
    )


def create_testobjecversion(
    pk: str,
    id: str = "",
    startdate: str = "",
    enddate: str = "",
    status: ProjectStatus = ProjectStatus.ACTIVE,
    created_time: str = "",
    description: str = "",
    html_description: str = "",
    testing_intelligence: str = "",
    baselines: Baselines = Baselines(),
    placeholders: Placeholders = Placeholders(),
    variants_definitions: VariantsDefinitions = VariantsDefinitions(),
    variants_markers: VariantsMarkers = VariantsMarkers(),
    placeholder_values: PlaceholderValues = PlaceholderValues(),
    testcycles: Testcycles = Testcycles(),
    testthemes: Testthemes = Testthemes(),
    test_elements: TestElements = TestElements(),
) -> Testobjectversion:
    return Testobjectversion(
        pk=pk,
        id=id,
        startdate=startdate,
        enddate=enddate,
        status=status,
        created_time=created_time,
        description=description,
        html_description=html_description,
        testing_intelligence=testing_intelligence,
        baselines=baselines,
        placeholders=placeholders,
        variants_definitions=variants_definitions,
        variants_markers=variants_markers,
        placeholder_values=placeholder_values,
        testcycles=testcycles,
        testthemes=testthemes,
        test_elements=test_elements,
    )


def create_reference(
    pk: str,
    filename: str,
    attachment_pk: Union[str, None],
    attachment_path: Union[str, None],
    attachment_filename: Union[str, None],
    attachment_file_pk: Union[str, None],
    type_value: ReferenceKind = ReferenceKind.LINK,
    version: str = "",
    old_versions: Optional[OldVersions] = None,
) -> Reference:
    return Reference(
        pk=pk,
        filename=filename,
        attachment_pk=attachment_pk,
        attachment_path=attachment_path,
        attachment_filename=attachment_filename,
        attachment_file_pk=attachment_file_pk,
        type_value=type_value,
        version=version,
        old_versions=old_versions,
    )


def create_project_dump(
    repository: str,
    details: ProjectDetails,
    testobjectversions: Testobjectversions = Testobjectversions(),
    version: str = "",
    build_number: str = "",
    references: Union[References, None] = None,
) -> ProjectDump:
    return ProjectDump(
        details=details,
        testobjectversions=testobjectversions,
        version=version,
        build_number=build_number,
        repository=repository,
        references=references,
    )
