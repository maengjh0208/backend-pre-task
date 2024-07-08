from django.urls import path, re_path
from .views import ContactAPIView, ContactDetailAPIView

urlpatterns = [
    # post 요청시 URL 마지막에 슬래쉬(/)를 붙이지 않아도 인식할 수 있도록 함
    re_path(r'contacts/?$', ContactAPIView.as_view(), name='contact'),
    path('contacts/<int:contact_id>/', ContactDetailAPIView.as_view(), name='contact-detail'),
]