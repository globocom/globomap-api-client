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
from unittest.mock import MagicMock
from unittest.mock import Mock
from unittest.mock import patch

import unittest2

from globomap_api_client import exceptions
from globomap_api_client.base import Base


class BaseTest(unittest2.TestCase):

    def tearDown(self):
        patch.stopall()

    def test_post_error(self):
        mock_requests = patch('globomap_api_client.base.Session').start()
        response_mock = MagicMock(return_value={'message': 'Error'})

        mock_requests.return_value.request.return_value = MagicMock(
            json=response_mock, status_code=500)

        with self.assertRaises(exceptions.ApiError):
            base = Base(Mock())
            data = {'key': 'value'}
            base.make_request('POST', 'path', None, data)

    def test_post_exception(self):
        mock_requests = patch('globomap_api_client.base.Session').start()

        mock_requests.return_value.request.return_value = MagicMock(
            side_effect=Exception())

        with self.assertRaises(exceptions.ApiError):
            base = Base(Mock())
            data = {'key': 'value'}
            base.make_request('POST', 'path', None, data)

    def test_post_200(self):
        mock_session = patch('globomap_api_client.base.Session').start()

        response_mock = MagicMock(return_value={'message': 'message'})
        request_mock = mock_session.return_value.request
        request_mock.return_value = MagicMock(
            json=response_mock, status_code=200)

        data = {'key': 'value'}

        base = Base(Mock(api_url='http://localhost', token='token123'))
        base.make_request('POST', 'path', None, data)

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Token token=token123'
        }
        request_mock.assert_called_once_with(
            'POST', 'http://localhost/v2/path/', data=json.dumps(data), headers=headers
        )

    def test_post_400(self):
        mock_requests = patch('globomap_api_client.base.Session').start()
        response_mock = MagicMock(return_value={'message': 'Error'})

        mock_requests.return_value.request.return_value = MagicMock(
            json=response_mock, status_code=400)

        with self.assertRaises(exceptions.ValidationError):
            base = Base(Mock())
            data = {'key': 'value'}
            base.make_request('POST', 'path', None, data)

    def test_post_401(self):
        mock_requests = patch('globomap_api_client.base.Session').start()
        response_mock = MagicMock(return_value={'message': 'Error'})

        mock_requests.return_value.request.return_value = MagicMock(
            json=response_mock, status_code=401)

        with self.assertRaises(exceptions.Unauthorized):
            base = Base(Mock())
            data = {'key': 'value'}
            base.make_request('POST', 'path', None, data)

    def test_post_403(self):
        mock_requests = patch('globomap_api_client.base.Session').start()
        response_mock = MagicMock(return_value={'message': 'Error'})

        mock_requests.return_value.request.return_value = MagicMock(
            json=response_mock, status_code=403)

        with self.assertRaises(exceptions.Forbidden):
            base = Base(Mock())
            data = {'key': 'value'}
            base.make_request('POST', 'path', None, data)

    def test_post_404(self):
        mock_requests = patch('globomap_api_client.base.Session').start()
        response_mock = MagicMock(return_value={'message': 'Error'})

        mock_requests.return_value.request.return_value = MagicMock(
            json=response_mock, status_code=404)

        with self.assertRaises(exceptions.NotFound):
            base = Base(Mock())
            data = {'key': 'value'}
            base.make_request('POST', 'path', None, data)

    def test_post_409(self):
        mock_requests = patch('globomap_api_client.base.Session').start()
        response_mock = MagicMock(return_value={'message': 'Error'})

        mock_requests.return_value.request.return_value = MagicMock(
            json=response_mock, status_code=409)

        with self.assertRaises(exceptions.DocumentAlreadyExists):
            base = Base(Mock())
            data = {'key': 'value'}
            base.make_request('POST', 'path', None, data)

    def test_put_error(self):
        mock_requests = patch('globomap_api_client.base.Session').start()
        response_mock = MagicMock(return_value={'message': 'Error'})

        mock_requests.return_value.request.return_value = MagicMock(
            json=response_mock, status_code=500)

        with self.assertRaises(exceptions.ApiError):
            base = Base(Mock())
            data = {'key': 'value'}
            base.make_request('PUT', 'path', None, data)

    def test_put_exception(self):
        mock_requests = patch('globomap_api_client.base.Session').start()

        mock_requests.return_value.request.return_value = MagicMock(
            side_effect=Exception())

        with self.assertRaises(exceptions.ApiError):
            base = Base(Mock())
            data = {'key': 'value'}
            base.make_request('PUT', 'path', None, data)

    def test_put_200(self):
        mock_session = patch('globomap_api_client.base.Session').start()

        response_mock = MagicMock(return_value={'message': 'message'})
        request_mock = mock_session.return_value.request
        request_mock.return_value = MagicMock(
            json=response_mock, status_code=200)

        data = {'key': 'value'}

        base = Base(Mock(api_url='http://localhost', token='token123'))
        base.make_request('PUT', 'path', None, data)

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Token token=token123'
        }
        request_mock.assert_called_once_with(
            'PUT', 'http://localhost/v2/path/', data=json.dumps(data), headers=headers
        )

    def test_put_400(self):
        mock_requests = patch('globomap_api_client.base.Session').start()
        response_mock = MagicMock(return_value={'message': 'Error'})

        mock_requests.return_value.request.return_value = MagicMock(
            json=response_mock, status_code=400)

        with self.assertRaises(exceptions.ValidationError):
            base = Base(Mock())
            data = {'key': 'value'}
            base.make_request('PUT', 'path', None, data)

    def test_put_401(self):
        mock_requests = patch('globomap_api_client.base.Session').start()
        response_mock = MagicMock(return_value={'message': 'Error'})

        mock_requests.return_value.request.return_value = MagicMock(
            json=response_mock, status_code=401)

        with self.assertRaises(exceptions.Unauthorized):
            base = Base(Mock())
            data = {'key': 'value'}
            base.make_request('PUT', 'path', None, data)

    def test_put_403(self):
        mock_requests = patch('globomap_api_client.base.Session').start()
        response_mock = MagicMock(return_value={'message': 'Error'})

        mock_requests.return_value.request.return_value = MagicMock(
            json=response_mock, status_code=403)

        with self.assertRaises(exceptions.Forbidden):
            base = Base(Mock())
            data = {'key': 'value'}
            base.make_request('PUT', 'path', None, data)

    def test_put_404(self):
        mock_requests = patch('globomap_api_client.base.Session').start()
        response_mock = MagicMock(return_value={'message': 'Error'})

        mock_requests.return_value.request.return_value = MagicMock(
            json=response_mock, status_code=404)

        with self.assertRaises(exceptions.NotFound):
            base = Base(Mock())
            data = {'key': 'value'}
            base.make_request('PUT', 'path', None, data)

    def test_patch_error(self):
        mock_requests = patch('globomap_api_client.base.Session').start()
        response_mock = MagicMock(return_value={'message': 'Error'})

        mock_requests.return_value.request.return_value = MagicMock(
            json=response_mock, status_code=500)

        with self.assertRaises(exceptions.ApiError):
            base = Base(Mock())
            data = {'key': 'value'}
            base.make_request('PATCH', 'path', None, data)

    def test_patch_exception(self):
        mock_requests = patch('globomap_api_client.base.Session').start()

        mock_requests.return_value.request.return_value = MagicMock(
            side_effect=Exception())

        with self.assertRaises(exceptions.ApiError):
            base = Base(Mock())
            data = {'key': 'value'}
            base.make_request('PATCH', 'path', None, data)

    def test_patch_200(self):
        mock_session = patch('globomap_api_client.base.Session').start()

        response_mock = MagicMock(return_value={'message': 'message'})
        request_mock = mock_session.return_value.request
        request_mock.return_value = MagicMock(
            json=response_mock, status_code=200)

        data = {'key': 'value'}

        base = Base(Mock(api_url='http://localhost', token='token123'))
        base.make_request('PATCH', 'path', None, data)

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Token token=token123'
        }
        request_mock.assert_called_once_with(
            'PATCH', 'http://localhost/v2/path/', data=json.dumps(data), headers=headers
        )

    def test_patch_400(self):
        mock_requests = patch('globomap_api_client.base.Session').start()
        response_mock = MagicMock(return_value={'message': 'Error'})

        mock_requests.return_value.request.return_value = MagicMock(
            json=response_mock, status_code=400)

        with self.assertRaises(exceptions.ValidationError):
            base = Base(Mock())
            data = {'key': 'value'}
            base.make_request('PATCH', 'path', None, data)

    def test_patch_401(self):
        mock_requests = patch('globomap_api_client.base.Session').start()
        response_mock = MagicMock(return_value={'message': 'Error'})

        mock_requests.return_value.request.return_value = MagicMock(
            json=response_mock, status_code=401)

        with self.assertRaises(exceptions.Unauthorized):
            base = Base(Mock())
            data = {'key': 'value'}
            base.make_request('PATCH', 'path', None, data)

    def test_patch_403(self):
        mock_requests = patch('globomap_api_client.base.Session').start()
        response_mock = MagicMock(return_value={'message': 'Error'})

        mock_requests.return_value.request.return_value = MagicMock(
            json=response_mock, status_code=403)

        with self.assertRaises(exceptions.Forbidden):
            base = Base(Mock())
            data = {'key': 'value'}
            base.make_request('PATCH', 'path', None, data)

    def test_patch_404(self):
        mock_requests = patch('globomap_api_client.base.Session').start()
        response_mock = MagicMock(return_value={'message': 'Error'})

        mock_requests.return_value.request.return_value = MagicMock(
            json=response_mock, status_code=404)

        with self.assertRaises(exceptions.NotFound):
            base = Base(Mock())
            data = {'key': 'value'}
            base.make_request('PATCH', 'path', None, data)

    def test_get_error(self):
        mock_requests = patch('globomap_api_client.base.Session').start()
        response_mock = MagicMock(return_value={'message': 'Error'})

        mock_requests.return_value.request.return_value = MagicMock(
            json=response_mock, status_code=500)

        with self.assertRaises(exceptions.ApiError):
            base = Base(Mock())
            query = {'key': 'value'}
            base.make_request('GET', 'path', query, None)

    def test_get_exception(self):
        mock_requests = patch('globomap_api_client.base.Session').start()

        mock_requests.return_value.request.return_value = MagicMock(
            side_effect=Exception())

        with self.assertRaises(exceptions.ApiError):
            base = Base(Mock())
            query = {'key': 'value'}
            base.make_request('GET', 'path', query, None)

    def test_get_200(self):
        mock_session = patch('globomap_api_client.base.Session').start()

        response_mock = MagicMock(return_value={'message': 'message'})
        request_mock = mock_session.return_value.request
        request_mock.return_value = MagicMock(
            json=response_mock, status_code=200)

        params = {'key': 'value'}

        base = Base(Mock(api_url='http://localhost', token='token123'))
        base.make_request('GET', 'path', params, None)

        headers = {
            'Authorization': 'Token token=token123'
        }
        request_mock.assert_called_once_with(
            'GET', 'http://localhost/v2/path/', params=params, headers=headers
        )

    def test_get_400(self):
        mock_requests = patch('globomap_api_client.base.Session').start()
        response_mock = MagicMock(return_value={'message': 'Error'})

        mock_requests.return_value.request.return_value = MagicMock(
            json=response_mock, status_code=400)

        with self.assertRaises(exceptions.ValidationError):
            base = Base(Mock())
            params = {'key': 'value'}
            base.make_request('GET', 'path', params, None)

    def test_get_401(self):
        mock_requests = patch('globomap_api_client.base.Session').start()
        response_mock = MagicMock(return_value={'message': 'Error'})

        mock_requests.return_value.request.return_value = MagicMock(
            json=response_mock, status_code=401)

        with self.assertRaises(exceptions.Unauthorized):
            base = Base(Mock())
            params = {'key': 'value'}
            base.make_request('GET', 'path', params, None)

    def test_get_403(self):
        mock_requests = patch('globomap_api_client.base.Session').start()
        response_mock = MagicMock(return_value={'message': 'Error'})

        mock_requests.return_value.request.return_value = MagicMock(
            json=response_mock, status_code=403)

        with self.assertRaises(exceptions.Forbidden):
            base = Base(Mock())
            params = {'key': 'value'}
            base.make_request('GET', 'path', params, None)

    def test_get_404(self):
        mock_requests = patch('globomap_api_client.base.Session').start()
        response_mock = MagicMock(return_value={'message': 'Error'})

        mock_requests.return_value.request.return_value = MagicMock(
            json=response_mock, status_code=404)

        with self.assertRaises(exceptions.NotFound):
            base = Base(Mock())
            params = {'key': 'value'}
            base.make_request('GET', 'path', params, None)
