from django.urls import path
from . import views

urlpatterns = [
    path('', views.Shows),
    path('shows/new', views.AddShow),
    path('shows/<int:idshow>', views.ShowShow),
    path('shows', views.Shows),
    path('shows/<int:idshow>/edit', views.ShowEdit),

    path('shows/create', views.CreateShow),
    path('shows/<int:idshow>/update', views.ShowUpdate),
    path('delete/<int:idshow>/destroy', views.deleteShow)
    
    
]