from django.urls import path, include
from .views import *

urlpatterns = [
    path('', indexPageView, name='index'),
    path('<str:movieTitle>/<str:director>', moviePageView, name='moviePageView'),
    path('joinus/', joinusPageView, name='joinus'),
    path('about/', aboutPageView, name='about'),
    path('contact/', contactPageView, name='contact'),
    path('search/', searchPageView, name='search'),
    path('list/', listPageView, name='list'),
    path('deleteReview/', deleteReviewView, name='deleteReview'),
    path('editReviewView/', editReviewView, name='editReview'),
]