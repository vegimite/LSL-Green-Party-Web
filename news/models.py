from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

class Event(models.Model):
    title_english = models.CharField(max_length=100)
    title_french = models.CharField(max_length=100)
    date = models.DateTimeField()
    text_english = models.TextField()
    text_french = models.TextField()
    slug_english = models.SlugField(editable=False)
    slug_french = models.SlugField(editable=False)
    draft = models.BooleanField()
    lang = ""


    def save(self, *args, **kwargs):
        if not self.id:
            self.slug_english = slugify(self.title_english)
            self.slug_french = slugify(self.title_french)

        super(Event, self).save(*args, **kwargs)

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

    def getSlug(self):
        if self.lang == "en":
            return self.slug_english
        if self.lang == "fr":
            return self.slug_french


    def __unicode__(self):
        return self.title_english

