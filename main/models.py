from django.db import models


class About(models.Model):
    name = models.CharField(max_length=212)
    profession = models.TextField()
    image = models.ImageField(upload_to='about')
    instagram = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=212)

    def __str__(self):
        return self.name


class Services(models.Model):
    image = models.ImageField(upload_to='services')
    title = models.CharField(max_length=212)
    description = models.TextField()

    def __str__(self):
        return self.title


class Categories(models.Model):
    name = models.CharField(max_length=212)

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    title = models.CharField(max_length=212)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolios')
    category = models.ManyToManyField(Categories)
    resume = models.FileField(upload_to='resume', null=True, blank=True)

    def __str__(self):
        return self.title
