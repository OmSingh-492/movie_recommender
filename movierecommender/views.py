from . import views
from .models import Movie
from django.shortcuts import render

def movie_recommendation_view(request):
    if request.method == "GET":
        # The context/data to be presented in the HTML template
        context = {}
        # Rendwe a HTML page with specified template and context
        return render(request, 'movierecommender/movie_list.html', context)