import requests
import json
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from rest_framework.response import Response
import logging
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Login


@csrf_exempt
def processlogin(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    username = body['email']
    password = body['password']
    users = User.objects.all().filter(username=username)
    if(len(users) == 0):
        return JsonResponse({'access': 'error'}, safe=False)
    
    else:
        headers = {'content-type': 'application/json'}
        data = json.dumps({'username': username, 'password': password})
        url = "http://localhost:8000/api/token"
        r = requests.post(url, data=data, headers=headers)
        a = r.json()
        access = a['access']
        userid = User.objects.values_list('id', flat=True).get(username=username)
        insertuser = Login(id=userid, accesstoken=access)
        insertuser.save()
        return JsonResponse({'access': access}, safe=False)


@csrf_exempt
def processregister(request, username, password):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    username = body['email']
    password = body['password']
    users = User.objects.all().filter(username=username)
    if(len(users) == 0):
        User.objects.create_user(username, '', password)
        return JsonResponse({'message': 'account successfully created'}, safe=False)
    else:
        return JsonResponse({'message': 'username already taken'}, safe=False)


@csrf_exempt
def processlogout(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    print(str(body))
    accesstoken = body['accesstoken']
    Login.objects.filter(accesstoken=accesstoken).delete()
    return JsonResponse({'message': 'Logout Successful'}, safe=False)
