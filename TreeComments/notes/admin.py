from django.contrib import admin

from .models import Articles, Comments

from mptt.admin import MPTTModelAdmin

admin.site.register(Articles)

admin.site.register(Comments, MPTTModelAdmin)

# Register your models here.
