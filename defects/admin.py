from django.contrib import admin
from defects.models import defectsData,Developers,Testers,defect_screenshot

# Register your models here.
admin.site.register(defectsData)
admin.site.register(Developers)
admin.site.register(Testers)
admin.site.register(defect_screenshot)

