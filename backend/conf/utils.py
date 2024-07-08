from rest_framework.views import exception_handler

from .exceptions import CustomValidationError


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        if isinstance(exc, CustomValidationError):
            response.data = exc.detail
        else:
            response.data = {
                "message": response.data[0],
                "status_code": response.status_code,
            }
        return response

    return response
