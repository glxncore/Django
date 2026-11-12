from django.shortcuts import render
from .models import Movie

def add_movie(request):

    message = ''




    if request.method == 'POST':

        name = request.POST.get('name')
        year = request.POST.get('year')

        movie = Movie(name=name, year=year)
        movie.save()

        message = f"Movie saved: {name} ({year})"

    return render(request, 'movie.html', {'message': message})