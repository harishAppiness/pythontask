from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .responseFormat import message_response
from .responseMessage import *

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserInfoSerializer
from .models import UserInfo
from .encryption import *
# from rest_framework_simplejwt.tokens import RefreshToken
import datetime
from django.utils import timezone
from random import randint
import requests
# from .encryption import jwt_payload_handler, jwt_encode_handler


# Create your views here.
@api_view(['POST'])
def Signup(request):
    email = request.data.get('email',None)
    if UserInfo.objects.filter(email=email).exists():
        return Response(message_response(duplicate_entry), status = 400)
    else:
        serializer = UserInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
    return Response('signed up successfully')


@api_view(['POST'])
def Login(request):
    mobile = request.data.get('mobile',None)
    if UserInfo.objects.filter(mobile=mobile).exists():
        api_key='bc290823-0e47-11ed-9c12-0200cd936042'
        per = get_object_or_404(UserInfo, mobile=mobile)
        phone_number=per.mobile
        otp= str(randint(1000, 9999))
        eotp=crypto_encode(otp)
        per.otp=eotp
        per.save()
        r = requests.get(f'https://2factor.in/API/V1/{api_key}/SMS/{phone_number}/{otp}', params=request.GET)
        if r.status_code == 200:
            return Response('otp sended')
    else:
        return Response('signup first')
        # return redirect(signup)
        # return Response message&signupapi
        
@api_view(['POST'])
def LoginVerify(request):
    otp = request.data.get('otp',None)
    mobile=request.data.get('mobile',None)
    print(otp,mobile)
    
    otp=str(otp)
    per = get_object_or_404(UserInfo, mobile=mobile)
    print(per)
    dotp= crypto_decode(per.otp)
    if dotp==otp:
        payload = jwt_payload_handler(per)
        per.otp = None
        per.last_login = timezone.now()
        per.save()
        context = {
                'token': jwt_encode_handler(payload),
                'email': per.email,
                'mobile': per.mobile,
                'user_details': UserInfoSerializer(per).data,
            }
        return Response(context)
    else:
        return Response({"Time out" : "Given otp is expired!!"}, status=status.HTTP_408_REQUEST_TIMEOUT)
