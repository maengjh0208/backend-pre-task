from rest_framework import serializers

from .models import Contact, Label, ContactDetail, ContactLabel


class ContactDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactDetail
        fields = ["type", "value"]


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = ["label_id", "label_name"]


class ContactSerializer(serializers.ModelSerializer):
    labels = LabelSerializer(many=True, read_only=True)

    class Meta:
        model = Contact
        fields = ["contact_id", "user_id", "image_url", "name", "email", "phone_number", "company_name",
                  "company_position", "created_at", "updated_at", "labels"]


class ContactCreateSerializer(serializers.ModelSerializer):
    details = ContactDetailSerializer(many=True)
    label_ids = serializers.ListField(write_only=True, child=serializers.IntegerField())
    user_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Contact
        fields = ["user_id", "image_url", "name", "email", "phone_number", "company_name", "company_position", "memo",
                  "label_ids", "details"]

    def create(self, validated_data):
        details = validated_data.pop("details")
        label_ids = validated_data.pop("label_ids")

        contact = Contact.objects.create(**validated_data)

        for detail_data in details:
            ContactDetail.objects.create(contact=contact, **detail_data)

        for label_id in label_ids:
            label = Label.objects.get(pk=label_id)
            ContactLabel.objects.create(contact=contact, label=label)

        return contact
