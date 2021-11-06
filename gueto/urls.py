

from django.contrib import admin
from django.urls import path,include

#from . import clinique
from .import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('clinique.urls')),
    path('Contact/',views.contact_view),
]
