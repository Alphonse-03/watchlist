from rest_framework import serializers
from api.models import Movie

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name=serializers.CharField()
    description= serializers.CharField()
    viewed = serializers.BooleanField()
    director = serializers.CharField()
    rating = serializers.IntegerField()
    urls = serializers.URLField()

    def create(self,validated_data):
        return Movie.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.description=validated_data.get('description',instance.description)
        instance.viewed=validated_data.get('viewed',instance.viewed)
        instance.save()
        return instance 