from django.db import models

# Create your models here.

class Event(models.Model):
    title_english = models.CharField(max_length=100)
    title_french = models.CharField(max_length=100)
    date = models.DateTimeField()
    text_english = models.TextField()
    text_french = models.TextField()
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
