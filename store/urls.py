from django.db.models import lookups
from django.urls import path
from django.urls.conf import include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers


router = routers.NestedDefaultRouter()
router.register('products', views.ProductViewSet)
router.register('collection', views.CollectionViewSet)

product_router = routers.NestedDefaultRouter(
    router, 'products', lookups='product')
product_router.register('reviews', views.ReviewViewSet,
                        basename='product-reviews')

urlpatterns = router.urls+product_router.urls
