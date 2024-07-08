# models.py

from django.db import models


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'User'


class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=255, default='')
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100, default='')
    phone_number = models.CharField(max_length=20, default='')
    company_name = models.CharField(max_length=50, default='')
    company_position = models.CharField(max_length=50, default='')
    memo = models.CharField(max_length=255, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Contact'

    @property
    def labels(self):
        return Label.objects.filter(contactlabel__contact=self)

    @property
    def details(self):
        return ContactDetail.objects.filter(contact=self)


class Label(models.Model):
    label_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    label_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Label'


class ContactLabel(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('contact', 'label'),)
        db_table = 'ContactLabel'


class ContactDetail(models.Model):
    contact_detail_id = models.AutoField(primary_key=True)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    value = models.CharField(max_length=255, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'ContactDetail'
