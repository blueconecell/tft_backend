from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/champions/', include("champions.urls")),
    path('api/v1/synergies/', include("synergies.urls")),
    path('api/v1/items/', include("items.urls")),
    path('api/v1/augments/', include("augments.urls")),
]