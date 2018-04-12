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
from unittest.mock import Mock
from unittest.mock import patch

import unittest2

from globomap_api_client.graph import Graph


class GraphTest(unittest2.TestCase):

    def tearDown(self):
        patch.stopall()

    def test_post(self):
        graph = Graph(Mock())
        graph.make_request = Mock()
        graph.post({'doc': 1})

        graph.make_request.assert_called_once_with(
            method='POST', uri='graphs', data={'doc': 1})

    def test_list(self):
        graph = Graph(Mock())
        graph.make_request = Mock()
        graph.list()

        graph.make_request.assert_called_once_with(method='GET', uri='graphs')

    def test_traversal(self):
        graph = Graph(Mock())
        graph.make_request = Mock()
        graph.traversal('graph_test', 'collection_test/key1')

        graph.make_request.assert_called_once_with(
            method='GET', params={'start_vertex': 'collection_test/key1'},
            uri='graphs/graph_test/traversal/'
        )

    def test_traversal_with_kwargs(self):
        graph = Graph(Mock())
        graph.make_request = Mock()
        kwargs = {
            'item_order': 'forward',
            'strategy': 'dfs',
            'order': 'preorder',
            'edge_uniqueness': 'global',
            'vertex_uniqueness': 'global',
            'max_iter': '0',
            'min_depth': '1',
            'max_depth': '2',
            'init_func': 'init_func',
            'sort_func': 'sort_func',
            'filter_func': 'filter_func',
            'visitor_func': 'visitor_func',
            'expander_func': 'expander_func'
        }
        graph.traversal('graph_test', 'collection_test/key1', **kwargs)
        params = {'start_vertex': 'collection_test/key1'}
        params.update(kwargs)
        graph.make_request.assert_called_once_with(
            method='GET', params=params, uri='graphs/graph_test/traversal/')

    def test_traversal_with_kwargs_invalid(self):
        graph = Graph(Mock())
        graph.make_request = Mock()
        kwargs = {
            'invalid_param': 'invalid_param',
        }
        graph.traversal('graph_test', 'collection_test/key1', **kwargs)
        graph.make_request.assert_called_once_with(
            method='GET', params={'start_vertex': 'collection_test/key1'},
            uri='graphs/graph_test/traversal/'
        )
