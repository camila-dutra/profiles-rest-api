from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):   #self: required for all class functions, request object passed by the django rest framework, contains details of the request being made to the API, format is used to add a format suffix to the end of the endpoint URL
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview}) # response needs to contain a dictionary or a list which it will then output when the API is called, so it converts the response object to json
