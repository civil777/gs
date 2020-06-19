from django.db import models


class TimeStampedModel(models.Model):

    """" Time Stamped Model """

    등록한_날짜 = models.DateTimeField()
    수정한_날짜 = models.DateTimeField()

    class Meta:
        abstract = True
