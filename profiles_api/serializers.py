from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """serializers a name field for testing our APIView"""
    # accepts a name input and then we're going to add this to our APIView
    name = serializers.CharField(max_length = 10)
