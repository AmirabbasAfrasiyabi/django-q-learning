from django.contrib.sessions.backends import file
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

# Create your views here.
@csrf_exempt
@ require_http_methods(['GET', 'POST' , 'DELETE'])
def get_profile(request , user_id , username = None):

    if request.method == 'GET':
        q_param = request.GET.keys()
        print(f'User profile called for user_id {user_id} with username {username} -- q_param : {q_param}')
        return HttpResponse(f'User {user_id} with username {username} profile returned -- q_param : {q_param}')

    elif request.method == 'PUT':
        return HttpResponse(f'Profile{user_id} profile updated ' , status=201)


    elif request.method == 'DELETE':
        return HttpResponse(f'Profile{user_id} profile deleted ' , status=405)

