from django.shortcuts import render
from .models import *


def index(request):
    products = Product.objects.all()
    return render(request, 'tz_app/index.html', {'products': products})
