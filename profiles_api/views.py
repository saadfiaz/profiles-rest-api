from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets

from profiles_api import serializers


class HelloAPiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer
    def get(self, request, format=None):
        """Returns a list of Api View features"""
        an_apiview = [
            "perfect for implementing complex logics",
            "calling other apis",
            "working with local files",
            "Is mapped manually to the urls"
        ]
        return Response({"message":"hello", "an_apiview": an_apiview})

    def post(self, request):
        """Create a Hello Message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({"message":message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle Updating an object"""
        return Response({"method": "PUT"})

    def patch(self, request, pk=None):
        """Handle a partial update of  an object"""
        return Response({"method": "PATCH"})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({"method": "DELETE"})


class HelloViewSet(viewsets.ViewSet):
    """Test API viewsets"""
    serializer_class = serializers.HelloSerializer
    def list(self, request):
        """Returns a Hello Message"""
        a_viewset = [
            "Uses Actions (list, create, retrive, update, partial_update)",
            "Automatically mapes to URLS using Routers",
            "Provides more functionality with less code"
        ]

        return Response({"message": "Hello", "a_viewset":a_viewset})

    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    def retrive(self, request, pk=None):
        """Handle Getting an object with it id"""
        return Response({"http_method": "GET"})

    def update(self, request, pk=None):
        """Handle Updating an object"""
        return Response({"http_method":"PUT"})

    def partial_update(self, request, pk=None):
        """Handle Updating part of an object"""
        return Response({"http_method":"PATCH"})

    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({"http_method":"DELETE"})
