from django.db import models
from core import models as core_models


class Review(core_models.TimeStampedModel):

    """ Review Model Definition"""

    review = models.TextField()
    품질 = models.IntegerField()
    배송 = models.IntegerField()
    가격 = models.IntegerField()
    신선도 = models.IntegerField()
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.review} - {self.product.제품이름}"
