from rest_framework import serializers
from .models import Person, Post


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = (
            'id',
            'name',
            'title',
            'created_on'
        )
