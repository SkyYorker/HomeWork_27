import json

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, CreateView, UpdateView
from rest_framework.generics import UpdateAPIView, DestroyAPIView
from django.http import JsonResponse
from rest_framework.generics import ListAPIView


from ads.Serializer import AdSerializer
from ads.models import Ad
from ads.permissions import IsOwnerOrAdminOrModerator
from cat.models import Category
from user.models import User
from rest_framework.permissions import IsAuthenticated




class AdListView(ListAPIView):
    queryset = Ad.objects.all().order_by('-price')
    serializer_class = AdSerializer
    # permission_classes = [IsAuthenticated]

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
            "id": ad.Id,
            'name': ad.name,
            'author_id': author.id,
            "author": author.username,
            'price': ad.price,
            'description': ad.description,
            "is_published": ad_data["is_published"] if "is_published" in ad_data else False,
            'category_id': category.id,
        })


class AdUpdateView(UpdateAPIView):
    model = Ad
    queryset = Ad.objects.all()
    permission_classes = [IsOwnerOrAdminOrModerator]


class AdDeleteView(DestroyAPIView):
    model = Ad
    queryset = Ad.objects.all()
    permission_classes = [IsOwnerOrAdminOrModerator]




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
