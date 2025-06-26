from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods


@csrf_exempt
@require_http_methods(['PUT' , 'GET'])
def get_profile(request , user_id , username=None):
    if request.method == 'GET':
        q_param = request.GET.getlist('x')
        print(f'User profile called for user-{user_id} with username: {username} -- queries: {q_param}')
        return HttpResponse(f'User {user_id} with username {username} returned! -- queries: {q_param}')
    elif request.method == 'PUT':
        return HttpResponse(f'User profile called for user-{user_id} with username: {username} ,status:201')
    elif request.method == 'DELETE':
        return HttpResponse('Profile called for user-{user_id} with username: {username} deleted',status=201)


