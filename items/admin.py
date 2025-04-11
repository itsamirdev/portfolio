from django.contrib import admin

from items.models import Contact, Project, About, ItemBox

admin.site.register(Project)
admin.site.register(About)
admin.site.register(ItemBox)
admin.site.register(Contact)

