# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ShortURL
from .serializers import ShortURLSerializer

class ShortURLDetailView(APIView):
    def get(self, request, short_code=None, pk=None):
        if short_code:
            short_url = ShortURL.objects.get(short_code=short_code)
            serializer = ShortURLSerializer(short_url)
            return Response(serializer.data)
        elif pk:
            short_url = ShortURL.objects.get(pk=pk)
            serializer = ShortURLSerializer(short_url)
            return Response(serializer.data)
        else:
            short_urls = ShortURL.objects.all()
            serializer = ShortURLSerializer(short_urls, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = ShortURLSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, short_code=None, pk=None):
        if short_code:
            short_url = ShortURL.objects.get(short_code=short_code)
            serializer = ShortURLSerializer(short_url, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif pk:
            short_url = ShortURL.objects.get(pk=pk)
            serializer = ShortURLSerializer(short_url, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, short_code=None, pk=None):
        if short_code:
            short_url = ShortURL.objects.get(short_code=short_code)
            serializer = ShortURLSerializer(short_url, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif pk:
            short_url = ShortURL.objects.get(pk=pk)
            serializer = ShortURLSerializer(short_url, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, short_code=None, pk=None):
        if short_code:
            short_url = ShortURL.objects.get(short_code=short_code)
            short_url.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        elif pk:
            short_url = ShortURL.objects.get(pk=pk)
            short_url.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
