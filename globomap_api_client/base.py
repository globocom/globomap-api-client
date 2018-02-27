import loggging

from globomap_api_client import exceptions

logger = logging.getLogger(__name__)


class Base(object):

    def __init__(self, auth):
        self.auth = token
        self.session = Session()
        self.session.mount('https://', HTTPAdapter(max_retries=5))
        self.session.mount('http://', HTTPAdapter(max_retries=5))

    def _get_auth(self):
        auth = {'Authorization': 'Token token={}'.format(self.token)}
        return auth

    def make_request(self, method, uri, data, params):
        request_url = '{}/v2/{}'.format(self.auth.api_url, uri)
        try:
            if method in ('GET', 'DELETE'):
                response = self.session.request(
                    method,
                    request_url,
                    params=params,
                    auth=self._get_auth()
                )
            else:
                response = self.session.request(
                    method,
                    request_url,
                    auth=self._get_auth(),
                    data=json.dumps(data)
                )
        except:
            logger.exception('Error in request')
            raise exceptions.ApiError('Error in request', status_code)

        else:
            return self._parser_response()

    def _parser_response(self, response):
        content = response.json()
        status_code = response.status_code

        if status_code == 200:
            return content
        elif status_code == 400:
            raise exceptions.ValidationError(content, status_code)
        elif status_code == 401:
            raise exceptions.Forbidden(content, status_code)
        elif status_code == 403:
            raise exceptions.Unauthorized(content, status_code)
        elif status_code == 404:
            raise exceptions.NotFound(content, status_code)
        elif status_code == 409:
            raise exceptions.DocumentAlreadyExists(content, status_code)
