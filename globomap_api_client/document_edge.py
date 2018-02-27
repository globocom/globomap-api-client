from globomap_api_client.document import Document


class DocumentEdge(Document):

    kind = 'edges'

    def post(self, edge, document):
        return super(DocumentEdge, self).post(
            kind=self.kind, edge=edge, document=document)

    def get(self, edge, key):
        return super(DocumentEdge, self).get(
            kind=self.kind, edge=edge, key=key)

    def search_many_coll(self, edges, query=None, per_page=10, page=1):
        uri = '{}/search'.format(self.kind)
        params = {
            'query': query,
            'per_page': per_page,
            'edges': edges,
            'page': page
        }
        return self.make_request(method='GET', uri=uri, params=params)

    def search(self, edge, query=None, per_page=10, page=1):
        return super(DocumentEdge, self).search(
            kind=self.kind, edge=edge, query=None, per_page=10, page=1)

    def list(self, edge, per_page=10, page=1):
        return super(DocumentEdge, self).list(
            kind=self.kind, edge=edge, per_page=10, page=1)

    def put(self, edge, key, document):
        return super(DocumentEdge, self).put(
            kind=self.kind, edge=edge, key=key, document=document)

    def patch(self, edge, key, document):
        return super(DocumentEdge, self).patch(
            kind=self.kind, edge=edge, key=key, document=document)

    def delete(self, edge, key):
        return super(DocumentEdge, self).delete(
            kind=self.kind, edge=edge, key=key)
