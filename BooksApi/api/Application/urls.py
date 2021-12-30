from django.urls import path
from .views import BookView

urlpatterns = [
    path('books/', BookView.as_view(), name='books_list'),
    path('books/<int:pk>', BookView.as_view(), name='book_process'),
]
