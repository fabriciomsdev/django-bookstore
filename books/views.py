from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets, mixins, generics

from books.services import BookAnalysesService
from .serializers import AuthorsSerializer, BooksSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Author, Book

class AuthorsViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorsSerializer


class BooksViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer


@api_view(http_method_names=['GET'])
def analyse_library(request):
    kind = request.query_params.get('kind')
    service = BookAnalysesService()

    if kind == 'show_book_and_author':
        books = [
            {
                'title': book.title,
                'author': book.author.name
            }
            for book in service.show_book_and_author()
        ]
    elif kind == 'get_books_qty_for_each_author':
        books = [
            {
                'author': entry['author__name'],
                'books': entry['books']
            }
            for entry in service.get_books_qty_for_each_author()
        ]
    elif kind == 'list_all_authors_their_books':
        books = [
            {
                'author': author.name,
                'books_written': author.books_list
            }
            for author in service.list_all_authors_their_books()
        ]
    
    return Response(books)

        