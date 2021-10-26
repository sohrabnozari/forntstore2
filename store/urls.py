from django.urls import path
from django.urls.conf import incluce
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

# URLConf
router = DefaultRouter()
router.register('products', views.ProductViewSet)
router.register('collection', views.CollectionViewSet)

urlpatterns = router.urls
#  [
#     path('products/', views.ProductList.as_view()),
#     path('products/<int:pk>', views.ProductDetail.as_view()),
#     path('collection/', views.CollectionList.as_view()),
#     path('collection/<int:pk>', views.CollectionDetail.as_view())
# ]
