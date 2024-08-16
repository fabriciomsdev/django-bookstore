from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Author, Book

class AuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name']


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author']


