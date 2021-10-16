from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:employer_extra>/<int:file_extra>', views.index, name='index')
]
