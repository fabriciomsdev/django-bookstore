from django.urls import include, path
from rest_framework import routers

from .views import AuthorsViewSet, analyse_library, BooksViewSet

books_router_api = routers.DefaultRouter()
books_router_api.register(r'authors', AuthorsViewSet)
books_router_api.register(r'books', BooksViewSet)

books_api_urls = [
    path('', include(books_router_api.urls)),
    path('library-analyses', analyse_library),
]
