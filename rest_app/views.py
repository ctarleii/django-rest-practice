from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.request import Request

from rest_app.models import Product, Category
from rest_app.permissions import AdminOrReadOnly
from rest_app.serializers import ProductSerializer, CategorySerializer


class ListCreateCategory(ListCreateAPIView):

    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [AdminOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def validate(self, data):
        if 'discount' in data:
            raise ValidationError('Contact phone field is required.')


class CreateListAPIView(ListCreateAPIView):

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [AdminOrReadOnly]

    def get(self, request: Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request: Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class RetrieveDestroyUpdateAPIView(RetrieveUpdateDestroyAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AdminOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


