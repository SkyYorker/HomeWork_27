import json

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View 
from django.http import JsonResponse
from ads.models import Ads, Categories


@method_decorator(csrf_exempt, name='dispatch')
class AdsView(View):
    def get(self, request):
        ads = Ads.objects.all()
        response = []
        for i in ads:
            response.append({
                "id": i.id,
                "name": i.name,
                "author": i.author,
                "price": i.price
            })
        return JsonResponse(response, safe=False)
    
   
    def post(self, request):
        ads_data = json.loads(request.body)

        ads = Ads.objects.create(
        name = ads_data["name"],
        author = ads_data["author"],
        price = ads_data["price"],
        description = ads_data["description"],
        address = ads_data["address"],
        is_published = ads_data["is_published"],
        )

        return JsonResponse({
        "id": ads.id,
        'name' : ads.name,
        'author' : ads.author,
        'price' : ads.price,
        'description': ads.description,
        'address': ads.address,
        'is_published': ads.is_published
        })


@method_decorator(csrf_exempt, name='dispatch')
class CategoriesView(View):
    def get(self, request):
        cat = Categories.objects.all()
        response = []
        for i in cat:
            response.append({
                "id": i.id,
                "name": i.name,
            })
        return JsonResponse(response, safe=False)


    def post(self, request):
        categories_data = json.loads(request.body)

        categories = Categories.objects.create(
        name = categories_data["name"],
        )

        return JsonResponse({
        "id": categories.id,
        'name' : categories.name,
        })  
    

class AdsEntityView(View):
    def get(self, request, id):
        try:
            ads = Ads.objects.get(pk=id)
        except Ads.DoesNotExist:
            return JsonResponse({"error": "Not found"}, status=404)
        
        return JsonResponse({
            "id": ads.id,
            "name": ads.name,
            "author": ads.author,
            "price": ads.price,
            "description": ads.description,
            "address": ads.address,
            "is_published": ads.is_published
        })
    
class CategoriesEntityView(View):
    def get(self, request, id):
        try:
            ads = Categories.objects.get(pk=id)
        except Categories.DoesNotExist:
            return JsonResponse({"error": "Not found"}, status=404)
        
        return JsonResponse({
            "id": ads.id,
            "name": ads.name,
        })
    
