from django.contrib import admin
from django.urls import path
from mathapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('power/', views.power_calc, name='power_calc'),
    path('', views.power_calc, name="home")
]
