#  Copyright 2021- imbus AG
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
#  This code contains derived code from Robot Framework Core Project
#  under Apache 2.0 License.
#  https://github.com/robotframework/robotframework

import enum
import os
from datetime import datetime, timezone
from hashlib import sha1
from pathlib import Path
from typing import Dict, List, Optional, Set

from robot.libdocpkg.robotbuilder import LibraryDoc
from robot.running.arguments.argumentspec import ArgInfo
from robot.utils import XmlWriter


class ElementTypes(enum.Enum):
    """Enum for different test elements found in the imbus TestBench."""

    subdivision = 'subdivision'
    datatype = 'datatype'
    interaction = 'interaction'
    condition = 'condition'


class ProjectStates(enum.Enum):
    """Enum for different project states found in the imbus TestBench."""

    planned = 'planned'
    active = 'active'
    finished = 'finished'
    closed = 'closed'


class PKGenerator:
    """A class used to generate unique primary keys for test elements.
    Only one instance should be created and used to ensure continuous
    unique pks."""

    def __init__(self, first_pk: int = 230):
        self.pk_counter = first_pk

    def get_pk(self) -> str:
        self.pk_counter += 1
        return str(self.pk_counter)


class Element:
    """A class to represent imbus TestBench related test elements."""

    # Remember all created element objects and their associated pk.
    all_elements = {}

    def __init__(self, pk_generator: PKGenerator, name, documentation="", parent_element=None):
        self.html_desc = f"<html>{documentation}</html>"
        if parent_element:
            self.name = parent_element.name + '.' + name
        else:
            self.name = name
        # Register element for later access to element's unique pk
        self.pk = pk_generator.get_pk()
        Element.all_elements[self.name] = self.pk

    def get_name(self) -> str:
        # Returns the element's name without the parent-prefix.
        return self.name.split('.', 1)[-1]


class DataType(Element):
    """A class used to gather information for imbus TestBench
    data types from the associated Robot Framework data type.
    Each Robot Framework data type is converted into one
    "members" equivalence class and each valid value is one
    representative in the imbus TestBench."""

    def __init__(
        self, pk_generator: PKGenerator, name: str, documentation: str = "", parent_element=None
    ):
        super().__init__(pk_generator, name, documentation, parent_element)

        # Holds all enum values, typed_dics are considered to be
        # generic for imbus TestBench purposes.
        self.pk_generator = pk_generator
        self.equivalence_classes: Dict[str, Set[str]] = {}
        self.representatives = {}
        self.name = name

    def add_equivalence_class(
        self, equivalence_class_name: str, members: Optional[Set[str]] = None
    ):
        existing_eqivalence_class = self.equivalence_classes.get(equivalence_class_name)
        if not existing_eqivalence_class:
            self.equivalence_classes[equivalence_class_name] = set()
        if members:
            for member in members:
                if (Element.all_elements.get(f"{self.name}.{member}")) is None:
                    self.equivalence_classes[equivalence_class_name].add(member)
                    Element.all_elements[f"{self.name}.{member}"] = self.pk_generator.get_pk()


