from time import sleep
import csv
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, FileResponse, StreamingHttpResponse
from django.shortcuts import render


# Create your views here.

def retrive_posts(request):

    print('retrive_posts')
    # return HttpResponse('retrive_posts')

    date = [
        {
            'title' : 'post_one' ,
            'content' : 'My Post is' ,
            'author' : 'ali'
        }
    ]
    return JsonResponse(date , safe=False)

def retrive_Post_info(request):
    print('retrive_Post_info')
    file = open('static/harvard.jpg', 'rb')
    response = FileResponse(file , content_type='image/jpeg')
    #for auto downloading
    response['Content-Disposition'] = f'attachment; filename="harvard.png"'
    return response


def generate_post_csv(request):
    print('generate_text')
    for i in range(100):
        if i % 10 == 0:
            sleep(0.2)
        yield [i,f'data{i}' , f'author column{i}']

def retrive_Post_text(request):
    print('retrive_Post_text')
    writer = csv.writer(CSVWriter())
    response = StreamingHttpResponse((writer.writerow(row) for row in generate_post_csv(request))  , content_type='text/csv')
    return response


class CSVWriter:
    def write(self, value):
        return value