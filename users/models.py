from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    """ User Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "남자"),
        (GENDER_FEMALE, "여자"),
        (GENDER_OTHER, "기타"),
    )

    LANGUAGE_ENGLISH = "english"
    LANGUAGE_KOREAN = "korean"
    LANGUAGE_CHINESE = "chinese"

    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, "English"),
        (LANGUAGE_KOREAN, "한국어"),
        (LANGUAGE_CHINESE, "Chinese"),
    )

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICES = (
        (CURRENCY_USD, "USD $"),
        (CURRENCY_KRW, "KRW 원"),
    )

    기타사항 = models.TextField(default="", blank=True)
    프로필_사진 = models.ImageField(null=True, blank=True)
    성별 = models.CharField(choices=GENDER_CHOICES, max_length=10, null=True, blank=True)
    생일 = models.DateField(null=True)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=7, null=True, blank=True
    )
    통화 = models.CharField(choices=CURRENCY_CHOICES, max_length=7, null=True, blank=True)
    할인_혜택_회원 = models.BooleanField(default=False)
