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


class ApiError(Exception):

    def __init__(self, message, status_code=None):
        super(ApiError, self).__init__(message, status_code)

        self.message = message
        self.status_code = status_code


class ValidationError(Exception):

    def __init__(self, message, status_code):
        super(ValidationError, self).__init__(message, status_code)

        self.message = message
        self.status_code = status_code


class Unauthorized(Exception):

    def __init__(self, message, status_code):
        super(Unauthorized, self).__init__(message, status_code)

        self.message = message
        self.status_code = status_code


class Forbidden(Exception):

    def __init__(self, message, status_code):
        super(Forbidden, self).__init__(message, status_code)

        self.message = message
        self.status_code = status_code


class NotFound(Exception):

    def __init__(self, message, status_code):
        super(NotFound, self).__init__(message, status_code)

        self.message = message
        self.status_code = status_code


class DocumentAlreadyExists(Exception):

    def __init__(self, message, status_code):
        super(DocumentAlreadyExists, self).__init__(message, status_code)

        self.message = message
        self.status_code = status_code
