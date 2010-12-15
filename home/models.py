from django.db import models

# Create your models here.
class Welcome(models.Model):
    main_english = models.TextField()
    main_french = models.TextField()
    lang = ""

    def getMainText(self):
        if self.lang == "en":
            return self.main_english
        if self.lang == "fr":
            return self.main_french


# Create your models here.
class Candidate(models.Model):
    main_english = models.TextField()
    main_french = models.TextField()
    lang = ""

    def getMainText(self):
        if self.lang == "en":
            return self.main_english
        if self.lang == "fr":
            return self.main_french

# Create your models here.
class Aside(models.Model):
    title_english = models.CharField(max_length=100)
    title_french = models.CharField(max_length=100)
    main_english = models.TextField()
    main_french = models.TextField()
    lang = ""

    def getMainText(self):
        if self.lang == "en":
            return self.main_english
        if self.lang == "fr":
            return self.main_french

    def getTitle(self):
        if self.lang == "en":
            return self.title_english
        if self.lang == "fr":
            return self.title_french

    def __unicode__(self):
        return self.title_english