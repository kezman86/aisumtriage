from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response

from api.serializers import CaseSFSerializer
from webapp.models import CaseSF
from webapp.views import sumModules
from django.db import IntegrityError
from django.utils import timezone

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def loginapi(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'status' : 'true', 'token': token.key},
                    status=HTTP_200_OK)


@csrf_exempt
@api_view(["GET"])
def sample_api(request):
    data = {'sample_data': 123}
    return Response(data, status=HTTP_200_OK)


@csrf_exempt
@api_view(["GET"])
def getAllCases(request):
    allcases = CaseSF.objects.filter( status = 0 )
    cases = []
    for case in allcases:
        cases.append(CaseSFSerializer(case ).data)
    data = {
        'cases': cases,
        'modules_risk' : sumModules['risk'],
        'modules_acct' : sumModules["acct"],
        'modules_bo' : sumModules["bo"],
        'modules_fo' : sumModules["fo"],
        'modules_arch' : sumModules["arch"]
        }
    return Response(data, status=HTTP_200_OK)

@csrf_exempt
@api_view(["POST"])
def approvecase(request, caseID):
    if 'sumModule' not in request.POST:
        data = {'detail' : 'errors: module not specified'}
        return Response ( data , status = HTTP_400_BAD_REQUEST )

    case = get_object_or_404(CaseSF, caseIDSf=caseID)

    case.datecompleted = timezone.now()
    case.completedBy = request.user
    case.status = 1  # reviewed

    if case.caseModule != request.POST['sumModule']:
        case.caseModule = request.POST['sumModule']
        case.aicorrect = False

        case.save()
        data = {'detail' : 'case approved - module changed'}
        return Response ( data , status = HTTP_200_OK )

    data = {'detail' : 'case approved'}
    return Response ( data , status = HTTP_200_OK )