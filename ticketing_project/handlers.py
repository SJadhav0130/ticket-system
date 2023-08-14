from rest_framework.views import exception_handler #type:ignore
from rest_framework.response import Response #type:ignore

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        return Response({
            "error": response.data,
        }, status=response.status_code)

    return None
