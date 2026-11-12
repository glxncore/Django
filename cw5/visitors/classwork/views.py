
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def result(request):
    username = request.GET.get('username')

    form_data = request.GET

    return render(request, 'result.html', {
        'username': username,
        'form_data': form_data
    })