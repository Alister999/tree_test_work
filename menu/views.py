from http.client import responses, HTTPResponse

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView


class MainView(TemplateView):
    template_name = 'menu/index.html'
    extra_context = {'menu_selected': 0}

class MenuView(TemplateView):
    template_name = 'menu/index.html'
    menu_url_kwarg = 'menu_slug'
    # extra_context = {'menu_selected': menu_id}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_selected'] = self.kwargs['menu_slug']
        return context


# def main_view(request):
#     return render(request, 'menu/index.html', context={'menu_selected': 0})
#
# def menu(request, menu_id):
#     return render(request, 'menu/index.html', context={'menu_selected': menu_id})
#

    # def get(request):
    # return main_view(request)#render(request, 'menu/index.html')
        #HttpResponse(f'{menu_id} menu')

# class MenuView(DetailView):
#     template_name =
