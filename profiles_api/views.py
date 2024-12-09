from rest_framework.views import APIView
from rest_framework.response import Response


class HelloAPiView(APIView):
    """Test API View"""
    def get(self, request, format=None):
        """Returns a list of Api View features"""
        an_apiview = [
            "perfect for implementing complex logics",
            "calling other apis",
            "working with local files",
            "Is mapped manually to the urls"
        ]
        return Response({"message":"hello", "an_apiview": an_apiview})
