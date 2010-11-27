from greenparty.polls.models import Poll, Choice
from django.contrib import admin

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question']
    inlines = [ChoiceInline]

admin.site.register(Poll, PollAdmin)
