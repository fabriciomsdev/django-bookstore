import csv
import os
from django.core.management.base import BaseCommand
from books.models import Book, Author


class Command(BaseCommand):
    help = 'Load books from a CSV file into the database'

    def handle(self, *args, **kwargs):
        current_path = os.path.dirname(os.path.abspath(__file__))
        file_path = current_path + '/fixtures/books.csv'
        authors = set()
        author_books = {}

        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                author_name = row['author']
                authors.add(author_name)
                
                if author_name not in author_books:
                    author_books[author_name] = []

                author_books[author_name].append(row)
            
            for author in authors:
                author_entity = Author.objects.create(name=author)
                for row in author_books[author]:
                    Book.objects.create(
                        title=row['title'],
                        author=author_entity
                    )

        self.stdout.write(self.style.SUCCESS('Data successfully loaded'))

        # list all books
        books = Book.objects.all()
        for book in books:
            print(f'"{book.title}". {book.author.name}')
