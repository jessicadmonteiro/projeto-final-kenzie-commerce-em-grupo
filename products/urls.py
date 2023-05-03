from rest_framework.urls import path
from . import views

urlpatterns = [
    path("products/", views.ProductView.as_view()),
    # path("products/<type>/", views.ProductDetailView.as_view()),
]
