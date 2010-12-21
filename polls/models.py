from __future__ import division
from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.
class Poll(models.Model):
    question_english = models.CharField(max_length=200)
    question_french = models.CharField(max_length=200)
    slug_english = models.SlugField(editable=False)
    slug_french = models.SlugField(editable=False)
    pub_date = models.DateTimeField('date published')
    draft = models.BooleanField()
    active = models.BooleanField()
    lang = ''


    def getQuestionText(self):
        if self.lang == "en":
            return self.question_english
        if self.lang == "fr":
            return self.question_french

    def getSlug(self):
        if self.lang == "en":
            return self.slug_english
        if self.lang == "fr":
            return self.slug_french

    def get_absolute_url(self):
        return "/%s/" % (self.getSlug())

    def totalVotes(self):
        votes = 0
        for c in self.choice_set.all():
            votes = votes + c.votes

        return votes

    def __unicode__(self):
        return self.question_english


    def save(self, *args, **kwargs):
        if not self.id:
            self.slug_english = slugify(self.question_english)
            self.slug_french = slugify(self.question_french)

        super(Poll, self).save(*args, **kwargs)

    class Meta:
        ordering = ('-pub_date',)
        get_latest_by = 'pub_date'

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_english = models.CharField(max_length=200)
    choice_french = models.CharField(max_length=200)
    votes = models.IntegerField()

    def getChoiceText(self):
        if self.poll.lang == "en":
            return self.choice_english
        if self.poll.lang == "fr":
            return self.choice_french

    def percent(self):
        return self.votes / self.poll.totalVotes * 100

    def __unicode__(self):
        return self.choice_english