from django import forms
from django_countries.fields import CountryField
from . import models


class SearchForm(forms.Form):

    도로명_주소 = forms.CharField(required=False)
    국가 = CountryField(default="KR").formfield()
    product_type = forms.ModelChoiceField(
        required=False, empty_label="제품 타입", queryset=models.ProductType.objects.all(),
    )
    가격 = forms.IntegerField(required=False)
    customer = forms.IntegerField(required=False)
    남은수량 = forms.IntegerField(required=False)
    규격_및_중량 = forms.IntegerField(required=False)
    할인_혜택_고객용_가격 = forms.IntegerField(required=False)
    할인상품 = forms.BooleanField(required=False)
    무료배송 = forms.BooleanField(required=False)
    facilities = forms.ModelMultipleChoiceField(
        required=False,
        queryset=models.Facility.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
