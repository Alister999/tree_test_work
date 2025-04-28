from http.client import responses, HTTPResponse

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView

from menu.models import Menu


class MainView(TemplateView):
    template_name = 'menu/index.html'
    extra_context = {'menu_selected': 0}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        menus = Menu.objects.prefetch_related('items__children').filter(
            slug__in=['general-page', 'our-services', 'about-us', 'contacts-us']
        )
        context['menus'] = menus
        return context

class MenuView(TemplateView):
    template_name = 'menu/index.html'
    menu_url_kwarg = 'menu_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_selected'] = self.kwargs['menu_slug']
        return context

def phone(request):
    return HttpResponse('phone')
