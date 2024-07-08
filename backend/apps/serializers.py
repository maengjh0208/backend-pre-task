from rest_framework import serializers

from .models import Contact, Label


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = ['label_id', 'label_name']


class ContactSerializer(serializers.ModelSerializer):
    labels = LabelSerializer(many=True, read_only=True)

    class Meta:
        model = Contact
        fields = ["contact_id", "user_id", "image_url", "name", "email", "phone_number", "company_name",
                  "company_position", "labels", "created_at", "updated_at"]
