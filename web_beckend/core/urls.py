
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('api.urls')),
    path('tg_api/',include('tg_api.urls')),
    path('web_api/',include('web_api.urls'))
]