class Libdoc2TestBenchWriter:
    """A class to generate imbus TestBench readable xml-files from Robot Framework
    libraries.

    Methods
    -------
    write(libdoc, outfile)
        Writes the content of the libdoc in an imbus TestBench importable xml-format."""

    # Created when first evoked by self.write
    pk_generator = None

    # Values used to fill project view fields.
    testobject_state = ProjectStates.active.value
    testobject_desc = "Robot Framework Import"
    created_time = datetime.now(tz=timezone.utc).strftime('%Y-%m-%d %H:%M:%S %z')
    libdoc_name = None  # set-up in write() method.
    attachment_reference_pk = {}  # Needed for resource files - holds exactly one pk

    # Attributes used in the header of the xml-file
    xml_attributes = {'version': "3.0", 'build-number': "230202/6a0c", 'repository': "iTB_RF"}

    # Values used to fill imbus TestBench project settings.
    project_settings = {
        'overwrite-exec-responsible': 'false',
        'optional-checkin': 'false',
        'filter-sync-interval': '30',
        'ignore-not-edited': 'false',
        'ignore-not-planned': 'true',
        'designers-may-manage-baselines': 'false',
        'designers-may-import-baselines': 'false',
        'only-admins-manage-udfs': 'false',
        'variants-management-enabled': 'false',
    }

    # Values used to fill testobject version fields.
    testobjectversion_tags = {
        'pk': None,  # set-up in write() method
        'id': 'RF Import',
        'startdate': '',
        'enddate': '',
        'status': testobject_state,
        'createdTime': created_time,
        'description': 'Robot Framework Import',
        'html-description': '',
        'testingIntelligence': 'false',
        'baselines': '',
        'placeholders': '',
        'variantsDefinitions': '',
        'variantsMarkers': '',
        'placeholderValues': '',
        'testcycles': '',
        'testthemes': '',
    }

    def __init__(self, project_name='RF Import', testobject_name='RF Import'):
        self.project_name = project_name
        self.testobject_name = testobject_name

    def write(
        self,
        libraries: List,
        resources: List,
        outfile,
        repo_id: str,
        library_root: str,
        resource_root: str,
        attachment: bool,
    ):
        """Writes an imbus TestBench readable xml-file.

        Parameters
        ----------
        libraries : LibraryDocumentation lists
            List of robot.libdocpkg.LibraryDocumentation file.
        resources : LibraryDocumentation lists
            List of robot.libdocpkg.LibraryDocumentation file.
        outfile: IO
            IO stream to write files to.
        repo_id: String
            Overwrite XML-attribute in the header
        """

        # If --repository is set, overwrite xml_attribute for it.
        if repo_id:
            self.xml_attributes['repository'] = repo_id

        self.pk_generator = PKGenerator()

        self.testobjectversion_tags["pk"] = self.pk_generator.get_pk()

        writer = XmlWriter(outfile, usage='Libdoc spec')
        self._write_start(writer)
        if attachment:
            self._write_attachments(resources, writer)
        self._start_testobjectversion(writer)
        if libraries:
            self._start_root_subdivision(writer, library_root, 'Robot Framework Libraries')
            for libdoc in libraries:
                Element.all_elements = {}
                self._start_library_subdivision(libdoc, writer)
                self._write_data_types(libdoc, writer)
                self._write_interactions(libdoc, writer)
                self._end_library_subdivision(writer)
            self._end_root_subdivision(writer)
        if resources:
            self._start_root_subdivision(writer, resource_root, 'Robot Framework Resource Files')
            for libdoc in resources:
                Element.all_elements = {}
                self._start_library_subdivision(libdoc, writer)
                self._write_data_types(libdoc, writer)
                self._write_interactions(libdoc, writer, attachment)
                self._end_library_subdivision(writer)
            self._end_root_subdivision(writer)
        self._end_testobjectversion(writer)
        self._write_end(writer)

        # Return last issued primary key.
        return self.pk_generator.get_pk()

    def _write_start(self, writer):
        writer.start('project-dump', self.xml_attributes)
        writer.start('details')
        writer.element('name', self.project_name)
        writer.element('id', '')
        writer.element('testobjectname', self.testobject_name)
        writer.element('state', self.testobject_state)
        for tag in [
            'customername',
            'customeradress',
            'contactperson',
            'testlab',
            'checklocation',
            'startdate',
            'enddate',
        ]:
            writer.element(tag, '')
        writer.element('status', self.testobject_state)
        writer.element('description', self.testobject_desc)
        writer.element('html-description', '')
        writer.element('testingIntelligence', 'false')
        writer.element('createdTime', self.created_time)
        writer.start('settings')
        for key, value in self.project_settings.items():
            writer.element(key, value)
        writer.end('settings')
        for tag in ['requirement-repositories', 'requirement-projects', 'requirement-udfs']:
            writer.element(tag, '')
        writer.end('details')

        writer.element('userroles', '')
        writer.element('keywords', '')
        writer.start('labels')
        for tag in ['public', 'private']:
            writer.element(tag, '')
        writer.end('labels')

    def _write_attachments(self, resources, writer):
        writer.start('references')
        for libdoc in resources:
            writer.start('reference')
            # set-up needed reference
            self.attachment_reference_pk[libdoc.name] = self.pk_generator.get_pk()
            writer.element('pk', self.attachment_reference_pk[libdoc.name])
            writer.element('attachment-path', os.path.split(str(Path(libdoc.source).resolve()))[0])
            writer.element('filename', os.path.split(str(Path(libdoc.source).resolve()))[1])
            writer.element('type', '2')
            writer.element('version', '')
            writer.element('attachment-pk', self.pk_generator.get_pk())
            writer.element('attachment-filename', libdoc.name + '.resource')
            writer.element('attachment-file-pk', self.pk_generator.get_pk())
            writer.element('old-versions', '')
            writer.end('reference')
        writer.end('references')

    def _start_testobjectversion(self, writer):
        writer.start('testobjectversions')
        writer.start('testobjectversion')
        for key, value in self.testobjectversion_tags.items():
            writer.element(key, value)
        writer.start('test-elements')

    def _start_root_subdivision(self, writer, name, description):
        # Start RF/Resource subdivison
        writer.start('element', {'type': ElementTypes.subdivision.value})
        writer.element('pk', self.pk_generator.get_pk())
        writer.element('name', name)
        writer.element('uid', self._generate_uid('SD', name))
        writer.element('locker', '')
        writer.element('description', description)
        writer.element('html-description', '')
        writer.element('historyPK', '-1')
        writer.element('identicalVersionPK', '-1')
        writer.element('references', '')

    def _start_library_subdivision(self, libdoc, writer):
        writer.start('element', {'type': ElementTypes.subdivision.value})
        writer.element('pk', self.pk_generator.get_pk())
        writer.element('name', libdoc.name)
        writer.element('uid', self._generate_uid('SD', libdoc.name))
        writer.element('locker', '')
        writer.element(
            'html-description',
            f"<html><p> Import of {libdoc.name} {libdoc.version}</p>{libdoc.doc}</html>",
        )
        writer.element('historyPK', '-1')
        writer.element('identicalVersionPK', '-1')
        writer.element('references', '')

    def _get_argument_name_prefix(self, argument_kind: str) -> str:
        if argument_kind == ArgInfo.VAR_POSITIONAL:
            return "* "
        if argument_kind == ArgInfo.VAR_NAMED:
            return "** "
        if argument_kind == ArgInfo.NAMED_ONLY:
            return "- "
        return ""

    def _write_interactions(self, libdoc, writer, attachment=False):
        libdoc_dic = libdoc.to_dictionary()
        for keyword in libdoc_dic["keywords"]:
            writer.start('element', {'type': ElementTypes.interaction.value})
            writer.element('pk', self.pk_generator.get_pk())
            writer.element('name', keyword['name'])
            writer.element('uid', self._generate_uid('IA', keyword['name'], libdoc.name))
            writer.element('locker', '')
            writer.element('status', '3')
            writer.element(
                'html-description',
                f"<html>{keyword['doc'].replace('<br>', '<br/>').replace('<hr>', '<br>')}</html>",
            )
            writer.element('historyPK', '-1')
            writer.element('identicalVersionPK', '-1')
            writer.start('references')

            if attachment:
                writer.element(
                    'reference-ref', attrs={'pk': self.attachment_reference_pk[libdoc.name]}
                )
            writer.end('references')
            writer.start('parameters')
            for arg in keyword['args']:
                argument_kind = arg.get('kind')
                if (
                    not argument_kind
                    or argument_kind == ArgInfo.POSITIONAL_ONLY_MARKER
                    or argument_kind == ArgInfo.NOTSET
                ):
                    continue
                writer.start('parameter')
                writer.element('pk', self.pk_generator.get_pk())
                argument_name_prefix = self._get_argument_name_prefix(argument_kind)
                writer.element('name', f"{argument_name_prefix}{arg['name']}")
                type_name = self._get_datatype_name(arg)
                typ_pk = Element.all_elements.get(type_name, '-1')

                writer.element('datatype-ref', '', {'pk': typ_pk})
                writer.element('definition-type', '0')
                writer.element('use-type', '1')
                writer.element('datatype-name', type_name)
                default_value = arg.get('defaultValue')
                if default_value is None:
                    default_value = self._get_arg_kind_default_value(argument_kind)
                else:
                    writer.start('default-value', {'type': 'representative'})
                    writer.element('type', '1')
                    representative_pk = Element.all_elements.get(
                        f"{type_name}.{default_value}", '-1'
                    )
                    writer.element('representative-ref', '', {'pk': representative_pk})
                    writer.element('representative-name', default_value)
                    writer.end('default-value')
                writer.end('parameter')
            writer.end('parameters')
            writer.end('element')  # close interaction tag

    def _get_arg_kind_default_value(self, argument_kind: str) -> Optional[str]:
        if argument_kind == ArgInfo.VAR_POSITIONAL:
            return "@{EMPTY}"
        if argument_kind == ArgInfo.VAR_NAMED:
            return "&{EMPTY}"
        return None

    def _get_datatype_name(self, argument: Dict[str, str]) -> str:
        for argument_type in argument.get('typedocs', {}).values():
            if argument_type in self.enum_types or argument_type in self.typed_dicts:
                return argument_type
        return argument.get('name', "")

    def _get_datatype_documentation(self, datatype_name, libdoc_dic: Dict[str, any]) -> str:
        if datatype_name in self.enum_types:
            return next(
                filter(lambda enum: enum['name'] == datatype_name, libdoc_dic['dataTypes']['enums'])
            ).get('doc', '')
        if datatype_name in self.typed_dicts:
            return next(
                filter(
                    lambda typedDict: typedDict['name'] == datatype_name,
                    libdoc_dic['dataTypes']['typedDicts'],
                )
            ).get('doc', '')
        return ""

    def _get_enum_types(self, libdoc_dic: Dict[str, any]) -> Set[str]:
        return {enum.get('name') for enum in libdoc_dic.get('dataTypes').get('enums')}

    def _get_typed_dicts(self, libdoc_dic: Dict[str, any]) -> Set[str]:
        return {enum.get('name') for enum in libdoc_dic.get('dataTypes').get('typedDicts')}

    def _write_data_types(self, libdoc: LibraryDoc, writer):
        libdoc_dic = libdoc.to_dictionary()
        self.enum_types = set(self._get_enum_types(libdoc_dic))
        self.typed_dicts = self._get_typed_dicts(libdoc_dic)

        datatypes = {}
        keyword_arguments = [
            argument for keyword in libdoc_dic['keywords'] for argument in keyword['args']
        ]
        for argument in keyword_arguments:
            argument_kind = argument.get('kind')
            if (
                not argument_kind
                or argument_kind == ArgInfo.POSITIONAL_ONLY_MARKER
                or argument_kind == ArgInfo.NOTSET
            ):
                continue
            datatype_name = self._get_datatype_name(argument)
            datatype_documentation = self._get_datatype_documentation(datatype_name, libdoc_dic)
            datatype = datatypes.get(datatype_name) or DataType(
                self.pk_generator, datatype_name, datatype_documentation
            )
            default_value = argument.get('defaultValue')
            if default_value is None:
                default_value = self._get_arg_kind_default_value(argument_kind)
            for type_name in argument.get('typedocs', {}):
                members = set()
                if type_name == "bool":
                    members = {'True', 'False', '${True}', '${False}'}
                    datatype.add_equivalence_class(type_name, members)
                elif type_name in self.enum_types:
                    members_list = next(
                        filter(
                            lambda enum: enum['name'] == datatype_name,
                            libdoc_dic['dataTypes']['enums'],
                        )
                    ).get('members', [])
                    members = {member.get('name') for member in members_list}
                    datatype.add_equivalence_class(type_name, members)
            if default_value == "None":
                datatype.add_equivalence_class("None", {default_value})
            else:
                datatype.add_equivalence_class(datatype_name, {default_value})
            datatype.add_equivalence_class(datatype_name)
            datatypes[datatype_name] = datatype

        writer.start('element', {'type': ElementTypes.subdivision.value})
        writer.element('pk', self.pk_generator.get_pk())
        writer.element('name', '_Datatypes')
        writer.element('uid', self._generate_uid('SD', '_Datatypes', libdoc.name))
        writer.element('locker', '')
        writer.element('status', '3')
        writer.element('html-description', '')
        writer.element('historyPK', '-1')
        writer.element('identicalVersionPK', '-1')
        writer.element('references', '')

        for datatype_idx, data_type in enumerate(datatypes.values()):
            writer.start('element', {'type': ElementTypes.datatype.value})
            writer.element('pk', data_type.pk)
            writer.element('name', data_type.get_name())
            writer.element('uid', self._generate_uid('DT', data_type.name, libdoc.name))
            writer.element('locker', '')
            writer.element(
                'html-description',
                data_type.html_desc.replace('<br>', '<br/>').replace('<hr>', '<br>'),
            )
            writer.element('historyPK', '-1')
            writer.element('identicalVersionPK', '-1')
            writer.start('equivalence-classes')
            for ec_name, ec_members in data_type.equivalence_classes.items():
                writer.start('equivalence-class')
                writer.element('pk', self.pk_generator.get_pk())
                writer.element('name', ec_name)
                writer.element('description', ec_name)
                writer.element('ordering', str(1024 * datatype_idx))
                writer.start('representatives')
                default_pk = '-1'
                for idx, representative in enumerate(ec_members):
                    writer.start('representative')
                    pk = Element.all_elements[f"{data_type.get_name()}.{representative}"]
                    if idx == 0:
                        default_pk = pk
                    writer.element('pk', pk)
                    writer.element('name', representative)
                    writer.element('ordering', str(1024 * (idx + 1)))
                    writer.end('representative')
                writer.end('representatives')
                writer.element('default-representative-ref', '', {'pk': default_pk})
                writer.end('equivalence-class')
            writer.end('equivalence-classes')
            writer.end('element')  # close dataType tag
        writer.end('element')  # close datatype subdivision tag

    def _end_library_subdivision(self, writer):
        writer.end('element')  # close Library Subdivision tag

    def _end_root_subdivision(self, writer):
        writer.end('element')  # close RF or Resource subdivision tag

    def _end_testobjectversion(self, writer):
        writer.end('test-elements')
        writer.end('testobjectversion')
        writer.end('testobjectversions')

    def _write_end(self, writer):
        writer.element('requirements', '')
        writer.start('referenced-user-names')
        writer.end('referenced-user-names')
        writer.element('errors', '')
        writer.element('warnings', '')
        writer.end('project-dump')
        writer.close()

    def _generate_uid(self, element_type: str, element_name: str, lib_name: str = "") -> str:
        # UIDs format:
        # Prefix: RepositoryID-AbreviationElementType-
        # Root: first 10 characters of sha1Hash of LibraryName.ElementName
        repository_id = self.xml_attributes.get('repository', 'itb')

        # robustify element name regarding smaller changes
        element_name = element_name.replace('_', '')
        element_name = element_name.replace(' ', '')
        element_name = element_name.lower()

        prefix = f"{repository_id}-{element_type}-"
        root_hash = sha1(f"{lib_name}.{element_name}".encode()).hexdigest()[:10]
        return f"{prefix}{root_hash}"
