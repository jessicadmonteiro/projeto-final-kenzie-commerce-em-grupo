from rest_framework.urls import path
from . import views

urlpatterns = [
    path("order/", views.OrderView.as_view()),
    # path("order/product/<int:pk>/", views.OrderProductView.as_view())
]
