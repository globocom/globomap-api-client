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

from globomap_api_client.document_edge import Document
from globomap_api_client.document_edge import DocumentEdge


class DocumentEdgeTest(unittest2.TestCase):

    def tearDown(self):
        patch.stopall()

    def test_post(self):
        with patch.object(Document, 'post') as mock_method:
            doc = DocumentEdge(Mock())
            doc.post('edge_test', {'doc': 1})
            mock_method.assert_called_with(
                kind='edges', collection='edge_test', document={'doc': 1})

    def test_get(self):
        with patch.object(Document, 'get') as mock_method:
            doc = DocumentEdge(Mock())
            doc.get('edge_test', 'key1')
            mock_method.assert_called_with(
                kind='edges', collection='edge_test', key='key1')

    def test_search_many_coll(self):
        doc = DocumentEdge(Mock())
        doc.make_request = Mock()
        edges = ['edge_test1', 'edge_test2']
        query = [[{'field': 'name', 'operator': 'LIKE', 'value': 'test'}]]
        doc.search_many_coll(edges, query, 20, 2)

        params = {
            'query': json.dumps(query),
            'per_page': 20,
            'edges': edges,
            'page': 2
        }
        doc.make_request.assert_called_once_with(
            method='GET', uri='edges/search', params=params)

    def test_search(self):
        with patch.object(Document, 'search') as mock_method:
            doc = DocumentEdge(Mock())
            query = [[{'field': 'name', 'operator': 'LIKE', 'value': 'test'}]]
            doc.search('edge_test', query, 20, 2)
            mock_method.assert_called_with(
                kind='edges', collection='edge_test', query=query,
                per_page=20, page=2
            )

    def test_list(self):
        with patch.object(Document, 'list') as mock_method:
            doc = DocumentEdge(Mock())
            doc.list('edge_test', 20, 2)
            mock_method.assert_called_with(
                kind='edges', collection='edge_test', per_page=20, page=2)

    def test_put(self):
        with patch.object(Document, 'put') as mock_method:
            doc = DocumentEdge(Mock())
            doc.put('edge_test', 'key1', {'doc': 1})
            mock_method.assert_called_with(
                kind='edges', collection='edge_test',
                key='key1', document={'doc': 1}
            )

    def test_patch(self):
        with patch.object(Document, 'patch') as mock_method:
            doc = DocumentEdge(Mock())
            doc.patch('edge_test', 'key1', {'doc': 1})
            mock_method.assert_called_with(
                kind='edges', collection='edge_test',
                key='key1', document={'doc': 1}
            )

    def test_delete(self):
        with patch.object(Document, 'delete') as mock_method:
            doc = DocumentEdge(Mock())
            doc.delete('edge_test', 'key1')
            mock_method.assert_called_with(
                kind='edges', collection='edge_test', key='key1')

    def test_clear(self):
        with patch.object(Document, 'clear') as mock_method:
            doc = DocumentEdge(Mock())
            query = [[{'field': 'name', 'operator': 'LIKE', 'value': 'test'}]]
            doc.clear('edge_test', query)
            mock_method.assert_called_with(
                kind='edges', collection='edge_test', query=query
            )
