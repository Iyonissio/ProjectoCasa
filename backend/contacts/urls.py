from django.conf.urls import url
from django.urls import path
from .views import ContactCreateView

urlpatterns = [
    path('', ContactCreateView.as_view()),
]