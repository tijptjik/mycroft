from django.contrib import admin

from models import *

for model in [UnawareOrder, Item]:
    admin.site.register(model)
