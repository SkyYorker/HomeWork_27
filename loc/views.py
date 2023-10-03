from rest_framework import viewsets

from loc.models import Location
from loc.serializer import LocationSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer