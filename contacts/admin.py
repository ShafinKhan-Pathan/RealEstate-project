from django.contrib import admin
from .models import Contact
# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','email','asset_title','city','state')
    list_display_links= ('id','first_name','last_name')
    search_fields = ('first_name','last_name','email','asset_title')
    list_per_pages = 25




admin.site.register(Contact, ContactAdmin)
