from django.urls import path
from .views import ContactView, ContactInfoView

urlpatterns = [
    path('', ContactView.as_view(), name='contact'),
    path('info/', ContactInfoView.as_view(), name='contact-info')

]
