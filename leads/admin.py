from django.contrib import admin
from .models import User, Lead, Agent, UserProfile
from django.contrib.auth.admin import UserAdmin

admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Lead)
admin.site.register(Agent)
