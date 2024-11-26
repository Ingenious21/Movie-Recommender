from . import views
from .models import Movie
from django.shortcuts import render

# HINT: Create a view to provide movie recommendations list for the HTML template
def movie_recommendation_view(request):
    if request.method == "GET":
        context = {}
        #The context/data to be presented is in the HTML template
        # #Render an HTML page with specified template and context
        return render(request, 'movierecommender/movielist.html', context)

