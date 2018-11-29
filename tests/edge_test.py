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

from globomap_api_client.edge import Edge


class EdgeTest(unittest2.TestCase):

    def tearDown(self):
        patch.stopall()

    def test_post(self):
        edge = Edge(Mock())
        edge.make_request = Mock()
        edge.post({'doc': 1})

        edge.make_request.assert_called_once_with(
            method='POST', uri='edges', data={'doc': 1})

    def test_list(self):
        edge = Edge(Mock())
        edge.make_request = Mock()
        edge.list()

        edge.make_request.assert_called_once_with(
            method='GET', params={'per_page': 10, 'page': 1}, uri='edges')

    def test_list_with_pagination(self):
        edge = Edge(Mock())
        edge.make_request = Mock()
        edge.list(page=2, per_page=20)

        edge.make_request.assert_called_once_with(
            method='GET', params={'per_page': 20, 'page': 2}, uri='edges')

    def test_search(self):
        edge = Edge(Mock())
        edge.make_request = Mock()
        query = [[{'field': 'name', 'operator': 'LIKE', 'value': 'test'}]]
        edge.search(query=query)

        params = {
            'query': json.dumps(query),
            'per_page': 10,
            'page': 1
        }
        edge.make_request.assert_called_once_with(
            method='GET', uri='edges',
            params=params
        )

    def test_search_with_pagination(self):
        edge = Edge(Mock())
        edge.make_request = Mock()
        query = [[{'field': 'name', 'operator': 'LIKE', 'value': 'test'}]]
        edge.search(query, 20, 2)

        params = {
            'query': json.dumps(query),
            'per_page': 20,
            'page': 2
        }
        edge.make_request.assert_called_once_with(
            method='GET', uri='edges',
            params=params
        )
