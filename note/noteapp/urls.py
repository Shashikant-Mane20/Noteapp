from django.urls import path
from noteapp import views

urlpatterns = [
    path('dashboard',views.dashboard_page),
    path('home',views.home_page),
    path('add_notes',views.add_notes),
    path('delete/<rid>',views.delete_notes),
    path('edit/<rid>',views.edit_notes),
    
]
