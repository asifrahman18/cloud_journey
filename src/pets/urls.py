
from django.urls import path
from pets.views import PetsListView, PetCreateView

urlpatterns = [
    path("all/", PetsListView.as_view(), name="pet-list"),
    path("add/", PetCreateView.as_view(), name="add-pet"),
    
]