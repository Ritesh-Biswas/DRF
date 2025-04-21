from rest_framework import serializers #type: ignore
from base.models import Item #type: ignore

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'  # This will include all fields in the Item model