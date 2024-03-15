from django.shortcuts import render
from .models import ContactInfo, Contact
from .serializers import ContactSerializer, ContactInfoSerializer
from rest_framework import generics


class ContactView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactInfoView(generics.ListAPIView):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer
