from rest_framework import serializers
from books.models import Author, Book


class BookSerializer(serializers.ModelSerializer):
    book_author = serializers.ReadOnlyField()
    class Meta:
        model = Book
        fields = "__all__"


class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = (
            'id',
            "first_name",
            "last_name",
            "books",
        )
