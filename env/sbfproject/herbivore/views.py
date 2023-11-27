from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.http import JsonResponse
from herbivore.models import Animal
from herbivore.serializers import AnimalSerializer
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.

class HomeView(View) :
    def get(self, request) :
        return render(request, 'home.html')

@method_decorator(login_required, name='dispatch')
class AnimalView(View) :
    def get(self, request) :
        return render(request, 'animal.html')

class AddAndDeleteAnimalModel(APIView) :
    def get(self, request, id) :
        items = Animal.objects.filter(id = id)
        serializer = AnimalSerializer(items, many = True)
        return JsonResponse(
            data = serializer.data,
            safe = False,
            status = 200
        )
    
    def post(self, request, id) :
        item = Animal.objects.get(id = id)
        serializer = AnimalSerializer(item, data = request.data)
        if serializer.is_valid() :
            serializer.save()
            return JsonResponse(
                data = serializer.data,
                safe = False,
                status = 200
            )
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id) :
        Animal.objects.filter(id = id).delete()
        return JsonResponse(
            data = {
                'message' : 'Animal successfully deleted'
            },
            status = 200
        )
