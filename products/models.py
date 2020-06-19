from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models


class Product(core_models.TimeStampedModel):

    """ Product Model Definition """

    제품이름 = models.CharField(max_length=140)
    설명 = models.TextField()
    국가 = CountryField()
    도로명_주소 = models.CharField(max_length=80)
    상세주소 = models.CharField(max_length=150)
    가격 = models.IntegerField()
    할인_혜택_고객용_가격 = models.IntegerField()
    남은_수량 = models.IntegerField()
    규격_및_중량 = models.CharField(max_length=80)
    원산지 = models.CharField(max_length=80)
    무료배송 = models.BooleanField(default=False)
    생산날짜 = models.TimeField()
    유통기한 = models.TimeField()
    생산자 = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
