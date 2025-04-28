from django import template

register = template.Library()


@register.inclusion_tag('menu/list_menu.html')
def draw_menu(menu):
    menu_items = menu.items.all()
    return {
        "menu": menu,
        'menu_items': menu_items
    }