from rest_framework.urls import path
from . import views

urlpatterns = [
    path("products/", views.ProductView.as_view()),
    path("products/<int:pk>/", views.UpdateProduct.as_view()),
]
