from rest_framework import status
from rest_framework.response import Response as drf_response
from rest_framework.views import exception_handler


# def custom_exception_handler(exc, context):
#     # Call REST framework's default exception handler first,
#     # to get the standard error response.
#     response = exception_handler(exc, context)
#     if isinstance(exc, AuthenticationFailed):
#         response.data = {'msg': str(exc), 'status': False, 'data': None}
#         response.status_code = exc.status_code
#         return response
#     elif isinstance(exc, PermissionDenied):
#         response.data = {'msg': str(exc), 'status': False, 'data': None}
#         response.status_code = exc.status_code
#         return response
#     elif isinstance(exc, (ValidationError, MethodNotAllowed, NotAcceptable)):
#         detail_message = exc.detail[0] if isinstance(exc.detail, list) else exc.detail
#         response.data = {'msg': str(detail_message), 'status': False, 'data': None}
#         response.status_code = exc.status_code
#         return response
#     elif isinstance(exc, APIException):
#         data = None
#         if hasattr(exc, 'data'):
#             data = exc.data
#         response.data = {'msg': str(exc), 'status': False, 'data': data}
#         response.status_code = status.HTTP_200_OK
#         return response
#     else:
#         return response


class Response(drf_response):
    def __init__(self, data=None, status=None, template_name=None, headers=None, exception=False, content_type=None,
                 code=200,
                 msg=''):
        super().__init__(data=data, status=status, template_name=template_name, headers=headers, exception=exception,
                         content_type=content_type)
        self.data = {'data': data, 'msg': msg, 'code': code}
