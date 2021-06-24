
from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = fields = ('username', 'first_name','last_name','email', 'is_staff','is_active')

    def create(self,validated_data):
        user = User.objects.create(**validated_data)
        return user

    def update(self,instance,validated_data):
        instance.username = validated_data.get("username",instance.username)
        instance.first_name = validated_data.get("first_name",instance.first_name)
        instance.last_name = validated_data.get("last_name",instance.last_name)
        instance.email = validated_data.get("email",instance.email)
        instance.is_staff = validated_data.get("is_staff",instance.is_staff)
        instance.is_active = validated_data.get("is_active",instance.is_active)
        instance.save()
        return instance

    
