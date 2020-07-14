from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from api.models import Book


# csrf_token 豁免
@csrf_exempt
def book(request):
    if request.method == 'GET':
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

    elif request.method == 'POST':
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


@csrf_exempt
def books(request, bookid):
    if request.method == 'GET':
        book_obj = Book.objects.get(pk=bookid)

        data = {
            'status': 200,
            'msg': 'ok',
            'data': book_obj.to_dict(),
        }

    elif request.method == 'DELETE':
        book_obj = Book.objects.get(pk=bookid)
        book_obj.delete()

        data = {
            'status': 204,
            'msg': 'delete success',
            # 'data': {},
        }

    return JsonResponse(data=data, status=204)
