from django.db import models
from django.template.defaultfilters import slugify
from django.utils.html import strip_tags
from greenparty.home.models import GreenModel
# Create your models here.

class Event(GreenModel):
    title_english = models.CharField(max_length=100)
    title_french = models.CharField(max_length=100)
    slug_english = models.SlugField(editable=False)
    slug_french = models.SlugField(editable=False)


    draft = models.BooleanField()
    date = models.DateTimeField()


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

    def getSlug(self):
        if self.lang == "en":
            return self.slug_english
        if self.lang == "fr":
            return self.slug_french

    def get_absolute_url(self):
        return "/%s/%s/" %(self.date.strftime("%Y/%b/%d").lower(), self.getSlug())

    def __unicode__(self):
        return self.title_english

    class Meta:
        ordering = ('-date',)
        get_latest_by = 'date'



