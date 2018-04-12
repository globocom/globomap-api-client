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

from globomap_api_client.document_collection import Document
from globomap_api_client.document_collection import DocumentCollection


class DocumentCollectionTest(unittest2.TestCase):

    def tearDown(self):
        patch.stopall()

    def test_post(self):
        with patch.object(Document, 'post') as mock_method:
            doc = DocumentCollection(Mock())
            doc.post('collection_test', {'doc': 1})
            mock_method.assert_called_with(
                kind='collections', collection='collection_test', document={'doc': 1})

    def test_get(self):
        with patch.object(Document, 'get') as mock_method:
            doc = DocumentCollection(Mock())
            doc.get('collection_test', 'key1')
            mock_method.assert_called_with(
                kind='collections', collection='collection_test', key='key1')

    def test_search_many_coll(self):
        doc = DocumentCollection(Mock())
        doc.make_request = Mock()
        collections = ['collection_test1', 'collection_test2']
        query = [[{'field': 'name', 'operator': 'LIKE', 'value': 'test'}]]
        doc.search_many_coll(collections, query, 20, 2)

        params = {
            'query': json.dumps(query),
            'per_page': 20,
            'collections': collections,
            'page': 2
        }
        doc.make_request.assert_called_once_with(
            method='GET', uri='collections/search', params=params)

    def test_search(self):
        with patch.object(Document, 'search') as mock_method:
            doc = DocumentCollection(Mock())
            query = [[{'field': 'name', 'operator': 'LIKE', 'value': 'test'}]]
            doc.search('collection_test', query, 20, 2)
            mock_method.assert_called_with(
                kind='collections', collection='collection_test', query=query,
                per_page=20, page=2
            )

    def test_list(self):
        with patch.object(Document, 'list') as mock_method:
            doc = DocumentCollection(Mock())
            doc.list('collection_test', 20, 2)
            mock_method.assert_called_with(
                kind='collections', collection='collection_test', per_page=20, page=2)

    def test_put(self):
        with patch.object(Document, 'put') as mock_method:
            doc = DocumentCollection(Mock())
            doc.put('collection_test', 'key1', {'doc': 1})
            mock_method.assert_called_with(
                kind='collections', collection='collection_test',
                key='key1', document={'doc': 1}
            )

    def test_patch(self):
        with patch.object(Document, 'patch') as mock_method:
            doc = DocumentCollection(Mock())
            doc.patch('collection_test', 'key1', {'doc': 1})
            mock_method.assert_called_with(
                kind='collections', collection='collection_test',
                key='key1', document={'doc': 1}
            )

    def test_delete(self):
        with patch.object(Document, 'delete') as mock_method:
            doc = DocumentCollection(Mock())
            doc.delete('collection_test', 'key1')
            mock_method.assert_called_with(
                kind='collections', collection='collection_test', key='key1')

    def test_clear(self):
        with patch.object(Document, 'clear') as mock_method:
            doc = DocumentCollection(Mock())
            query = [[{'field': 'name', 'operator': 'LIKE', 'value': 'test'}]]
            doc.clear('collection_test', query)
            mock_method.assert_called_with(
                kind='collections', collection='collection_test', query=query
            )
