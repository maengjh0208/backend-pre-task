from rest_framework.exceptions import APIException
from rest_framework import status


class CustomValidationError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Invalid input'

    def __init__(self, message=None, status_code=None):
        message = message if message else self.default_detail
        status_code = status_code if status_code else self.status_code

        self.detail = {
            'message': message,
            'status_code': status_code,
        }
