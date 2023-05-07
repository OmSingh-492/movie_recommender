from django.urls import path
from . import views

urlpatterns = [
    path(route ='', view=views.movie_recommendation_view, name='recommendations'),
]
