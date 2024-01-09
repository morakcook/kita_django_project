from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_search, name='news_search'),
]