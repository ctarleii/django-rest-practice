from django.urls import path

from rest_app.views import *


urlpatterns = [
    path('', CreateListAPIView.as_view(), name='product-list-create'),
    path('<int:pk>/', RetrieveDestroyUpdateAPIView.as_view(), name='product-detail'),
    path('category/', ListCreateCategory.as_view(), name='category-list-create'),

]