from django.http.response import HttpResponse
from django.urls import path
from .views import indexPageView, movieInfoPageView, addMoviePageView, addReviewPageView, aboutPageView, editMoviePageView

urlpatterns = [
    path('', indexPageView, name='index'),
    path('movie/<str:movieID>', movieInfoPageView, name='movieInfoPageView'),
    path('movie/addMovie', addMoviePageView, name='addMoviePageView'),
    path('movie/<str:movieID>/editReview/<int:reviewID>/', addReviewPageView, name='addReviewPageView'),
    path('', aboutPageView, name='about'),
    path('', editMoviePageView, name='editMovie')
]
