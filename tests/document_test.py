"""
   Copyright 2018 Globo.com

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""
import json
from unittest.mock import Mock
from unittest.mock import patch

import unittest2

from globomap_api_client.document import Document


class DocumentTest(unittest2.TestCase):

    def tearDown(self):
        patch.stopall()

    def test_post(self):
        doc = Document(Mock())
        doc.make_request = Mock()
        doc.post('collections', 'collection_test', {'doc': 1})

        doc.make_request.assert_called_once_with(
            method='POST', uri='collections/collection_test/', data={'doc': 1})

    def test_get(self):
        doc = Document(Mock())
        doc.make_request = Mock()
        doc.get('collections', 'collection_test', 'key1')

        doc.make_request.assert_called_once_with(
            method='GET', uri='collections/collection_test/key1')

    def test_search(self):
        doc = Document(Mock())
        doc.make_request = Mock()
        query = [[{'field': 'name', 'operator': 'LIKE', 'value': 'test'}]]
        doc.search('collections', 'collection_test', query, 20, 2)

        params = {
            'query': json.dumps(query),
            'per_page': 20,
            'page': 2
        }
        doc.make_request.assert_called_once_with(
            method='GET', uri='collections/collection_test',
            params=params
        )

    def test_list(self):
        doc = Document(Mock())
        doc.make_request = Mock()
        doc.list('collections', 'collection_test', 20, 2)
        params = {
            'per_page': 20,
            'page': 2
        }
        doc.make_request.assert_called_once_with(
            method='GET', uri='collections/collection_test', params=params)

    def test_put(self):
        doc = Document(Mock())
        doc.make_request = Mock()
        doc.put('collections', 'collection_test', 'key1', {'doc': 1})

        doc.make_request.assert_called_once_with(
            method='PUT', uri='collections/collection_test/key1/', data={'doc': 1})

    def test_patch(self):
        doc = Document(Mock())
        doc.make_request = Mock()
        doc.patch('collections', 'collection_test', 'key1', {'doc': 1})

        doc.make_request.assert_called_once_with(
            method='PATCH', uri='collections/collection_test/key1/', data={'doc': 1})

    def test_delete(self):
        doc = Document(Mock())
        doc.make_request = Mock()
        doc.delete('collections', 'collection_test', 'key1')

        doc.make_request.assert_called_once_with(
            method='DELETE', uri='collections/collection_test/key1/')

    def test_clear(self):
        doc = Document(Mock())
        doc.make_request = Mock()
        query = [[{'field': 'name', 'operator': 'LIKE', 'value': 'test'}]]
        doc.clear('collections', 'collection_test', query)

        doc.make_request.assert_called_once_with(
            method='POST', uri='collections/collection_test/clear/', data=query
        )
