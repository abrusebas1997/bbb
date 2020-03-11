from django.urls import path

from api.views import BookList, BookDetail

urlpatterns = [
    path('book/', BookList.as_view(), name='book_list'),
    path('book/<int:pk>', BookDetail.as_view(), name='book_detail')
]
