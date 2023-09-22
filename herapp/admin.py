from django.contrib import admin

from herapp.models import Office

# Register your models here.
class OfficeAdmin(admin.ModelAdmin):
    list_display=('id','name','department')
    search_fields=('name',)



admin.site.register(Office,OfficeAdmin)