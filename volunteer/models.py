from django.db import models
from django.forms import ModelForm
from home.models import GreenModel

# Create your models here.
class Volunteer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    extra = models.TextField()


    def __unicode__(self):
        return self.last_name + ', ' + self.first_name

class Blurb(GreenModel):
    blurb = ''

class VolunteerForm(ModelForm):
    class Meta:
        model = Volunteer
