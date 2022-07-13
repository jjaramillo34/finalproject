from django.contrib import admin
from parler.admin import TranslatableAdmin
from about.models import About, Members

# Register your models here.
admin.site.register(About, TranslatableAdmin)
admin.site.register(Members, TranslatableAdmin)

