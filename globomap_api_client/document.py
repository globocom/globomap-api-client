from globomap_api_client.base import Base


class Document(Base):

    def post(self, kind, collection, document):
        uri = '{}/{}'.format(kind, collection)
        return self.make_request(method='POST', uri=uri, data=document)

    def get(self, kind, collection, key):
        uri = '{}/{}/{}'.format(kind, collection, key)
        return self.make_request(method='GET', uri=uri)

    def search(self, kind, collection, query=None, per_page=10, page=1):
        uri = '{}/{}/{}'.format(kind, collection, key)
        params = {
            'query': query,
            'per_page': per_page,
            'page': page
        }
        return self.make_request(method='GET', uri=uri, params=params)

    def list(self, kind, collection, per_page=10, page=1):
        uri = '{}/{}/{}'.format(kind, collection, key)
        params = {
            'per_page': per_page,
            'page': page
        }
        return self.make_request(method='GET', uri=uri, params=params)

    def put(self, kind, collection, key, document):
        uri = '{}/{}/{}'.format(kind, collection, key)
        return self.make_request(method='PUT', uri=uri, data=document)

    def patch(self, kind, collection, key, document):
        uri = '{}/{}/{}'.format(kind, collection, key)
        return self.make_request(method='PUT', uri=uri, data=document)

    def delete(self, kind, collection, key):
        uri = '{}/{}/{}'.format(kind, collection, key)
        return self.make_request(method='DELETE', uri=uri)
