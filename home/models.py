from django.db import models
import markdown

class GreenModel(models.Model):
    lang = ''
    main_english = models.TextField(blank=True, editable=False)
    main_french = models.TextField(blank=True, editable=False)
    markdown_english = models.TextField()
    markdown_french = models.TextField()

    def getMainText(self):
        if self.lang == "en":
            return self.main_english
        if self.lang == "fr":
            return self.main_french

    def save(self, *args, **kwargs):
        self.main_english = markdown.markdown(self.markdown_english)
        self.main_french = markdown.markdown(self.markdown_french)

        super(GreenModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True

# Create your models here.
class Welcome(GreenModel):
    welcome = ''

# Create your models here.
class Candidate(GreenModel):
    candidate = ''

# Create your models here.
class Aside(GreenModel):
    title_english = models.CharField(max_length=100)
    title_french = models.CharField(max_length=100)

    def getTitle(self):
        if self.lang == "en":
            return self.title_english
        if self.lang == "fr":
            return self.title_french

    def __unicode__(self):
        return self.title_english