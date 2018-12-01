from django.urls import path
from . import views


urlpatterns = [
    path("", views.products, name="products"),
    path("<str:catalog>/", views.test, name="test")
]