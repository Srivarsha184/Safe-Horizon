'''from django.db import models

class login(models.Model):
    email_id = models.EmailField()
    password = models.CharField(max_length=128,help_text="Your password must be at least 6 characters long.")'''
'''
from django.db import models

from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    college_name = models.CharField(max_length=100)
    college_id = models.CharField(max_length=50)
    address = models.TextField()
    qualification = models.CharField(max_length=50, choices=[('UG', 'Under Graduate'), ('PG', 'Post Graduate')])
    graduation_year = models.IntegerField(choices=[(year, year) for year in range(2024, 2030)])
    roll_number = models.CharField(max_length=50)

# Create your models here.
class Report(models.Model):
    date=models.DateField()
    place=models.CharField(max_length=200)
    description=models.TextField()
    severity = models.CharField(max_length=10)
    def __str__(self):
        return f"Incident reported by {self.name} on {self.date}"
'''
# from django.contrib.auth.models import User
# from django.db import models

# class UserProfile(models.Model):
#     username = models.OneToOneField(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     phone = models.CharField(max_length=10)
#     clgname = models.CharField(max_length=100)
#     clgid = models.CharField(max_length=6)
#     clgaddress = models.TextField()
#     qualification = models.CharField(max_length=50, choices=[('UG', 'Under Graduate'), ('PG', 'Post Graduate')])
#     gradyear = models.IntegerField(choices=[(year, year) for year in range(2024, 2030)])
#     roll = models.CharField(max_length=50)


from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    clgname = models.CharField(max_length=100)
    clgid = models.CharField(max_length=50)
    clgaddress = models.CharField(max_length=200)
    qualification = models.CharField(max_length=50)
    gradyear = models.IntegerField()
    roll = models.CharField(max_length=20)
    # Add other fields as needed


from django.db import models
from django.contrib.auth.models import User

class Incident(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='incidents', verbose_name='Reported By')
    date = models.DateField(verbose_name='Date of the incident')
    location = models.CharField(max_length=100, verbose_name='Location of the incident')
    description = models.TextField(verbose_name='Incident Description')
    victim_injury = models.CharField(max_length=3, choices=(('yes', 'Yes'), ('no', 'No')), verbose_name='Is the Individual Injured')
    witness_present = models.CharField(max_length=3, choices=(('yes', 'Yes'), ('no', 'No')), verbose_name='Is there a Witness Present')
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"Incident on {self.date} at {self.location} reported by {self.user.username}"
