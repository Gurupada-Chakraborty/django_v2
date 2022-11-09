from rest_framework import serializers
from decimal import Decimal


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    unit_price = serializers.DecimalField(max_digits=6, decimal_places=2)
    # customizing serializers field
    unit_price_tax = serializers.SerializerMethodField(method_name='tax')

    def tax(self, product):
        return product.unit_price * Decimal(1.1)
    