from django.db import models


class TimeStampedModel(models.Model):

    """" Time Stamped Model """

    등록한_날짜 = models.DateTimeField(auto_now_add=True)
    수정한_날짜 = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
