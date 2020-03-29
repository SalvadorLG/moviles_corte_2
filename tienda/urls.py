from django.urls import include, path
from rest_framework.routers import DefaultRouter
from tienda.viewsets import ProductosViewSet, DetallesViewSet
from tienda.views import UserProfileListCreateView, userProfileDetailView
from rest_framework import routers

router = routers.SimpleRouter()
router.register('productos',ProductosViewSet)
router.register('detalles',DetallesViewSet)

urlpatterns = [
    #gets all user profiles and create a new profile
    path("all-profiles/",UserProfileListCreateView.as_view(),name="all-profiles"),
   # retrieves profile details of the currently logged in user
    path("profile/<int:pk>",userProfileDetailView.as_view(),name="profile"),
]

urlpatterns += router.urls
