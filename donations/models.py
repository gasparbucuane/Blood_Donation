from .choices import ChoicesBloodType
from django.db import models
from django.utils import timezone
from datetime import timedelta

class Donor(models.Model):
    BLOOD_TYPE_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]
    
    name = models.CharField(max_length=100)
    identification = models.CharField(max_length=100, unique=True, null=True, blank=True)    
    blood_type = models.CharField(max_length=3, choices=BLOOD_TYPE_CHOICES)
    birth_day = models.DateField()
    def save(self, *args, **kwargs):
        # Save the donor instance
        super().save(*args, **kwargs)
        # Create a new donation instance
        Donation.objects.create(donor=self)

    def __str__(self):
        return self.name
    
class Donation(models.Model):
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE,  related_name='donations')
    created_at = models.DateTimeField(auto_now_add=True)
    next_donation = models.DateTimeField(null=True)
    
    def save(self, *args, **kwargs):
        if not self.id:  # Only set next_donation if this is a new record
             self.next_donation = timezone.now() + timedelta(days=60)
        super(Donation, self).save(*args, **kwargs)
    
    def __str__(self):
        return f"Donation by {self.donor.name} on {self.created_at}"


