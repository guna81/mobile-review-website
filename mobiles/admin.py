from django.contrib import admin
from .models import *

admin.site.register(Brand)
admin.site.register(Model)
admin.site.register(Latest)
admin.site.register(Varient)
admin.site.register(Spec)
admin.site.register(PopularMobiles)
admin.site.register(RecentMobiles)
admin.site.register(PopularComparisions)
admin.site.register(RecentComparisions)
admin.site.register(Review)