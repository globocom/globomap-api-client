from globomap_api_client.document import Document


class DocumentCollection(Document):

    kind = 'collections'

    def post(self, collection, document):
        return super(DocumentCollection, self).post(
            kind=self.kind, collection=collection, document=document)

    def get(self, collection, key):
        return super(DocumentCollection, self).get(
            kind=self.kind, collection=collection, key=key)

    def search_many_coll(self, collections, query=None, per_page=10, page=1):
        uri = '{}/search'.format(self.kind)
        params = {
            'query': query,
            'per_page': per_page,
            'collections': collections,
            'page': page
        }
        return self.make_request(method='GET', uri=uri, params=params)

    def search(self, collection, query=None, per_page=10, page=1):
        return super(DocumentCollection, self).search(
            kind=self.kind, collection=collection, query=None, per_page=10, page=1)

    def list(self, collection, per_page=10, page=1):
        return super(DocumentCollection, self).list(
            kind=self.kind, collection=collection, per_page=10, page=1)

    def put(self, collection, key, document):
        return super(DocumentCollection, self).put(
            kind=self.kind, collection=collection, key=key, document=document)

    def patch(self, collection, key, document):
        return super(DocumentCollection, self).patch(
            kind=self.kind, collection=collection, key=key, document=document)

    def delete(self, collection, key):
        return super(DocumentCollection, self).delete(
            kind=self.kind, collection=collection, key=key)