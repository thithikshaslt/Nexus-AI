from django.contrib import admin
from .models import ModelProvider, RoutingRule, FileRoutingRule

admin.site.register(ModelProvider)
admin.site.register(RoutingRule)
admin.site.register(FileRoutingRule)
