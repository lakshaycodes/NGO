from django.urls import path
from . import views

urlpatterns = [
    path('', views.bloghome, name="BlogHome"),
    path('<slug:slug>', views.viewblog, name="viewblog")
]
