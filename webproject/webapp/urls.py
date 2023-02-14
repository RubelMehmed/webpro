from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('remove/<int:id>/', views.remove, name='removing'),
    path('addnew/', views.addnew, name='addnow'),
    path('update/', views.update, name='saving'),
    path('edit/<int:id>/', views.edit, name='editing'),
    path('updatex/<int:id>/', views.update, name="updating")
]
