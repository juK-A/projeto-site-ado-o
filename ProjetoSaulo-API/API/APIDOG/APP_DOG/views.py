from .serializers import AdotanteSerializer,DogSerializer
from .models import Adotante,Dog
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET']) # Get todos os Adotantes
def getAdotantes(request):
    adotante = Adotante.objects.all()                                      # Get all tasks from database
    serializer = AdotanteSerializer(adotante, many=True)                   # Convert to JSON (serialize)
    return Response(serializer.data, status=status.HTTP_200_OK)     # Return JSON to client

@api_view(['GET']) # Get todos os Dogs 
def getDogs(request):
    dog = Dog.objects.all()                                      # Get all tasks from database
    serializer = DogSerializer(dog, many=True)                   # Convert to JSON (serialize)
    return Response(serializer.data, status=status.HTTP_200_OK)     # Return JSON to client

@api_view(['GET']) # Get para um resultado Adotante
def unigetAdotante(request, id):
    try:
        adotante = Adotante.objects.get(id=id)
        serializer = AdotanteSerializer(adotante, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET']) # Get para um resultado Dog 
def unigetDog(request, id):
    try:
        dog = Dog.objects.get(id=id)
        serializer = DogSerializer(dog, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST']) # Criar um Adotante
def createAdotantes(request):
    serializer = AdotanteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST']) # Criar um Dog
def createDogs(request):
    serializer = DogSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['DELETE'])   # Apagar um Adotante 
def deleteAdotante(request, id):
    try:
        adotante = Adotante.objects.get(id=id)
        adotante.delete()
        return Response(status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['DELETE'])   # Apagar um Dog 
def deleteDog(request, id):
    try:
        dog = Dog.objects.get(id=id)
        dog.delete()
        return Response(status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])  # editar adotante
def editAdotante(request, id):
    try:
        adotante = Adotante.objects.get(id=id)
        serializer = AdotanteSerializer(instance=adotante, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['PUT'])  # editar um Dog 
def editDog(request, id):
    try:
        dog = Dog.objects.get(id=id)
        serializer = DogSerializer(instance=dog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
