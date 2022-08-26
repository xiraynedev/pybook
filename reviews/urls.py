from django.urls import path
from .views import index, book_list, book_details

urlpatterns = [
    path('', index, name='index_view'),
    path('books/', book_list, name='book_list_view'),
    path('books/<int:id>', book_details, name='book_details_view')
]
