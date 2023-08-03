from django.contrib import admin
from .models import Asset
from django.utils.html import format_html
# Register your models here.



class AssetAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src= "{}" width = "40px" / >'.format(object.asset_photo.url))

    thumbnail.short_description = 'Photo'

    list_display = ('id','thumbnail','asset_title','asset_id','state','city','price','area','condition','year','is_featured',)
    list_display_links = ('thumbnail','asset_id','asset_title')
    search_fields = ('condition','city','year','asset_title')
    list_editable = ('is_featured',)
    list_filter = ('state','price','city')


admin.site.register(Asset, AssetAdmin)
