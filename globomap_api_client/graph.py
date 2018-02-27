from globomap_api_client.base import Base


class Graph(Base):

    def post(self, document):
        return self.make_request(method='POST', uri='graphs', data=document)

    def list(self):
        return self.make_request(method='GET', uri='graphs')

    def traversal(self, graph, start_vertex, **kwargs):
        uri = 'graphs/{}/traversal/'.format(graph)
        params = {
            'start_vertex': start_vertex,
        }

        keys = ('item_order', 'strategy', 'order', 'edge_uniqueness',
                'vertex_uniqueness', 'max_iter', 'min_depth', 'max_depth',
                'init_func', 'sort_func', 'filter_func', 'visitor_func',
                'expander_func'
                )
        for kw in kwargs:
            if kw in keys:
                params[kw] = kwargs[kw]

        return self.make_request(method='GET', uri=uri, params=params)
