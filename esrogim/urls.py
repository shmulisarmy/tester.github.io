from django.urls import path
from . import views, api

urlpatterns = [
    path('', views.index, name='index'),
    path('image/<str:image_name>', views.serve_image, name='index'),
    path('data/', api.json_data, name='json_data'),
    
]