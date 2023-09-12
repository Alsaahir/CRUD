from django.shortcuts import render, get_object_or_404
from .models import Person
from django.http import JsonResponse
from .serializers import PersonSerializer

from rest_framework.views import APIView
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import json


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {'GET': 'api/{user_id}/'},
        {'POST': 'api/'},
        {'PUT': 'api/{user_id}/'},
        {'DELETE': 'api/{user_id}'},
        
    ]
    return Response(routes)

class CreateView(APIView):
    queryset = Person.objects.all()
    permission_classes = []
    
    def post(self, request):
            serializer = PersonSerializer(data=request.data)

            if serializer.is_valid():
                email = serializer.validated_data['email']
                person, created = Person.objects.get_or_create(email=email, defaults=serializer.validated_data)
                
                if created:
                    return Response({'message': 'Person created successfully', 'person_id': person.id}, status=status.HTTP_201_CREATED)
                else:
                    return Response({'message': 'Person already exists', 'person_id': person.id}, status=status.HTTP_200_OK)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Crud(APIView):
    queryset = Person.objects.all() 

    permission_classes = []

    def get(self, request, id):
        try:
            person = get_object_or_404(Person, pk=id)
            data = {'id': person.id, 'name': person.name, 'email': person.email}
            return JsonResponse(data)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)


    def put(self, request, id):
        try:
            data = json.loads(request.body)
            person = get_object_or_404(Person, pk=id)
            person.name = data['name']
            if data['email']:
                person.email = data['email']
            else:
                pass
            person.save()
            return JsonResponse({'message': 'Person updated successfully'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    def delete(self, request, id):
        try:
            person = get_object_or_404(Person, pk=id)
            person.delete()
            return JsonResponse({'message': 'Person deleted successfully'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
