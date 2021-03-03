#  Copyright 2008-2015 Nokia Networks
#  Copyright 2016-     Robot Framework Foundation
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

import os.path
import enum, json, pytz
from pygments import highlight, lexers, formatters
from datetime import datetime, tzinfo

from robot.utils import WINDOWS, XmlWriter, unicode


class Element_Types(enum.Enum):
    subdivision = 'subdivision'
    datatype = 'datatype'
    interaction = 'interaction'
    condition = 'condition'


class Project_States(enum.Enum):
    planned = 'planned'
    active = 'active'
    finished = 'finished'
    closed = 'closed'


class PK_Generator():
    def __init__(self, pk_start: int = 230):
        self.pk_counter = pk_start

    def get_pk(self):
        self.pk_counter += 1
        return str(self.pk_counter)


class Element():
    # Remember all created element objects with pks
    all_elements = {}

    def __init__(self, pk_generator: PK_Generator, element, parent_element=None):
        self.element = element
        self.pk = pk_generator.get_pk()
        self.parent = parent_element

        if element.doc:
            self.desc = element.doc
            self.html_desc = f"<HTML>{self.desc}</HTML>"

        self._set_name_and_register_in_all_elements()
        # print(self.all_elements)

    def _set_name_and_register_in_all_elements(self):
        if self.parent is None:
            self.name = self.element.name
        else:
            self.name = self.parent.name + '.' + self.element.name
        Element.all_elements[self.name] = self.pk

    def get_name(self):
        return self.name.split('.', 1)[-1]

class Data_Type(Element):

    def __init__(self, pk_generator: PK_Generator, data_type, parent_element=None):
        super().__init__(pk_generator, data_type)
        self.type = data_type.type
        self.equivalence_classes = {}

        if self.type == 'TypedDict':
            pass
            # TODO TypedDict Processing
            # print('YAY dicts')

        if self.type == 'Enum':
            # TODO Enum Processing
            self.members = data_type.members
            # print(self.members)
            for member in self.members:
                # print(member)
                key = self.name + '.' + member['name']
                value = self.name + '.' + member['value']
                self.equivalence_classes[key] = value
                Element.all_elements[key] = pk_generator.get_pk()

            # print('yay ENUMS')
            # print(self.equivalence_classes)
            #print(Element.all_elements)

# class Equivalence_Class(Element):
    
#     def __init__(self, pk_generator: PK_Generator, equivalence_class, parent_element):
#         super().__init__(pk_generator, equivalence_class)
#         self.desc = self.name.split('.')[-1])
#         self.default_representative = None
#         self.representatives = {}
#         # self.ordering
#         for representative in equivalence_class.
        

# TODO class Interaction(Element):


