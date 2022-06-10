from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(path('__debug__/', include(debug_toolbar.urls)))
