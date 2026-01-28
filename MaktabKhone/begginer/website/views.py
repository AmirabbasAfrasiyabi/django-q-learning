from django.http import HttpResponse, JsonResponse


def home(request):
    return HttpResponse('<h1>this is a Home Page</h1>')


def about(request):
    return HttpResponse('<h1>this is a about Page</h1>')

def contact(request):
    return HttpResponse('<h1>this is a contact Page</h1>')