class Libdoc2TestBenchWriter:
    pk_generator = PK_Generator()

    project_name = 'RF Import'
    testobject_name = 'RF Import'
    testobject_state = Project_States.active.value
    testobject_desc = "RF import generated via Libdoc2TestBench.py"
    created_time = f"{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} +0000"
    print(f'createdTime: {created_time}')

    project_settings = {
        'overwrite-exec-responsible': 'false',
        'optional-checkin': 'false',
        # 'hide-exec-auto-checkin': 'false',
        'filter-sync-interval': '30',
        'ignore-not-edited': 'false',
        'ignore-not-planned': 'true',
        'designers-may-manage-baselines': 'false',
        'designers-may-import-baselines': 'false',
        'only-admins-manage-udfs': 'false',
        'variants-management-enabled': 'false'
    }

    def write(self, libdoc, outfile):
        writer = XmlWriter(outfile, usage='Libdoc spec')
        self._write_start(libdoc, writer)
        self._write_testobjectversion(libdoc, writer)
        self._write_data_types(libdoc.data_types, writer)
        self._write_interactions(libdoc.keywords, writer)
        self._write_end(writer)

    def _write_start(self, libdoc, writer):
        # generated = datetime.utcnow().replace(microsecond=0).isoformat() + 'Z'
        # attrs = {'name': libdoc.name,
        #          'type': libdoc.type,
        #          'format': libdoc.doc_format,
        #          'scope': libdoc.scope,
        #          'generated': generated,
        #          'specversion': '3'}
        # self._add_source_info(attrs, libdoc, writer.output)

        # TODO: Values for attributes - wird später benutzt um sicherzustellen, dass Importe auf spezifische Versionen der XSD und der Testbench auchbauen
        writer.start('project-dump', {
            'version': "2.6.1",
            'build-number': "201215/dcee",
            'repository': "itba"
        })
        writer.start('details')
        writer.element('name', self.project_name)
        writer.element('id', '')
        writer.element('testobjectname', self.testobject_name)
        writer.element('state', self.testobject_state)
        for tag in ['customername', 'customeradress', 'contactperson', 'testlab', 'checklocation', 'startdate', 'enddate']:
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
        writer.element('keywords', '')  # TODO: XSD choice?
        # TODO xsd <-> tb more strict public/private needs to be there
        writer.start('labels')
        for tag in ['public', 'private']:
            writer.element(tag, '')
        writer.end('labels')
        writer.element('references', '')  # TODO XSD choice?
        writer.start('testobjectversions')

    def _write_testobjectversion(self, libdoc, writer):
        testobjectversion_tags = {
            'pk': '38243',
            'id': 'RF Import',
            'startdate': '2021-03-01',
            'enddate': '',
            'status': self.testobject_state,
            'createdTime': self.created_time,
            'description': 'Robot Framework import',
            'html-description': '',
            'testingIntelligence': 'false',
            'baselines': '',
            'placeholders': '',
            'variantsDefinitions': '',
            'variantsMarkers': '',
            'placeholderValues': '',
            'testcycles': '',
            'testthemes': ''
        }

        writer.start('testobjectversion')
        for key, value in testobjectversion_tags.items():
            writer.element(key, value)

        writer.start('test-elements')
        writer.start('element', {'type': Element_Types.subdivision.value})
        writer.element('pk', self.pk_generator.get_pk())
        writer.element('name', 'RF')
        #writer.element('uid', 'itba-SD-221')
        writer.element('locker', '')
        writer.element('description', 'Robot Framework test elements import')
        writer.element('html-description', '')
        writer.element('historyPK', '221')
        writer.element('identicalVersionPK', '-1')
        writer.element('references', '')  # min occurs = 0

        writer.start('element', {'type': Element_Types.subdivision.value})
        writer.element('pk', self.pk_generator.get_pk())
        writer.element('name', libdoc.name)
        #writer.element('uid', 'itba-SD-222')
        writer.element('locker', '')
        writer.element('description', libdoc.doc)
        writer.element('html-description', '')
        writer.element('historyPK', '-1')
        writer.element('identicalVersionPK', '-1')
        writer.element('references', '')

    def _write_interactions(self, keywords, writer):
        # TODO: use class based approach instead
        # keyword = keywords[1]
        # attris = vars(keyword)
        # print(', '.join("%s: %s" % item for item in attris.items()))

        for keyword in keywords:
            writer.start('element', {'type': Element_Types.interaction.value})
            writer.element('pk', self.pk_generator.get_pk())
            writer.element('name', keyword.name)
            writer.element('locker', '')
            # writer.element('description', '')
            writer.element('html-description', '<html>'+keyword.doc+'</html>')
            # print(highlight('<html>'+keyword.doc+'</html>', lexers.HtmlLexer(), formatters.TerminalFormatter()))
            writer.element('historyPK', '-1') 
            writer.element('identicalVersionPK', '-1')
            writer.element('references', '')
            #TODO: change boilerplate code and use real parameters
            writer.start('parameters')
            for arg in keyword.args:
                writer.start('parameter')
                writer.element('pk', self.pk_generator.get_pk())
                writer.element('name', arg.name)
                typ_pk = '-1'
                for typ in arg.types_reprs:
                    typ_pk = Element.all_elements.get(typ, '-1')
                    if typ_pk != '-1':
                        break
                        
                writer.element('datatype-ref', '', {'pk': typ_pk})
                writer.element('definition-type', '0')
                writer.element('use-type', '1')
                writer.end('parameter')
            writer.end('parameters')
            #TODO #call sequence?=> interaction calls parameter-values?
            writer.end('element') # close interaction

    def _write_data_types(self, data_types, writer):
        # TODO
        datatype = data_types.enums[0]
        attris = vars(datatype)
        # print('########################################')
        # print(highlight(json.dumps(attris, indent=2), lexers.JsonLexer(), formatters.TerminalFormatter()))
        # print(', '.join("%s: %s" % item for item in attris.items()))

        datatypes = []
        if data_types.enums:
            for data_type in data_types.enums:
                datatypes.append(Data_Type(self.pk_generator, data_type))

        # TODO: typed_dicts?
        # if data_types.typed_dicts:
        #     for data_type in data_types.typed_dicts:
        #         Data_Type(self.pk_generator, data_type)

        for data_type in datatypes:
            writer.start('element', {'type': Element_Types.datatype.value})
            writer.element('pk', data_type.pk)
            writer.element('name', data_type.get_name())
            writer.element('locker', '')
            # writer.element('description', '')
            writer.element('html-description', data_type.html_desc)
            writer.element('historyPK', '-1')
            writer.element('identicalVersionPK', '-1')
            writer.start('equivalence-classes')
            writer.start('equivalence-class')   
            writer.element('pk', self.pk_generator.get_pk())
            writer.element('name', 'members')
            writer.element('description', 'Valid members')
            writer.element('ordering', '1024')
            
            writer.start('representatives')
            default_pk = '-1'
            for idx, representative in enumerate(data_type.equivalence_classes.keys()):
                writer.start('representative')
                pk = Element.all_elements[representative]
                if idx == 0:
                    default_pk = pk
                writer.element('pk', pk)
                writer.element('name', representative.split(f"{data_type.get_name()}.", 1)[-1])
                writer.element('ordering', str(1024 * idx))
                writer.end('representative')
            writer.end('representatives')
            writer.element('default-representative-ref', '', {'pk': default_pk})
            writer.end('equivalence-class')
            writer.end('equivalence-classes')
            writer.end('element') # close datatype


    # def _add_source_info(self, attrs, item, outfile, lib_source=None):
    #     if item.source and item.source != lib_source:
    #         attrs['source'] = self._format_source(item.source, outfile)
    #     if item.lineno > 0:
    #         attrs['lineno'] = str(item.lineno)

    # def _format_source(self, source, outfile):
    #     if not os.path.exists(source):
    #         return source
    #     source = os.path.normpath(source)
    #     if not (hasattr(outfile, 'name')
    #             and os.path.isfile(outfile.name)
    #             and self._on_same_drive(source, outfile.name)):
    #         return source
    #     return os.path.relpath(source, os.path.dirname(outfile.name))

    # def _on_same_drive(self, path1, path2):
    #     if not WINDOWS:
    #         return True
    #     return os.path.splitdrive(path1)[0] == os.path.splitdrive(path2)[0]

    # def _get_old_style_scope(self, libdoc):
    #     if libdoc.type == 'RESOURCE':
    #         return ''
    #     return {'GLOBAL': 'global',
    #             'SUITE': 'test suite',
    #             'TEST': 'test case'}[libdoc.scope]

    # def _write_keywords(self, list_name, kw_type, keywords, lib_source, writer):
    #     writer.start(list_name)
    #     for kw in keywords:
    #         attrs = self._get_start_attrs(kw, lib_source, writer)
    #         writer.start(kw_type, attrs)
    #         self._write_arguments(kw, writer)
    #         writer.element('doc', kw.doc)
    #         writer.element('shortdoc', kw.shortdoc)
    #         if kw_type == 'kw' and kw.tags:
    #             self._write_tags(kw.tags, writer)
    #         writer.end(kw_type)
    #     writer.end(list_name)

    # def _write_tags(self, tags, writer):
    #     writer.start('tags')
    #     for tag in tags:
    #         writer.element('tag', tag)
    #     writer.end('tags')

    # def _write_arguments(self, kw, writer):
    #     writer.start('arguments', {'repr': unicode(kw.args)})
    #     for arg in kw.args:
    #         writer.start('arg', {'kind': arg.kind,
    #                              'required': 'true' if arg.required else 'false',
    #                              'repr': unicode(arg)})
    #         if arg.name:
    #             writer.element('name', arg.name)
    #         for type_repr in arg.types_reprs:
    #             writer.element('type', type_repr)
    #         if arg.default is not arg.NOTSET:
    #             writer.element('default', arg.default_repr)
    #         writer.end('arg')
    #     writer.end('arguments')

    # def _get_start_attrs(self, kw, lib_source, writer):
    #     attrs = {'name': kw.name}
    #     if kw.deprecated:
    #         attrs['deprecated'] = 'true'
    #     self._add_source_info(attrs, kw, writer.output, lib_source)
    #     return attrs

    # def _write_data_types(self, data_types, writer):
    #     writer.start('datatypes')
    #     if data_types.enums:
    #         writer.start('enums')
    #         for enum in data_types.enums:
    #             writer.start('enum', {'name': enum.name})
    #             writer.element('doc', enum.doc)
    #             writer.start('members')
    #             for member in enum.members:
    #                 writer.element('member', attrs=member)
    #             writer.end('members')
    #             writer.end('enum')
    #         writer.end('enums')
    #     if data_types.typed_dicts:
    #         writer.start('typeddicts')
    #         for typ_dict in data_types.typed_dicts:
    #             writer.start('typeddict', {'name': typ_dict.name})
    #             writer.element('doc', typ_dict.doc)
    #             writer.start('items')
    #             for item in typ_dict.items:
    #                 if item['required'] is None:
    #                     item.pop('required')
    #                 elif item['required']:
    #                     item['required'] = 'true'
    #                 else:
    #                     item['required'] = 'false'
    #                 writer.element('item', attrs=item)
    #             writer.end('items')
    #             writer.end('typeddict')
    #         writer.end('typeddicts')
    #     writer.end('datatypes')

    def _write_end(self, writer):
        writer.end('element')  # close Library Subdivision
        writer.end('element')  # close RF Subdivision
        writer.end('test-elements')
        writer.end('testobjectversion')
        writer.end('testobjectversions')
        writer.element('requirements', '')
        writer.start('referenced-user-names')
        writer.end('referenced-user-names')
        writer.element('errors', '')
        writer.element('warnings', '')
        writer.end('project-dump')
        writer.close()
