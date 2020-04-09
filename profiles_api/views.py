from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    def get(self,request,format=None):

        an_apiview = [
            'user http',
            'similar to a traditional Django View',
            'Gives you the most control over you application logic',
            'is mapped manually to URLs',
        ]

        return Response({'message':'Hello!','an_apiview': an_apiview})