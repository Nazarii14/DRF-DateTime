from rest_framework.response import Response
from rest_framework.decorators import api_view
from .calculations.calculations import *


@api_view(['GET'])
def api_info(request, *args, **kwargs):
    info = get_all_info()
    return Response(info)


@api_view(['GET'])
def month_info(request, *args, **kwargs):
    info = get_month_info()
    return Response(info)


@api_view(['GET'])
def year_info(request, *args, **kwargs):
    info = get_year_info()
    return Response(info)
