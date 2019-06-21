from django.contrib import admin
from first_app.models import Topic, Webpage, AccessRecord, userDetails

admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)
admin.site.register(userDetails)