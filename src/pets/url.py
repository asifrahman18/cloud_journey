from django.urls import path
from pets.views import PetsListView

urlpatterns = [
    path("all/", PetsListView.as_view(), name="pet-list"),
]