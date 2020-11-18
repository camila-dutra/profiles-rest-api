from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status  # is a list of handy HTTP status codes that you can use when returning response from your API
from rest_framework import viewsets

from profiles_api import serializers

class HelloApiView(APIView):
    """Test API View"""
    serializer_class= serializers.HelloSerializer # this configures our APIView to have the serializer class that we created, to validate the input data when you are sendind a post, patch or put request

    def get(self, request, format=None):   #self: required for all class functions, request object passed by the django rest framework, contains details of the request being made to the API, format is used to add a format suffix to the end of the endpoint URL
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview}) # response needs to contain a dictionary or a list which it will then output when the API is called, so it converts the response object to json


    def post(self, request):
        """Create a hello message with our name"""
        serializer =  self.serializer_class(data=request.data)  # serializer_class is a class that cames with the APIView that retrieves the serializer class for our view

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message' : message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating objects"""
        return Response({'method' : 'PUT' })


    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method' : 'PATCH' })


    def delete(self, request, pk=None):
          """Delete an object"""
          return Response({'method' : 'DELETE' })


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class= serializers.HelloSerializer


    def list(self, request):
        """Return a hello message"""
        a_viewset = [
            'Uses actions(list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers ',
            'Provides more functionality with less code',
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})


    def create(self, request):
        """Create a new hello message"""
        serializer =  self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message' : message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting and object by its ID """
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle UPDATING an object"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle UPDATING PART of an object"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle REMOVING an object"""
        return Response({'http_method': 'DELETE'})
