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
