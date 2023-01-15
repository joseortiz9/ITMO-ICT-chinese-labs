from django.contrib import admin

# Register your models here.
from .models import Conference, Presentation, Review

admin.site.register(Conference)
admin.site.register(Presentation)
admin.site.register(Review)
