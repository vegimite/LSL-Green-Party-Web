from django.db import models
from greenparty.home.models import Link

# Create your models here.

class Event(models.Model):
    title_english = models.CharField(max_length=100)
    title_french = models.CharField(max_length=100)
    date = models.DateTimeField()
    text_english = models.TextField()
    text_french = models.TextField()
    links = models.ManyToManyField(Link, blank=True, null=True)
    lang = ""


    def getTitle(self):
        if self.lang == "en":
            return self.title_english
        if self.lang == "fr":
            return self.title_french

    def getText(self):
        if self.lang == "en":
            return self.text_english
        if self.lang == "fr":
            return self.text_french


    def __unicode__(self):
        return self.title_english

class Bio(models.Model):
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=50)
    english = models.TextField()
    french = models.TextField()
    title_english = models.CharField(max_length=100, blank=True, null=True)
    title_french = models.CharField(max_length=100, blank=True, null=True)
 #   links = models.ManyToManyField(Link, blank=True, null=True)
    lang = ""

    def getTitle(self):
        if self.lang == "en":
            return self.title_english
        if self.lang == "fr":
            return self.title_french

    def getBio(self):
        if self.lang == "en":
            return self.english
        if self.lang == "fr":
            return self.french

    def __unicode__(self):
        return self.name