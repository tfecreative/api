from rest_framework.views import exception_handler
from rest_framework.exceptions import ValidationError
from tfecreative import settings
from django.http import JsonResponse, Http404


default_message = "Nothing to see here, certainly not an error... (・・；)"


class ApiError(Exception):
    pass


def get_message_from_validation_error(exc):
    if not exc.detail:
        return None
    errors = exc.detail.get("non_field_errors")
    return None if not errors else str(errors[0])


def get_error_message(exc):
    if not exc:
        return default_message

    if settings.DEBUG:
        return str(exc) or default_message

    return {
        ApiError: str(exc),
        ValidationError: get_message_from_validation_error(exc) or default_message,
    }.get(type(exc), default_message)


def base_exception_handler(target_exception, context):
    response = exception_handler(target_exception, context)
    status_code = getattr(response, "status_code", 400)
    json_data = {
        "error": get_error_message(target_exception),
        "status_code": status_code,
    }
    return JsonResponse(data=json_data, status=status_code)
