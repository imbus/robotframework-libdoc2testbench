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
from datetime import datetime

from robot.utils import WINDOWS, XmlWriter, unicode


class PK_Generator():
    def __init__(self, pk_start: int = 230):
        self.pk_counter = pk_start
    # TODO: maybe insert here logic to get pk for specific objects

    def get_pk(self):
        self.pk_counter += 1
        return str(self.pk_counter)

class Libdoc2TestBenchWriter:
    pk_generator = PK_Generator()

    project_name = 'RF Import'
    testobject_name = 'RF Import'
    testobject_state = 'planned'
    created_time = '2021-03-20 09:29:29' #TODO: datetime.now

    project_settings = {
            'overwrite-exec-responsible': 'false',
            'optional-checkin': 'false',
            #'hide-exec-auto-checkin': 'false',
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
        # self._write_keywords('inits', 'init', libdoc.inits, libdoc.source, writer)
        # self._write_keywords('keywords', 'kw', libdoc.keywords, libdoc.source, writer)
        # self._write_data_types(libdoc.data_types, writer)
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

        #TODO: Values for attributes
        writer.start('project-dump', {
            'version': "2.6.1",
            'build-number': "201215/dcee",
            'repository': "itba"
        })
        writer.start('details')
        writer.element('name', self.project_name)
        writer.element('id', '')
        writer.element('testobjectname', self.testobject_name)
        writer.element('state', self.testobject_state) # planned, active, finished, closed
        for tag in ['customername', 'customeradress', 'contactperson', 'testlab', 'checklocation']:
            writer.element(tag, '')
        #writer.element('visibleForTesters', 'true')
        for tag in ['startdate', 'enddate']:
            writer.element(tag, '')
        writer.element('status', 'planned')
        writer.element('description', '')
        writer.element('html-description', '&#60;html&#62;&#60;body&#62;&#60;/body&#62;&#60;/html&#62;')
        writer.element('testingIntelligence', 'false')
        writer.element('createdTime', self.created_time)
        writer.start('settings')
        for key, value in self.project_settings.items():
            writer.element(key, value)
        writer.end('settings')
        for tag in ['requirement-repositories', 'requirement-projects', 'requirement-udfs']: #TODO: check minoccurs
            writer.element(tag, '')
        writer.end('details')
        for tag in ['userroles', 'UserDefinedFields', 'DefectUserDefinedFields']: #TODO: check minoccurs
            writer.element(tag, '')
        
        writer.element('keywords', '') #TODO: xsd fault?
        writer.start('labels') #TODO xsd <-> tb more strict
        for tag in ['public', 'private']:
            writer.element(tag, '')
        writer.end('labels')
        writer.element('references', '') #TODO xsd fault?
        writer.start('testobjectversions')
        
        #writer.start('keywordspec', attrs)
        #writer.element('version', libdoc.version)
        #writer.element('doc', libdoc.doc)
        #self._write_tags(libdoc.all_tags, writer)
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
        #TODO: Use model to insert values here!
        writer.start('element', {'type': 'subdivision'})
        writer.element('pk', self.pk_generator.get_pk())
        writer.element('name', 'RF')
        #writer.element('uid', 'itba-SD-221')
        writer.element('locker', '') #TODO:default value? ''
        writer.element('description', 'Robot Framework test elements import')
        writer.element('html-description', '&#60;html&#62;&#60;body&#62;&#60;/body&#62;&#60;/html&#62;')
        writer.element('historyPK', '221')
        writer.element('identicalVersionPK', '-1')
        writer.element('references', '')

        writer.start('element', {'type': 'subdivision'})
        writer.element('name', 'Neue Subdivision')
        writer.element('pk', self.pk_generator.get_pk())
        #writer.element('uid', 'itba-SD-222')
        writer.element('locker', '') #TODO:default value? '' 
        writer.element('description', '')
        writer.element('html-description', '&#60;html&#62;&#60;body&#62;&#60;/body&#62;&#60;/html&#62;')
        writer.element('historyPK', '222')
        writer.element('identicalVersionPK', '-1')
        writer.element('references', '')


    def _add_source_info(self, attrs, item, outfile, lib_source=None):
        if item.source and item.source != lib_source:
            attrs['source'] = self._format_source(item.source, outfile)
        if item.lineno > 0:
            attrs['lineno'] = str(item.lineno)

    def _format_source(self, source, outfile):
        if not os.path.exists(source):
            return source
        source = os.path.normpath(source)
        if not (hasattr(outfile, 'name')
                and os.path.isfile(outfile.name)
                and self._on_same_drive(source, outfile.name)):
            return source
        return os.path.relpath(source, os.path.dirname(outfile.name))

    def _on_same_drive(self, path1, path2):
        if not WINDOWS:
            return True
        return os.path.splitdrive(path1)[0] == os.path.splitdrive(path2)[0]

    def _get_old_style_scope(self, libdoc):
        if libdoc.type == 'RESOURCE':
            return ''
        return {'GLOBAL': 'global',
                'SUITE': 'test suite',
                'TEST': 'test case'}[libdoc.scope]

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

    def _write_tags(self, tags, writer):
        writer.start('tags')
        for tag in tags:
            writer.element('tag', tag)
        writer.end('tags')

    def _write_arguments(self, kw, writer):
        writer.start('arguments', {'repr': unicode(kw.args)})
        for arg in kw.args:
            writer.start('arg', {'kind': arg.kind,
                                 'required': 'true' if arg.required else 'false',
                                 'repr': unicode(arg)})
            if arg.name:
                writer.element('name', arg.name)
            for type_repr in arg.types_reprs:
                writer.element('type', type_repr)
            if arg.default is not arg.NOTSET:
                writer.element('default', arg.default_repr)
            writer.end('arg')
        writer.end('arguments')

    def _get_start_attrs(self, kw, lib_source, writer):
        attrs = {'name': kw.name}
        if kw.deprecated:
            attrs['deprecated'] = 'true'
        self._add_source_info(attrs, kw, writer.output, lib_source)
        return attrs

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
