from django.contrib import admin
from . import models


@admin.register(models.Reservation)
class ReservationAdmin(admin.ModelAdmin):

    """ Reservation Admin Definition """

    list_display = (
        "product",
        "status",
        "check_in",
        "check_out",
        "customer",
        "in_progress",
        "is_finished",
    )

    list_filter = ("status",)
