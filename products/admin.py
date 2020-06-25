# from django.contrib import admin
# from . import models

# @admin.register(models.ProductType, models.Facility)
# class ItemAdmin(admin.ModelAdmin):

#     """ Item Admin Definition """

#     list_display = ("제품이름", "used_by")

#     def used_by(self, obj):
#         return obj.products.count()

#     pass


# @admin.register(models.Product)
# class ProductAdmin(admin.ModelAdmin):

#     """ Produt Admin Definition """

#     pass


# @admin.register(models.Photo)
# class PhotoAdmin(admin.ModelAdmin):

#     pass

from django.contrib import admin
from django.utils.html import mark_safe
from . import models


@admin.register(models.Facility)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.products.count()

    pass


class PhotoInline(admin.TabularInline):

    model = models.Photo


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):

    """ Product Admin Definition """

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("제품이름", "설명", "국가", "도로명_주소", "상세주소", "가격", "할인_혜택_고객용_가격")},
        ),
        ("Times", {"fields": ("생산날짜", "유통기한", "무료배송")}),
        ("Numbers", {"fields": ("남은_수량", "규격_및_중량", "원산지")}),
        (
            "More About the Space",
            {"classes": ("collapse",), "fields": ("제품_종류", "facilities",),},
        ),
        ("Last Details", {"fields": ("판매자",)}),
    )

    list_display = (
        "제품이름",
        "국가",
        "도로명_주소",
        "가격",
        "할인_혜택_고객용_가격",
        "상세주소",
        "남은_수량",
        "규격_및_중량",
        "원산지",
        "무료배송",
        "생산날짜",
        "유통기한",
        "생산자",
        "제품_종류",
        "total_rating",
    )

    list_filter = (
        "무료배송",
        "할인_혜택_고객용_가격",
        "제품_종류",
        "가격",
        "facilities",
        "국가",
        "도로명_주소",
        "상세주소",
    )

    search_fields = (
        "=도로명_주소",
        "^판매자__username",
        "제품이름",
    )

    raw_id_fields = ("판매자",)
    search_fields = ("=도로명_주소", "^판매자__username")
    filter_horizontal = ("facilities",)

    def count_photos(self, obj):
        return obj.photos.count()


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Phot Admin Definition """

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}" />')

    get_thumbnail.short_description = "Thumbnail"
