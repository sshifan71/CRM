from django.contrib import admin
from .models import User, Lead, Agent, UserProfile

#Inside the leads app, we have registered 3 attributes
admin.site.register(UserProfile)

admin.site.register(User)

admin.site.register(Lead)

admin.site.register(Agent)