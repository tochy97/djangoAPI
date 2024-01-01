from django.contrib import admin
from .models import Hash, Key
from django.apps import apps
# Register your models here.

admin.site.register(Hash)
admin.site.register(Key)

app = apps.get_app_config('graphql_auth')

for mode_name, model in app.models.items():
    admin.site.register(model)