from django.urls import path
from .views import indexPageView, searchPageView, listPageView


urlpatterns = [
    path('', indexPageView, name='index'),
    path('', searchPageView, name='search'),
    path('', listPageView, name='list')

]
