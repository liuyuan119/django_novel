from django.conf.urls import url

from apps.art import search_handler, views

urlpatterns = [
    url(r'^index/', views.IndexHandler),
    url(r'^search/', search_handler.SearchHandler),
]
