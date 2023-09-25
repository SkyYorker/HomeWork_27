import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from avito.models import User, Location
from django.db.models import Count
from django.core.paginator import Paginator
from avito.settings import TOTAL_ON_PAGE


@method_decorator(csrf_exempt, name='dispatch')
class UserListView(ListView):
    model = User
    queryset = User.objects.all()


    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        self.object_list.order_by("-username")
        ads_qs = User.objects.annotate(ads=Count('ad'))
        
        paginator = Paginator(ads_qs, TOTAL_ON_PAGE)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        users = []
        for user in page_obj:
            users.append({
                "id": user.id,
                "username": user.username,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "role": user.role,
                "age": user.age,
                "total_ads": user.ads,
                "locations": [str(u) for u in user.locations.all()]          
            })

        response = {
            "items": users,
            "total": paginator.count,
            "num_pages": paginator.num_pages
        }
        return JsonResponse(response, safe=False)
    

    
class UserDetailView(DetailView):
    model = User
    

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        user = self.get_object()
        
        return JsonResponse({
            "id": user.id,
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "role": user.role,
            "age": user.age,
        })

@method_decorator(csrf_exempt, name='dispatch')
class UserCreateView(CreateView):
    model = User
    fields = ["id", "username", "password", "first_name", "last_name", "role", "age"]

    def post(self, request, *args, **kwargs):

        user_data = json.loads(request.body)
        
        user = User.objects.create(
            username = user_data["username"],
            password = user_data["password"],
            first_name = user_data["first_name"],
            last_name = user_data["last_name"],
            role = user_data["role"],
            age = user_data["age"],
        )
        for loc in user_data['locations']:
            location, _ = Location.objects.get_or_create(name=loc)
            user.locations.add(location)


        return JsonResponse({
        "id": user.id,
        "username": user.username,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "role": user.role,
        "age": user.age,
        "locations": [str(u) for u in user.locations.all()]
    
        })
    

@method_decorator(csrf_exempt, name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    fields = ["id", "username", "password", "first_name", "last_name", "role", "age"]

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        user_data = json.loads(request.body)
        self.object.username = user_data['username']
        self.object.password = user_data['password']
        self.object.first_name = user_data['first_name']
        self.object.last_name = user_data['last_name']
        self.object.age = user_data['age']
        self.object.location = user_data['locations']
        self.object.save()

        return JsonResponse({
        "id": self.object.id,
        "username": self.object.username,
        "first_name": self.object.first_name,
        "last_name": self.object.last_name,
        "role": self.object.role,
        "age": self.object.age,
        "locations": [str(u) for u in self.object.locations.all()]
        })
    

@method_decorator(csrf_exempt, name='dispatch')
class UserDeleteView(DeleteView):
    model = User
    success_url = '/'
 
    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
              
        return JsonResponse({
            "status": "ok"
        })