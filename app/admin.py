from django.contrib import admin
from .models import Story, Storybone
# Register your models here.

class StoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')

class StoryboneAdmin(admin.ModelAdmin):
    list_display = ('id', 'starttext', 'lasttext')
    list_display_links = ('id', 'starttext', 'lasttext')

admin.site.register(Story, StoryAdmin)
admin.site.register(Storybone, StoryboneAdmin)