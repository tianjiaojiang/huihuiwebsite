from django.urls import path
from . import views


urlpatterns = [
    path("<str:catalog>", views.products, name="products"),
    path("test/", views.test, name="test")
]