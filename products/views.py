from django.shortcuts import render


def all_products(request):
    return render(request, "all_products.html")
