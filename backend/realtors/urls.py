from django.urls import path
from .views import RealtorListView, RealtorView, TopSellerView

urlpatterns = [
    path('', RealtorListView.as_view()),
    path('mais_vendido', TopSellerView.as_view()),
    path('<pk>', RealtorListView.as_view()),
]