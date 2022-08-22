from rest_framework import generics
from books.models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from rest_framework.response import Response
from rest_framework import status, permissions


class AuthorList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorCRUD(generics.RetrieveUpdateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = "id"

    # def get_object(self):
    #     queryset = self.get_queryset()
    #     return generics.get_object_or_404(self.queryset, user=self.request.user)

    def post(self, request, *args, **kwargs):
        name = request.data.get("name")
        isbn = request.data.get("isbn")
        author = request.data.get("author")
        x = author.split()
        print(x[0])
        get_author = Author.objects.get(pk=x[0])
        book = self.get_object()
        book.name = name
        book.isbn = isbn
        book.author = get_author
        book.save()
        return Response(f"Book {name} added", status=status.HTTP_200_OK)


class BookCRUD(generics.RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer