from django.db import models


class Author(models.Model):
    first_name = models.CharField(help_text="first name", max_length=150)
    last_name = models.CharField(help_text="last name", max_length=150)

    def __str__(self) -> str:
        return f"{self.first_name}-{self.last_name}"

    @property
    def get_fullname(self) -> str:
        return f"{self.first_name}-{self.last_name}"


class Book(models.Model):
    name = models.CharField(help_text="book name", max_length=150)
    isbn = models.CharField(help_text="book isbn", max_length=150)
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.pk}-{self.name}"

    @property
    def book_author(self) -> str:
        return f"{self.author.first_name} {self.author.last_name}"
