import csv
from time import sleep
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, HttpResponsePermanentRedirect, FileResponse, \
    StreamingHttpResponse
from django.shortcuts import render


def retrieve_posts(request):
    print('retrieve_posts')

    data = [
        {
            'id': 1,
            'title': 'post 1',
            'content': 'post 1 content',
            'author': 'ali',
        }
    ]
    return JsonResponse(data , safe=False)
    # return HttpResponse('post_list!')
    # return HttpResponseRedirect("http://127.0.0.1:8000/posts/")
    # return HttpResponsePermanentRedirect('/profile')


def retrieve_post_info(request):
    file = open('./static/static.jpg', 'rb')
    response = FileResponse(file , content_type='image/jpg')
    #downloadfile
    # response['Content-Disposition'] = f'attachment; filename={file.name}'
    return response

def generate_post_csv():
    for i in range(100):
        if i % 10 == 0:
            sleep(.5)
        yield [i, f'data_{i}', f'another column {i}']

def retrieve_post_text(request):
    writer = csv.writer(CSVWriter())
    response = StreamingHttpResponse((writer.writerow(row) for row in generate_post_csv()), content_type='text/csv')
    return response

class CSVWriter:
    def write(self, value):
        return value