import re

from rest_framework.exceptions import ValidationError
from rest_framework.request import Request

from .models import User


def is_valid_email(email: str) -> bool:
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None


def is_valid_phone_number(phone_number: str) -> bool:
    phone_regex = r'^(01[016789]|02)-?\d{3,4}-?\d{4}$'
    return re.match(phone_regex, phone_number) is not None


def validate_user_id(user_id: str) -> int:
    if not user_id:
        raise ValidationError("user_id is required")
    if not user_id.isdigit():
        raise ValidationError("user_id must be an integer")

    try:
        User.objects.get(pk=user_id)
    except:
        raise ValidationError("user_id doest not exist")

    return int(user_id)


def validate_create_contact(request: Request):
    user_id = str(request.data.get("user_id"))
    email = request.data.get("email")
    phone_number = request.data.get("phone_number")

    # 유저 아이디 검사
    validate_user_id(user_id)

    # 이메일 유효성 검사
    if not is_valid_email(email):
        raise ValidationError("invalid email format")

    # 휴대폰 유효성 검사
    if not is_valid_phone_number(phone_number):
        raise ValidationError("invalid phone_number format")
