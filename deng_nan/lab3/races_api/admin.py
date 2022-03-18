from django.contrib import admin

# Register your models here.
from races_api.models import Team, Race, Rider, Comment

admin.site.register(Team)
admin.site.register(Race)
admin.site.register(Rider)
admin.site.register(Comment)
