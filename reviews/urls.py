from django.urls import path
from .views import index, book_list, book_details, book_search, results

urlpatterns = [
    path('', index, name='index_view'),
    path('books/', book_list, name='book_list_view'),
    path('books/<int:id>', book_details, name='book_details_view'),
    path('search/', book_search, name='book_search_view'),
    path('results/', results, name='results_view')
]
