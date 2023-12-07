from django.contrib import admin

from issuesApp.models import Issue, Agent

# Register your models here.
admin.site.register(Issue)
admin.site.register(Agent)