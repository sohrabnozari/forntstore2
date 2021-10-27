from django.urls import path
from django.urls.conf import incluce
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers


router = routers.NestedDefaultRouter()
router.register('products', views.ProductViewSet)
router.register('collection', views.CollectionViewSet)

product_router = routers.NestedDefaultRouter(
    router, 'products', lookup='product')
product_router.register(review, )

urlpatterns = router.urls
