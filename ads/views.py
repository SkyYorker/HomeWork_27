import json

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import JsonResponse
from rest_framework.generics import ListAPIView


from ads.Serializer import AdSerializer
from ads.models import Ad
from avito.settings import TOTAL_ON_PAGE
from cat.models import Category
from user.models import User





class AdListView(ListAPIView):
    queryset = Ad.objects.all().order_by('-price')
    serializer_class = AdSerializer

    def get(self, request, *args, **kwargs):
        cat = request.GET.getlist("cat", None)
        text = request.GET.get("text", None)
        location = request.GET.get("location")
        price_from = request.GET.get("price_from")
        price_to = request.GET.get("price_to")
        if cat:
            self.queryset = self.queryset.filter(
                category__id__in=cat
            )
        if text:
            self.queryset = self.queryset.filter(
                name__icontains=text
            )
        if location:
            self.queryset = self.queryset.filter(
                author__locations__name__icontains=location
            )
        if price_from:
            self.queryset = self.queryset.filter(
                price__gte=price_from
            )
        if price_to:
            self.queryset = self.queryset.filter(
                price__lte=price_to
            )
        return super().get(self, *args, **kwargs)

# @method_decorator(csrf_exempt, name='dispatch')
# class AdListView(ListView):
#     model = Ad
#     queryset = Ad.objects.all()
#
#     def get(self, request, *args, **kwargs):
#         super().get(request, *args, **kwargs)
#         self.object_list.order_by("-price")
#         total_ads = self.object_list.count()
#
#         page = int(request.GET.get("page", 0))
#         offset = page * TOTAL_ON_PAGE
#         if offset > total_ads:
#             self.object_list = []
#         elif offset:
#             self.object_list = self.object_list[offset:TOTAL_ON_PAGE]
#         else:
#             self.object_list = self.object_list[:TOTAL_ON_PAGE]
#
#         ads = []
#         for i in self.object_list:
#             ads.append({
#                 "name": i.name,
#                 "price": i.price,
#                 "description": i.description,
#                 "is_published": i.is_published,
#                 "author_id": i.author_id,
#                 'author': i.author.first_name,
#                 "category_id": i.category_id
#             })
#
#         response = {
#             "items": ads,
#             "total": total_ads,
#             "per_page": TOTAL_ON_PAGE
#         }
#         return JsonResponse(response, safe=False)


class AdDetailView(DetailView):
    model = Ad

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        ad = self.get_object()
        return JsonResponse({
            "id": ad.Id,
            "name": ad.name,
            "price": ad.price,
            "description": ad.description,
            "is_published": ad.is_published,
            "image": ad.image,
            "author_id": ad.author_id,
            "category_id": ad.category_id
        })


@method_decorator(csrf_exempt, name='dispatch')
class AdCreateView(CreateView):
    model = Ad
    fields = ["Id", "name", "price", "description", "is_published", "image", "author_id", "category_id"]

    def post(self, request, *args, **kwargs):
        ad_data = json.loads(request.body)
        author = get_object_or_404(User, id=ad_data["author_id"])
        category = get_object_or_404(Category, id=ad_data['category_id'])

        ad = Ad.objects.create(
            name=ad_data["name"],
            author_id=author.id,
            price=ad_data["price"],
            description=ad_data["description"],
            category_id=category.id,
        )

        return JsonResponse({
            "id": ad.id,
            'name': ad.name,
            'author_id': author.id,
            "author": author.username,
            'price': ad.price,
            'description': ad.description,
            "is_published": ad_data["is_published"] if "is_published" in ad_data else False,
            'category_id': category.id,
        })


@method_decorator(csrf_exempt, name='dispatch')
class AdUpdateView(UpdateView):
    model = Ad
    fields = ["Id", "name", "price", "description", "is_published", "image", "author", "category"]

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        ad_data = json.loads(request.body)
        self.object.name = ad_data['name']
        self.object.author_id = ad_data['author_id']
        self.object.price = ad_data["price"]
        self.object.description = ad_data['description']
        self.object.category_id = ad_data['category_id']
        self.object.save()

        return JsonResponse({
            "id": self.object.Id,
            'name': self.object.name,
            'author_id': self.object.author_id,
            "author": self.object.author.username,
            'price': self.object.price,
            'description': self.object.description,
            "is_published": self.object["is_published"] if "is_published" in ad_data else False,
            'category_id': self.object.category_id,
        })


@method_decorator(csrf_exempt, name='dispatch')
class AdDeleteView(DeleteView):
    model = Ad
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({
            "status": "ok"
        })


@method_decorator(csrf_exempt, name='dispatch')
class AdUploadImageView(UpdateView):
    model = Ad
    fields = ['image']

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.image = request.FILES.get('image')
        self.object.save()

        return JsonResponse({
            "id": self.object.Id,
            'name': self.object.name,
            'price': self.object.price,
            'description': self.object.description,
            'is_published': self.object.is_published,
            "author": self.object.author.username,
            "image": self.object.image.url,
            'category': self.object.category.name
        })
