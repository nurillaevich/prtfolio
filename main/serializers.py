from rest_framework import serializers
from .models import About, Categories, Services, Portfolio


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'


class PortfolioSerializer(serializers.ModelSerializer):
    category = CategoriesSerializer(many=True)

    class Meta:
        model = Portfolio
        fields = ['id', 'title', 'description', 'image', 'category']
