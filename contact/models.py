from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=212)
    email = models.EmailField()
    subject = models.CharField(max_length=212)
    message = models.TextField()

    def __str__(self):
        return self.name


class ContactInfo(models.Model):
    address = models.CharField(max_length=212)
    phone = models.CharField(max_length=212)
    email = models.EmailField()
    website = models.URLField()

    def __str__(self):
        return self.phone
