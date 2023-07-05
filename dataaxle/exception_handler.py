from typing import Any, Optional

from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import APIException
from django.core.exceptions import ValidationError




class ExceptionCreator(Exception):
    code: Optional[int]
    message: Any

    def __init__(self, *, code: Optional[int] = None, message: Optional[Any] = None):
        self.code = code
        self.message = message or None

    def __str__(self):
        return self.message or None


def exception_handler(api_level=False):
    def decorator(func):
        def inner_func(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except KeyError as e:
                if api_level:
                    raise APIException(e)
                raise ExceptionCreator(message="required key {key} is mandatory".format(key=e), code=400)

            except ValueError as e:
                if api_level:
                    raise APIException(e)
                raise ExceptionCreator(message="{key}".format(key=e), code=400)

            except TypeError as e:
                if api_level:
                    raise APIException(e)
                raise ExceptionCreator(message="{key}".format(key=e), code=400)

            except ObjectDoesNotExist as e:
                if api_level:
                    raise APIException(e)
                raise ExceptionCreator(message="{key}".format(key=e), code=400)
            except ValidationError as e:
                if api_level:
                    raise APIException(e)
                raise ExceptionCreator(message="{key}".format(key=e), code=400)

            except AttributeError as e:
                if api_level:
                    raise APIException(e)
                raise ExceptionCreator(message="{key}".format(key=e), code=400)



        return inner_func
    return decorator
