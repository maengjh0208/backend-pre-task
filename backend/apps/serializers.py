# serializers.py

from rest_framework import serializers
from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['contact_id', 'user', 'image_url', 'name', 'email', 'phone_number', 'company_name',
                  'company_position', 'memo', 'created_at', 'updated_at']
