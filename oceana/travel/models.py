from django.db import models

from django.core.validators import RegexValidator

class Guest(models.Model):
    name=models.CharField(max_length=100)
    phone_pattern = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+91'. Up to 1o digits")
    phone = models.CharField(validators=[phone_pattern],max_length=30)
    email=models.EmailField(max_length=75)

    def __unicode__(self):
        return str(self.name)

class Enquiry(models.Model):
    guest=models.ForeignKey(Guest)
    address=models.TextField()
    travel_time=models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_time=models.DateTimeField(auto_now_add=False,auto_now=True)

    def __unicode__(self):
        return str(self.guest.id)
    
        
