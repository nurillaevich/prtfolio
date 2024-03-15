from django.urls import path
from .views import (AboutView,
                    ServicesView,
                    PortfolioView,
                    CategoriesView)
urlpatterns = [
    path('', AboutView.as_view(), name='about'),
    path('services/', ServicesView.as_view(), name='services'),
    path('portfolio/', PortfolioView.as_view(), name='portfolio'),
    path('categories/', CategoriesView.as_view(), name='category')
]
