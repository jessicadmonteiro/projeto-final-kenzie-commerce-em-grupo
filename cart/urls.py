from rest_framework.urls import path
from . import views

urlpatterns = [
    path("cart/", views.CartView.as_view()),
    path("cart/product/<int:pk>/", views.CartAddProductView.as_view())
]
