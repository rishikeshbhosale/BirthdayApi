from django.contrib import admin
from .models import login, birthday, designation, worklocation
# Register your models here.
admin.site.register(login)
admin.site.register(designation)
admin.site.register(worklocation)
admin.site.register(birthday)
