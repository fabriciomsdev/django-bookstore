import csv
import os
from django.core.management.base import BaseCommand
from books.models import Book, Author
from django.db.models import Count, CharField, F, Value, Subquery, OuterRef, Value
from django.db.models.functions import Coalesce
from django.contrib.postgres.aggregates import StringAgg

from books.services import BookAnalysesService

class Command(BaseCommand):
    help = 'Run analyses of books in library with optimized queries'
    service = BookAnalysesService()

    def add_arguments(self, parser):
        parser.add_argument("kind", type=str)

    def handle(self, *args, **options):        
        analyze_kind = options['kind']

        if analyze_kind == 'show_book_and_author':
            books = self.service.show_book_and_author()

            for book in books:
                print(f'"{book.title}". {book.author.name}')

        elif analyze_kind == 'get_books_qty_for_each_author':
            authors_books = self.service.get_books_qty_for_each_author()

            for entry in authors_books:
                author = entry['author__name']
                title_qty = entry['books']
                print(f'{author}: {title_qty}')

        elif analyze_kind == 'list_all_authors_their_books':
            authors_and_books = self.service.list_all_authors_their_books()

            for author in authors_and_books:
                print(f'{author.name}: {author.books_list} \n')

