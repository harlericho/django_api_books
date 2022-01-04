from django.http.response import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from .models import Book
import json
# Create your views here.
# class
class BookView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(BookView, self).dispatch(request, *args, **kwargs)

    def get(self, request, pk=0):
        if pk > 0:
            dataListId = list(Book.objects.filter(id=pk).values())
            if len(dataListId) > 0:
                file = dataListId[0]
                data = {'message': 'Success', 'data': file}
            else:
                data = {'message': 'Not found', 'data': {}}
            return JsonResponse(data)
        else:
            dataList = list(Book.objects.all().values())
            if len(dataList) > 0:
                data = {'message': 'Success', 'data': dataList}
            else:
                data = {'message': 'Not found', 'data': dataList}
            return JsonResponse(data)

    def post(self, request):
        data = json.loads(request.body)
        Book.objects.create(
            title=data['title'],
            author=data['author'],
            price=data['price']
        )
        data = {'message': 'Success'}
        return JsonResponse(data)
    
    def put(self, request, pk):
        data = json.loads(request.body)
        dataListId = list(Book.objects.filter(id=pk).values())
        if len(dataListId) > 0:
            Book.objects.filter(id=pk).update(
            title=data['title'],
            author=data['author'],
            price=data['price']
            )
            data = {'message': 'Success'}
        else:
            data = {'message': 'Not found', 'data': {}}
        return JsonResponse(data)
    
    def delete(self, request, pk):
        dataListId = list(Book.objects.filter(id=pk).values())
        if len(dataListId) > 0:
            Book.objects.filter(id=pk).delete()
            data = {'message': 'Success'}
            return JsonResponse(data)
        else:
            data = {'message': 'Not found', 'data': {}}
            return JsonResponse(data)