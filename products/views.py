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

        country = request.GET.get("country")

        if country:

            form = forms.SearchForm(request.GET)

            if form.is_valid():

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
                facilities = form.cleaned_data.get("facilities")

                filter_args = {}

                if city != "Anywhere":
                    filter_args["city__startswith"] = city

                filter_args["country"] = country

                if product_type is not None:
                    filter_args["product_type"] = product_type

                if price is not None:
                    filter_args["price__lte"] = price

                if guests is not None:
                    filter_args["guests__gte"] = guests

                if bedproducts is not None:
                    filter_args["bedproducts__gte"] = bedproducts

                if beds is not None:
                    filter_args["beds__gte"] = beds

                if baths is not None:
                    filter_args["baths__gte"] = baths

                if instant_book is True:
                    filter_args["instant_book"] = True

                if superhost is True:
                    filter_args["host__superhost"] = True

                for amenity in amenities:
                    filter_args["amenities"] = amenity

                for facility in facilities:
                    filter_args["facilities"] = facility

                qs = models.Room.objects.filter(**filter_args).order_by("-created")

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
