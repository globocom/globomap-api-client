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

from globomap_api_client.collection import Collection


class CollectionTest(unittest2.TestCase):

    def tearDown(self):
        patch.stopall()

    def test_post(self):
        collection = Collection(Mock())
        collection.make_request = Mock()
        collection.post({'doc': 1})

        collection.make_request.assert_called_once_with(
            method='POST', uri='collections', data={'doc': 1})

    def test_list(self):
        collection = Collection(Mock())
        collection.make_request = Mock()
        collection.list()

        collection.make_request.assert_called_once_with(
            method='GET', params={'per_page': 10, 'page': 1}, uri='collections')

    def test_list_with_pagination(self):
        collection = Collection(Mock())
        collection.make_request = Mock()
        collection.list(page=2, per_page=20)

        collection.make_request.assert_called_once_with(
            method='GET', params={'per_page': 20, 'page': 2}, uri='collections')

    def test_search(self):
        collection = Collection(Mock())
        collection.make_request = Mock()
        query = [[{'field': 'name', 'operator': 'LIKE', 'value': 'test'}]]
        collection.search(query=query)

        params = {
            'query': json.dumps(query),
            'per_page': 10,
            'page': 1
        }
        collection.make_request.assert_called_once_with(
            method='GET', uri='collections',
            params=params
        )

    def test_search_with_pagination(self):
        collection = Collection(Mock())
        collection.make_request = Mock()
        query = [[{'field': 'name', 'operator': 'LIKE', 'value': 'test'}]]
        collection.search(query, 20, 2)

        params = {
            'query': json.dumps(query),
            'per_page': 20,
            'page': 2
        }
        collection.make_request.assert_called_once_with(
            method='GET', uri='collections',
            params=params
        )
