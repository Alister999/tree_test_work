from django.contrib import admin

from menu.models import Menu, MenuItem


# # Register your models here.
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    fields = ['name',]
    list_display = ('name', )
    list_per_page = 10
    save_on_top = True


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    fields = ['menu', 'parent', 'title', 'url', 'named_url']
    list_display = ('menu', 'parent', 'title', 'url', 'named_url')
    list_per_page = 10
    save_on_top = True

