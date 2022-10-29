from django.contrib import admin
from django.urls import path, include
from histtory import urls
from .views import calculate, history_objects

urlpatterns = [
    path('admin/', admin.site.urls),
    path('calc',calculate, name = 'calc'),
    path('vivod', history_objects, name='vivod'),
]