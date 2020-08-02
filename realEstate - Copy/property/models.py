from datetime import datetime
from django.db import models
from phone_field import PhoneField

# Create your models here.
PURPOSE = (
    ('SALE', 'Sale'),
    ('RENT', 'Rent')
)

TYPE = (
    ('APARTMENT', 'Apartment'),
    ('HOUSE', 'House'),
    ('OTHERS', 'Others')
)

class Property(models.Model):
    propertyID=models.IntegerField()
    name=models.CharField(max_length=200)
    location=models.CharField(max_length=300)
    street=models.CharField(max_length=500)
    city=models.CharField(max_length=300)
    state=models.CharField(max_length=300)
    zipcode=models.CharField(max_length=50)
    BDS=models.CharField(max_length=5)
    BA=models.CharField(max_length=5)
    price=models.DecimalField(decimal_places=2, max_digits=10)
    purpose=models.CharField(choices=PURPOSE, max_length=20)
    images=models.ImageField(upload_to='properties/%Y/%m/%d',blank=True)
    type=models.CharField(choices=TYPE, max_length=100, default='')
    created=models.DateTimeField(default=datetime.now)
    updated=models.DateTimeField(default=datetime.now)

    class Meta:
        ordering=['-created']
        verbose_name_plural='Properties'

class Contact(models.Model):
    pID = models.ForeignKey(Property, related_name="contacts", on_delete=models.CASCADE, default=0, blank=True)
    agentID=models.IntegerField()
    agentFname=models.CharField(max_length=200)
    agentLname=models.CharField(max_length=200)
    contactNum=PhoneField(blank=True, help_text='Contact phone number')
    emailAddr=models.EmailField(max_length=300)
    requirements=models.CharField(max_length=1000)
    created=models.DateTimeField(default=datetime.now)
    updated=models.DateTimeField(default=datetime.now)

    class Meta:
        ordering=['-created']