from django.contrib import admin
from locationfinder.models import reg, add, fed, fedre, locre

admin.site.register(reg)
admin.site.register(add)
admin.site.register(fed)
admin.site.register(fedre)
admin.site.register(locre)
admin.site.site_header="NearMe Admin"
# Register your models here.
