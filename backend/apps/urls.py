from django.urls import path, re_path
from .views import ContactListAPIView

urlpatterns = [
    # post 요청시 URL 마지막에 슬래쉬(/)를 붙이지 않아도 인식할 수 있도록 함
    re_path(r'contacts/?$', ContactListAPIView.as_view(), name='contact-list'),
    # path('contact/', ContactCreateAPIView.as_view(), name='contact-create'),
]