from django.contrib import admin
from .models import Card, List

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ['title','description','story_points','business_value']
    list_editable = ['story_points']

#admin.site.register(Card)
admin.site.register(List)


