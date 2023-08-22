from django.shortcuts import render
from django.views import View 
from django.http import JsonResponse


class Ads_VIew(View):
    def get(self,request, *args, **kwargs):
        response_json = {
            "status": "ok"
        }
        return JsonResponse(response_json, safe=False)
