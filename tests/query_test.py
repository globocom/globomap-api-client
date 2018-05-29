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

from globomap_api_client.query import Query


class QueryTest(unittest2.TestCase):

    def tearDown(self):
        patch.stopall()

    def test_post(self):
        query_doc = Query(Mock())
        query_doc.make_request = Mock()
        query_doc.post({'query_doc': 1})

        query_doc.make_request.assert_called_once_with(
            method='POST', uri='queries/', data={'query_doc': 1})

    def test_get(self):
        query_doc = Query(Mock())
        query_doc.make_request = Mock()
        query_doc.get('key1')

        query_doc.make_request.assert_called_once_with(
            method='GET', uri='queries/key1')

    def test_search(self):
        query_doc = Query(Mock())
        query_doc.make_request = Mock()
        query = [[{'field': 'name', 'operator': 'LIKE', 'value': 'test'}]]
        query_doc.search(query, 20, 2)

        params = {
            'query': json.dumps(query),
            'per_page': 20,
            'page': 2
        }
        query_doc.make_request.assert_called_once_with(
            method='GET', uri='queries/', params=params)

    def test_list(self):
        query_doc = Query(Mock())
        query_doc.make_request = Mock()
        query_doc.list()
        params = {
            'per_page': 10,
            'page': 1
        }
        query_doc.make_request.assert_called_once_with(
            method='GET', uri='queries/', params=params)

    def test_search_with_pagination(self):
        query_doc = Query(Mock())
        query_doc.make_request = Mock()
        query = [[{'field': 'name', 'operator': 'LIKE', 'value': 'test'}]]
        query_doc.search(query)

        params = {
            'query': json.dumps(query),
            'per_page': 10,
            'page': 1
        }
        query_doc.make_request.assert_called_once_with(
            method='GET', uri='queries/',
            params=params
        )

    def test_list_with_pagination(self):
        query_doc = Query(Mock())
        query_doc.make_request = Mock()
        query_doc.list(20, 2)
        params = {
            'per_page': 20,
            'page': 2
        }
        query_doc.make_request.assert_called_once_with(
            method='GET', uri='queries/', params=params)

    def test_put(self):
        query_doc = Query(Mock())
        query_doc.make_request = Mock()
        query_doc.put('key1', {'query_doc': 1})

        query_doc.make_request.assert_called_once_with(
            method='PUT', uri='queries/key1/', data={'query_doc': 1})

    def test_delete(self):
        query_doc = Query(Mock())
        query_doc.make_request = Mock()
        query_doc.delete('key1')

        query_doc.make_request.assert_called_once_with(
            method='DELETE', uri='queries/key1/')

    def test_execute(self):
        query_doc = Query(Mock())
        query_doc.make_request = Mock()
        query_doc.execute('key1')

        query_doc.make_request.assert_called_once_with(
            method='GET', uri='queries/key1/execute/')
