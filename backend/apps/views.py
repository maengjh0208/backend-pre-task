from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Contact
from .serializers import ContactSerializer


class CustomPagination(PageNumberPagination):
    # 데이터는 3개씩 호출. 그리고 존재하지 않는 페이지 호출시 에러가 아닌 빈 리스트 반환하도록 설정
    page_size = 3

    def paginate_queryset(self, queryset, request, view=None):
        try:
            return super().paginate_queryset(queryset, request, view=view)
        except NotFound:
            return []


class ContactListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        user_id = request.query_params.get("user_id")
        sort = request.query_params.get("sort", None)
        order = request.query_params.get("order", "asc")

        # 기본 정렬
        if sort not in ["name", "email", "phone_number"]:
            sort = 'created_at'
        # 이름, 이메일, 전화번호 중 하나 선택하여 정렬 가능
        else:
            # 정렬 순서 중에 오름차순/내림차순/해제순이 있는데 해제순이 뭘 의미하는지 모르겠음 (일단 패스)
            sort = sort if order == "asc" else f"-{sort}"

        # 원래라면 회원번호를 query_params가 아닌 token 등으로 판별하겠으나, 회원 기능 따로 구현하지 않아서 임시 대응
        if not user_id:
            return Response(
                data={"error_message": "user_id is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        contacts = Contact.objects.filter(user_id=int(user_id)).order_by(sort)

        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(contacts, request)
        serializer = ContactSerializer(result_page, many=True)

        # 스크롤로 데이터가 더이상 존재하지 않을때까지 호출해주는 거니까 Response 사용해도 될 것 같음
        # return paginator.get_paginated_response(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)
