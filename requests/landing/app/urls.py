from django.urls import path

from app.views import landing, stats, index


urlpatterns = [
    path('', index, name='index'),
    path('landing/<name1>/', landing, name='landing'),
    path('stats/', stats, name='stats'),
]
