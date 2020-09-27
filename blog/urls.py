from .import views
from django.urls import path,include

urlpatterns = [
    path("",views.blog,name="blog")
]