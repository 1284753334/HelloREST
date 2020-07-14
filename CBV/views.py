from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
# 基于类的视图函数，类可以继承
from django.views import View
# 基于函数的视图函数  继承系统的包
from CBV.models import Book


class HelloCBV(View):

    msg = None

    def get(self, request):
        # 逻辑可以写在类里面

        return HttpResponse('hahaha  %s'% self.msg)

    def post(self, request):
        return HttpResponse('post 555')

    def put(self, request):
        return HttpResponse('put 555')


class BookCBV(View):
    def get(self, request):
        book_list = Book.objects.all()

        # book_list= serializers.serialize("json", book_list)
        #
        book_list_json = []
        for book in book_list:
            book_list_json.append(book.to_dict())
        data = {
            'status': 200,
            'msg': 'ok',
            'data': book_list_json,
        }
        return JsonResponse(data=data)

    def post(self, request):
        b_name = request.POST.get('b_name')
        b_price = request.POST.get('b_price')
        book = Book()
        book.b_name = b_name
        book.b_price = b_price
        book.save()
        data = {
            'status': 201,
            'msg': 'add success',
            'data': book.to_dict(),
        }

        return JsonResponse(data=data)
