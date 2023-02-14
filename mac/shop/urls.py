from django.contrib import admin
from django.urls import path
from shop.views import*

urlpatterns = [
    path("", index, name="index"),
    path("about/", about, name="Aboutus"),
    path("contact/", contact, name="ContactUs"),
    path("tracker/", tracker, name="TrackingStatus"),
    path("search/", search, name="Search"),
    path("checkout/", checkout, name="Checkout"),
    path("products/<int:id>", productView, name="ProductView"),

]