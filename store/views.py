from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product

# Create your views here.

@api_view()
def product_list(request):
    product = Product.objects.all()[:5]
    serializer = ProductSerializer(product, many=True)
    return Response(serializer.data)

