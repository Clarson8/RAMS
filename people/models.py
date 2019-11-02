from django.db import models
from location.models import Location

# Create your models here.
class Person(Location):
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    home_phone = models.CharField(max_length=50, blank=True, null=True)
    work_phone = models.CharField(max_length=50, blank=True, null=True)
    cell_phone = models.CharField(max_length=50, blank=True, null=True)
    best_contact = models.TextField(blank=True, null=True)
    drivers_license = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

class Owner(Person):

    @property
    def location_type(self):
        return 'owner'

class Reporter(Person):

    @property
    def location_type(self):
        return 'reporter'

class TeamMember(models.Model):

    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    cell_phone = models.CharField(max_length=50, blank=False, null=False)
    agency_id = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)
