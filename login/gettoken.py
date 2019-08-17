import requests
import json
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def processlogin(request, username, password):
    users = User.objects.all().filter(username=username)
    if(len(users) == 0):
        return redirect('/')
    
    else:
        headers = {'content-type': 'application/json'}
        data = json.dumps({'username': username, 'password': password})
        url = "http://localhost:8000/api/token"
        r = requests.post(url, data=data, headers=headers)
        a = r.json()
        return a
        # if "detail" not in a:
        #     context = {
        #         'length': len(users),
        #         'access': a['access'],
        #         'refresh': a['refresh'],
        #         'checker': 0
        #     }
        #     return render(request, 'login/index.html', context)
        
        # else:
        #     context = {
        #         'length': len(users),
        #         'detail': a['detail'],
        #         'checker': 1
        #     }
        #     return render(request, 'login/index.html', context)


def processregister(request, username, password):
    users = User.objects.all().filter(username=username)
    if(len(users) == 0):
        User.objects.create_user(username, '', password)
        a = "successfully created a user"
        return a
    else:
        a = "username already taken"
        return a
