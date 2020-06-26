from django.shortcuts import render
from django.http import HttpResponse


def all_products(request):
    return HttpResponse(content="it's work!")
