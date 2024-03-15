from .models import Portfolio, About, Categories, Services
from .serializers import (ServicesSerializer,
                          PortfolioSerializer,
                          AboutSerializer,
                          CategoriesSerializer)
from rest_framework import generics


class AboutView(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class CategoriesView(generics.ListAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


class ServicesView(generics.ListAPIView):
    queryset = Services.objects.all()[:4]
    serializer_class = ServicesSerializer


class PortfolioView(generics.ListAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

    def get_queryset(self):
        title = self.request.query_params.get('title')
        cat = self.request.query_params.get('category')
        if title is not None:
            return Portfolio.objects.filter(title__icontains=title)
        if cat is not None:
            return Portfolio.objects.filter(category__name__icontains=cat)

        else:
            return Portfolio.objects.all()


