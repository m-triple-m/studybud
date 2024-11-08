from django.urls import path
from . import views

urlpatterns = [
    path('browse/', views.browse),
    path('add-product', views.addProduct, name='add-product'),
    path('details/<str:id>/', views.details, name='details'),
    path('submit-review', views.submitReview, name='details'),
]