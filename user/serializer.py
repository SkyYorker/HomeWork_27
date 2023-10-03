from rest_framework import serializers

from loc.models import Location
from user.models import User


class UserSerializer(serializers.ModelSerializer):
    locations = serializers.SlugRelatedField(required=False, queryset=Location.objects.all(), many=True,
                                             slug_field='name')

    def is_valid(self, *, raise_exception=False):
        self._locations = self.initial_data.pop('locations')
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        user = User.objects.create(**validated_data)

        for loc in self._locations:
            location, _ = Location.objects.get_or_create(name=loc)
            user.locations.add(location)

        return user

    class Meta:
        model = User
        fields = '__all__'
