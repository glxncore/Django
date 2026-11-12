from django.shortcuts import render

# Create your views here.

def display(request):
    my_objects = [
        {'name': 'John', 'age': 25, 'city': 'New York'},
        {'name': 'Jane', 'age': 30, 'city': 'San Francisco'},
        {'name': 'Bob', 'age': 20, 'city': 'Chicago'}
    ]
    context = {'my_objects': my_objects}
    return render(request, 'index.html', context)