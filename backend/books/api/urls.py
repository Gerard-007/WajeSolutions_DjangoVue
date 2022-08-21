from django.urls import path
from books.api import views

urlpatterns = [
    path('author/<int:pk>/', views.AuthorCRUD.as_view(), name='author_rud_api'),
    path('authors/', views.AuthorList.as_view(), name='author_list_api'),
    path('book/<int:pk>/', views.BookCRUD.as_view(), name='book_rud_api'),
    path('', views.BookList.as_view(), name='book_list_api'),
]