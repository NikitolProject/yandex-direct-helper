from django.contrib import admin

from .models import LoginsModel, CidModel, UrlsModel

admin.site.register(LoginsModel)
admin.site.register(CidModel)
admin.site.register(UrlsModel)
