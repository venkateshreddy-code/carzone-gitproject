from django.urls import path
from . import views

urlpatterns = [
    path("", views.cars, name="cars"),
    path("search/", views.search, name="search"),                 # fallback
    path("search=<str:keyword>", views.search, name="search_eq"), # /cars/search=love
    path("<int:id>/", views.car_detail, name="car_detail"),
]
