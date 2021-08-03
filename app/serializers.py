from rest_framework import serializers,fields
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
from .models import *

class Userseriealizers(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only = True,required= True,
        validators = [validate_password]
    )
    confirm_password = serializers.CharField(write_only = True,required= True)
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    username = serializers.CharField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])


    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password',
            'confirm_password',
            'phone_no'
        )

    def validate(self,attrs):
        if attrs['password']!=attrs['confirm_password']:
            raise serializers.ValidationError({'password':'password did not match'})
        return attrs

    def create(self,validate_data):
        user=User.objects.create(
            username = validate_data['username'],
            email = validate_data['email'],
            phone_no = validate_data['phone_no'],
        )

        user.set_password(validate_data['password'])
        user.save()
        return user

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'