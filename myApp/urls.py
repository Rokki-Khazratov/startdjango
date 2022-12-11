from django.urls import path
from . import views

app_name = ''

urlpatterns = [
    path('<slug:slug>', Product, name = Product),
]

urlpatterns = [
    # path('',views.index, name='index'),
]