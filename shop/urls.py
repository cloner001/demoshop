from .import views
from django.urls import path,include

urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("search", views.search, name="search"),
    path("tracker", views.tracker, name="tracker"),
    path("productView/<int:myid>", views.productView, name="productView"),
    path("checkout", views.checkout, name="checkout"),
    path("thank", views.thank, name="thank"),

]