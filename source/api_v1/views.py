from django.core.serializers import deserialize
from django.shortcuts import render
import json
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.views.generic import View
from django.views.decorators.csrf import ensure_csrf_cookie


@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed('Only GET request are allowed')


def product_create_view(request, *args, **kwargs):
    if request.method == 'POST':
        if request.body:
            product_data = deserialize('json', request.body)
            for item in product_data:
                item.save()
                return JsonResponse({'id': item.object.pk})
        else:
            response = JsonResponse({'error': 'No data provided!'})
            response.status_code = 400
            return response

#         тело запроса
# [{
#   "model": "webapp.product",
#   "fields": {
#     "name": "Test",
#     "category": "food",
#     "price": "100.00",
#     "amount": "2"
#   }
# }]
