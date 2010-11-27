from django.db import models

# Create your models here.
class Volunteer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    extra = models.TextField()


    def __unicode__(self):
        return self.last_name + ', ' + self.first_name

class VolunteerBlurb(models.Model):

    text_english = models.TextField()
    text_french = models.TextField()
    lang = ""


    def getText(self):
        if self.lang == "en":
            return self.text_english
        if self.lang == "fr":
            return self.text_french