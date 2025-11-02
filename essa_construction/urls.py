# essa_construction/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # ajoute tes apps ici
    # path('', include('users.urls')),
]
