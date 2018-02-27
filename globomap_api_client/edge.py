from globomap_api_client.base import Base


class Edge(Base):

    def post(self, document):
        return self.make_request(method='POST', uri='collections', data=document)

    def list(self):
        return self.make_request(method='GET', uri='collections')
