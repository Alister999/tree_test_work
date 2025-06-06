from django.contrib import admin

from menu.models import Menu, MenuItem


# # Register your models here.
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    fields = ['name', 'slug']
    list_display = ('name', 'slug')
    list_per_page = 10
    save_on_top = True


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    fields = ['menu', 'parent', 'title', 'urls']
    list_display = ('menu', 'parent', 'title', 'urls')
    list_per_page = 10
    save_on_top = True

