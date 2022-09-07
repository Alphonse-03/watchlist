from rest_framework import serializers
from api.models import Movie,StreamPlatform

# def validate_length(data):
#     if len(data)<2:
#         raise serializers.ValidationError("lenght too short")
#     return data
class StreamPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model=StreamPlatform
        fields="__all__"

    def validate(self, data):
        if len(data)<2:
            raise serializers.ValidationError("lenght too short")
        return data


class MovieSerializer(serializers.ModelSerializer):
    len_name=serializers.SerializerMethodField()

    class Meta:
        model=Movie
        exclude=['id']
    
    def get_len_name(self,object):
        return len(object.name)

    def validate(self, data):
        if data['name']==data['description']:
            raise serializers.ValidationError("same name and description exists")
        
        x=Movie.objects.filter(name=data['name'])
        if len(x)>0:
            raise serializers.ValidationError("Same name movie already exists")

        return data




# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name=serializers.CharField(validators=[validate_length])
#     description= serializers.CharField()
#     viewed = serializers.BooleanField()
#     director = serializers.CharField()
#     rating = serializers.IntegerField()
#     urls = serializers.URLField()

#     def create(self,validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self,instance,validated_data):
#         instance.name=validated_data.get('name',instance.name)
#         instance.description=validated_data.get('description',instance.description)
#         instance.viewed=validated_data.get('viewed',instance.viewed)
#         instance.save()
#         return instance 

#     def validate(self, data):
#         if data['name']==data['description']:
#             raise serializers.ValidationError("same name and description exists")
        
#         x=Movie.objects.filter(name=data['name'])
#         if len(x)>0:
#             raise serializers.ValidationError("Same name movie already exists")

#         return data
    