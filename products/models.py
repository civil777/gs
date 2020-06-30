from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from django.urls import reverse


class AbstractItem(core_models.TimeStampedModel):

    """ Abstract Item """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class ProductType(AbstractItem):

    """ ProductType Model Definition """

    class Meta:
        verbose_name = "Product Type"


class Facility(AbstractItem):

    """ Facility Model Definition """

    pass

    class Meta:
        verbose_name_plural = "Facilities"


class Photo(core_models.TimeStampedModel):

    """ Photo Model Definition """

    caption = models.CharField(max_length=150)
    file = models.ImageField(upload_to="product_photos")
    product = models.ForeignKey("Product", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class Product(core_models.TimeStampedModel):

    """ Product Model Definition """

    제품이름 = models.CharField(max_length=140)
    설명 = models.TextField()
    국가 = CountryField(default="KR")
    도로명_주소 = models.CharField(max_length=80)
    상세주소 = models.CharField(max_length=150)
    가격 = models.IntegerField()
    할인_혜택_고객용_가격 = models.IntegerField()
    남은_수량 = models.IntegerField()
    규격_및_중량 = models.CharField(max_length=80)
    원산지 = CountryField(default="KR")
    무료배송 = models.BooleanField(default=False)
    생산날짜 = models.TimeField()
    유통기한 = models.TimeField()
    # 판매자 = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    생산자 = models.ForeignKey(
        "users.User", related_name="products", on_delete=models.CASCADE
    )
    # 제품_종류 = models.ManyToManyField(ProductType, blank=True)
    제품_종류 = models.ForeignKey(
        "ProductType",
        related_name="products",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    facilities = models.ManyToManyField("Facility", related_name="products", blank=True)

    def __str__(self):
        return self.제품이름

    def get_absolute_url(self):
        return reverse("products:detail", kwargs={"pk": self.pk})

    def total_rating(self):
        all_reviews = self.reviews.all()
        all_ratings = 0
        if len(all_reviews) > 0:
            for review in all_reviews:
                all_ratings += review.rating_average()
            return round(all_ratings / len(all_reviews), 2)
        return 0
