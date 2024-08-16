from books.models import Book, Author
from django.db.models import Count, CharField, F, Value, Subquery, OuterRef, Value
from django.db.models.functions import Coalesce
from django.contrib.postgres.aggregates import StringAgg


class BookAnalysesService:
    def show_book_and_author(self):
        books = (
            Book.objects
            .select_related('author')
            .order_by('author')
            .all()
        )

        return books

    def get_books_qty_for_each_author(self):
        authors_books = (
            Book.objects
            .select_related('author')
            .values('author__name')
            .annotate(books=Count('title'))
            .order_by('books')
            .all()
        )

        return authors_books

    def list_all_authors_their_books(self):
        authors_and_books = Author.objects.annotate(
            books_list=Coalesce(Subquery(
                Book.objects.filter(author=OuterRef('pk'))
                .values('author')
                .annotate(books=StringAgg('title', delimiter=', '))
                .values('books'),
                output_field=CharField()
            ), Value('No books'))
        )

        return authors_and_books
