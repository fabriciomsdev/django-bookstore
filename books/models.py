from django.db import models

# Create your models here.
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


"""
6.1 Using Django ORM, write a function that will print the book title and the author name(who wrote it) for
all the books we have in the database. Like this:
    “War and Peace”. Leo Tolstoy
    “Anna Karenina”. Leo Tolstoy
    “Resurrection”. Leo Tolstoy
    “The Three Musketeers”. Alexandre Dumas
    “The Count of Monte Cristo”. Alexandre Dumas
"""

"""
6.2 Write another function that will print the author’s name and all the books he wrote. For all the authors we
have in the database. Like this:
    Leo Tolstoy: “War and Peace”, “Anna Karenina”, “Resurrection”
    Alexandre Dumas: “The Three Musketeers”, “The Count of Monte Cristo”
"""

"""
6.3 Implement the third function, it should print the author’s name and the number of books he wrote. Order
by the number of books written, descending. Like this:
    Leo Tolstoy: 3
    Alexandre Dumas: 2
"""
