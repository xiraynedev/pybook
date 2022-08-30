"""import modules"""
from django.urls import path
from .views import index, books, book_details, book_search, results

urlpatterns = [
    path("", index, name="index_view"),
    path("books/", books, name="book_list_view"),
    path("books/<int:book_id>", book_details, name="book_details_view"),
    path("search/", book_search, name="book_search_view"),
    path("results/", results, name="results_view"),
]
