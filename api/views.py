from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from project.models import Book
from api.serializers import BookSerializer


class BookList(APIView):
    def get(self, request):
        books = Book.objects.all()[:20]
        data = BookSerializer(books, many=True).data
        return Response(data)

class BookDetail(APIView):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        data = BookSerializer(book).data
        return Response(data)
