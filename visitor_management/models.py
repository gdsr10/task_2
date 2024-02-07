from django.db import models
from django.utils import timezone

# Create your models here.
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
        
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    office_location = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Visitor(models.Model):
    # Define choices for visitor status
    WAITING_FOR_CHECK_IN = 'Waiting for Check in'
    INSIDE_BUILDING = 'Inside Building'
    CHECKED_OUT = 'Checked Out'
    STATUS_CHOICES = [
        (WAITING_FOR_CHECK_IN, 'Waiting for Check in'),
        (INSIDE_BUILDING, 'Inside Building'),
        (CHECKED_OUT, 'Checked Out'),
    ]

    # Define model fields
    name = models.CharField(max_length=100)
    email = models.EmailField()
    office_location = models.CharField(max_length=100)
    employee_visiting = models.ForeignKey(Employee, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
