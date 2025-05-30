from django.contrib import admin
from django.urls import path, include

import menu

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('menu.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
]
