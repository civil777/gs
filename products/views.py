from django.views.generic import ListView, DetailView, View
from django.shortcuts import render
from django.core.paginator import Paginator
from . import models, forms


class HomeView(ListView):

    """ HomeView Definition """

    model = models.Product
    paginate_by = 10
    paginate_orphans = 5
    ordering = "등록한_날짜"
    context_object_name = "products"


class ProductDetail(DetailView):

    """ ProductDetail Definition """

    model = models.Product


class SearchView(View):

    """ SearchView Definition """

    def get(self, request):

        제품이름 = request.GET.get("제품이름")

        if 제품이름:

            form = forms.SearchForm(request.GET)

            if form.is_valid():

                제품이름 = form.cleaned_data.get("제품이름")
                city = form.cleaned_data.get("city")
                country = form.cleaned_data.get("country")
                product_type = form.cleaned_data.get("product_type")
                price = form.cleaned_data.get("price")
                guests = form.cleaned_data.get("guests")
                bedproducts = form.cleaned_data.get("bedproducts")
                beds = form.cleaned_data.get("beds")
                baths = form.cleaned_data.get("baths")
                instant_book = form.cleaned_data.get("instant_book")
                superhost = form.cleaned_data.get("superhost")
                amenities = form.cleaned_data.get("amenities")

                도로명_주소 = form.cleaned_data.get("도로명_주소")
                국가 = form.cleaned_data.get("국가")
                product_type = form.cleaned_data.get("product_type")
                가격 = form.cleaned_data.get("가격")
                customer = form.cleaned_data.get("customer")
                남은수량 = form.cleaned_data.get("남은수량")
                규격_및_중량 = form.cleaned_data.get("규격_및_중량")
                할인_혜택_고객용_가격 = form.cleaned_data.get("할인_혜택_고객용_가격")
                할인상품 = form.cleaned_data.get("할인상품")
                무료배송 = form.cleaned_data.get("무료배송")
                facilities = form.cleaned_data.get("facilities")

                filter_args = {}

                # if city != "Anywhere":
                #     filter_args["city__startswith"] = city

                # filter_args["country"] = country

                if 가격 is not None:
                    filiter_args["가격"] = 가격

                if product_type is not None:
                    filter_args["product_type"] = product_type

                if price is not None:
                    filter_args["가격__lte"] = 가격

                if customer is not None:
                    filter_args["customer__gte"] = customer

                if 남은수량 is not None:
                    filter_args["남은수량__gte"] = 남은수량

                if 규격_및_중량 is not None:
                    filter_args["규격_및_중량__gte"] = 규격_및_중량

                if 할인_혜택_고객용_가격 is not None:
                    filter_args["할인_혜택_고객용_가격__gte"] = 할인_혜택_고객용_가격

                if 무료배송 is True:
                    filter_args["무료배송"] = True

                if 할인상품 is True:
                    filter_args["할인상품"] = True

                # for amenity in amenities:
                #     filter_args["amenities"] = amenity

                for facility in facilities:
                    filter_args["facilities"] = facility

                qs = models.Product.objects.filter(**filter_args).order_by("-생산날짜")

                paginator = Paginator(qs, 10, orphans=5)

                page = request.GET.get("page", 1)

                products = paginator.get_page(page)

                return render(
                    request,
                    "products/search.html",
                    {"form": form, "products": products},
                )

        else:
            form = forms.SearchForm()

        return render(request, "products/search.html", {"form": form})
