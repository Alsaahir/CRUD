from django.urls import path
from . import views


urlpatterns = [
    path('api', views.CreateView.as_view(), name='create'),
    path('api/<str:id>', views.Crud.as_view(), name='crud'),
    path('', views.getRoutes, name='get_routes')
]
