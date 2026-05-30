from django.contrib import admin
from django.urls import path
from choyxona.views import home_page, shashlik_view, salat_view, yaxna_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home_url'),
    path('shashlik/', shashlik_view, name='shashlik_url'),
    path('salat/', salat_view, name='salat_url'),
    path('yaxna/', yaxna_view, name='yaxna_url'),
]