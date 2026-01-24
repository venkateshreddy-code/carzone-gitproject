from django.urls import path
from django.http import HttpResponse
from . import views

urlpatterns = [
    path("test/", lambda r: HttpResponse("PAGES URLS WORK ✅")),
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("services/", views.services, name="services"),
    path("contact/", views.contact, name="contact"),
    path("cars/", views.cars, name="cars"),

]
