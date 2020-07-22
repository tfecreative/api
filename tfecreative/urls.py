from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path(route='api/', view=include('tfecreative.api.urls', namespace='api'), name='api'),
]
