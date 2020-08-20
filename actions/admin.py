from django.contrib import admin
from .models import Action

@admin.register(Action)
class actionAdmin(admin.ModelAdmin):
    '''Admin View for action'''

    list_display = ('user','verb','target', 'created')
    list_filter = ('created',)
    search_fields = ('verb',)
  
