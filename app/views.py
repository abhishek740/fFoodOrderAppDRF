from django.shortcuts import render
from app.models import Menu, Restaurant, User
from django.http import response
from django.shortcuts import render
from rest_framework.views import APIView
# from .serializers import Userseriealizers
from app.serializers import Userseriealizers,ItemSerializer,RestaurantSerializer,OrderSerializer,MenuSerializer
from rest_framework.response import Response
from rest_framework.views import status
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated, AllowAny

# Create your views here.
class SignupApi(APIView):
    # permission_classes = (IsAuthenticated,)

    def post(self,request):
        ser = Userseriealizers(data= request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data,status=status.HTTP_201_CREATED)
        return Response(ser.errors)


# api for add item 
class AddItem(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self,request):
        ser = ItemSerializer(data=request.data)
        if (ser.is_valid()):
            ser.save()
            return Response(ser.data,status= status.HTTP_201_CREATED)

        return Response(ser.errors,status= status.HTTP_400_BAD_REQUEST)

# api for add restaursnt 

class AddRestaurant(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self,request):
        ser = RestaurantSerializer(data=request.data)
        if (ser.is_valid()):
            ser.save()
            return Response(ser.data,status= status.HTTP_201_CREATED)

        return Response(ser.errors,status= status.HTTP_400_BAD_REQUEST)

# api for add menu
class AddMenu(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self,request):
        ser = MenuSerializer(data=request.data)
        if (ser.is_valid()):
            ser.save()
            return Response(ser.data,status= status.HTTP_201_CREATED)

        return Response(ser.errors,status= status.HTTP_400_BAD_REQUEST)

# api for place order
class Placeorder(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self,request):
        ser = OrderSerializer(data=request.data)
        if (ser.is_valid()):
            ser.save()
            return Response(ser.data,status= status.HTTP_201_CREATED)

        return Response(ser.errors,status= status.HTTP_400_BAD_REQUEST)

class ShowMenu(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        id = request.GET.get('id')
        if id is not None:
            menu = Menu.objects.filter(RestaurantName=id)
            ser = MenuSerializer(menu,many=True)
            return Response(ser.data)
        
        resp = {
                'success' : 'false',
                'message' : "Something went wrong try again",      
                }    
        return Response(resp, status=status.HTTP_304_NOT_MODIFIED) 

class ShowItem(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        id = request.GET.get('id')
        if id is not None:
            menu = Menu.objects.filter(id = id)
            ser = MenuSerializer(menu,many=True)
            return Response(ser.data)
        
        resp = {
                'success' : 'false',
                'message' : "Something went wrong try again",      
                }    
        return Response(resp, status=status.HTTP_304_NOT_MODIFIED) 

class ShowAllRestaurant(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        res = Restaurant.objects.all()
        ser = RestaurantSerializer(res,many=True)
        return Response(ser.data)

class DeleteRestaurant(APIView):
    permission_classes = (IsAuthenticated,)
    def delete(self, request):

        id = request.POST.get("id")  
        try:           
            qs = Restaurant.objects.get(id=id).delete()
            if qs:
                resp = {
                    'success' : 'true',
                    'message' : "Restaurant Deleted",
                    }
                return Response(resp, status=status.HTTP_200_OK)
        except:
            resp = {
                'success' : 'false',
                'message' : "Record does not exist",        }    
            return Response(resp, status=status.HTTP_400_BAD_REQUEST) 

class UpdateRestaurant(APIView):
    permission_classes = (IsAuthenticated,)
    def put(self, request):
        id = request.POST.get("id")       
        RestaurantNmame = request.POST.get("RestaurantNmame")
        phoneno = request.POST.get("phoneno")
        address = request.POST.get("address")    
        try: 
            qs = Restaurant.objects.get(id=id)
            if qs:
                qs.RestaurantNmame = RestaurantNmame
                qs.phoneno = phoneno
                qs.price = address
                qs.save()
                resp = {
                    'success' : 'true',
                    'message' : "Restaurant Has Been Successfully Updated",
                }
                return Response(resp, status=status.HTTP_201_CREATED)
        except:

            resp = {
                'success' : 'false',
                'message' : "Something went wrong try again",      
                }    
            return Response(resp, status=status.HTTP_304_NOT_MODIFIED) 