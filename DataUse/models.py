from django.db import models
from django.contrib.auth.models import User

class DataPull_ID(models.Model):
    TYPE_CHOICES = (
        ('keyword', 'keyword'),
        ('author', 'author'),
    )

    pulldate = models.DateTimeField(auto_now_add=True)
    pullname = models.CharField(max_length=1000)
    pullquery = models.TextField()
    pulltype = models.CharField(max_length=255, choices=TYPE_CHOICES, default='')
    pullsource = models.CharField(max_length=255)
    pullby = models.ForeignKey(User)

    class Meta:
        ordering = ('pulldate',)

class DataPull_Detail(models.Model):
    VALUE_STORE_CHOICES = (
        ('store','store'),
        ('duplicate', 'duplicate'),
        ('false positive', 'false positive')
    )

    pullid = models.ForeignKey(DataPull_ID)
    associatedid = models.CharField(max_length=255)
    valuestore = models.CharField(max_length=255, choices=VALUE_STORE_CHOICES, default='')
    note = models.CharField(max_length=1000, null=True, blank=True, default='')
    pubtype = models.CharField(max_length=255, null=True, blank=True, default='')

class DataPull_Title(models.Model):
    associatedid = models.CharField(max_length=255)
    title = models.CharField(max_length=1000)
    journal = models.CharField(max_length=500)
    publicationdate = models.DateField()
    optionalid01 = models.CharField(max_length=500)
    optionalid02 = models.CharField(max_length=500)

class DataPull_Author(models.Model):
    associatedid = models.CharField(max_length=255)
    forename = models.CharField(max_length=1000)
    lastname = models.CharField(max_length=1000)
    contributortype = models.CharField(max_length=255)
    contributorcontact = models.CharField(max_length=255)
    affiliation = models.TextField()

class DataPull_Keyword(models.Model):
    associatedid = models.CharField(max_length=255)
    keywordvalue = models.CharField(max_length=255)
    category1 = models.CharField(max_length=255)
    category2 = models.CharField(max_length=255)
    category3 = models.CharField(max_length=255)
    category4 = models.CharField(max_length=255)
    category5 = models.CharField(max_length=255)


