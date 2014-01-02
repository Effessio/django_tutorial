from django.contrib import admin
from polls.models import Poll,Choice
from django.utils import timezone
import datetime


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_display = ['question', 'pub_date', 'was_published_recently']
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question']



admin.site.register(Poll, PollAdmin)
