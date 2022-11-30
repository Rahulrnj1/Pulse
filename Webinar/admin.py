from django.contrib import admin
from psutil import users
from .models import *

# Register your models here.
admin.site.register(Cities)
admin.site.register(State)
admin.site.register(User)
admin.site.register(HCPConnect)
admin.site.register(WebinarList)
admin.site.register(Livewebinar)
admin.site.register(ClinicalTool)
admin.site.register(Clinic)