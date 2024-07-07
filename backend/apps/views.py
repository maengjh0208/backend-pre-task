from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Contact
from .serializers import ContactSerializer


class ContactAPIView(APIView):
    def get(self, request):
        queryset = Contact.objects.all()
        print('1' * 100)
        print(queryset)
        print('1' * 100)
        serializer = ContactSerializer(queryset, many=True)
        return Response(serializer.data)
