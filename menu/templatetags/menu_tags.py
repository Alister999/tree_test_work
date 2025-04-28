from django import template

from menu.models import Menu, MenuItem

register = template.Library()

@register.inclusion_tag('menu/list_menu.html')
def draw_menu(menu_slug): #menu_selected=None):
    menu = Menu.objects.get(slug=menu_slug)
    # menus = Menu.objects.all()
    menu_items = MenuItem.objects.filter(menu__slug=menu_slug)
    return {
        "menu": menu,
        #'menu_selected': menu_selected,
        'menu_items': menu_items
    }