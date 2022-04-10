from itertools import product
from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.response import Response

from products_app.models import Category, SubCategory, Product
from products_app.serializers import CategorySerializer, SubCategorySerializer, ProductSerializer


def get_all_subCategories(category):
    queryset = SubCategory.objects.filter(category=category).all()
    all_products =[]
    all_subCategories = queryset
    for subCategory in all_subCategories:
        print("Sub= ", subCategory)
        queryset = Product.objects.all()
        queryset = queryset.filter(subcategory=subCategory)
        all_products.append(queryset)
    return all_products

# Create your views here.
class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.order_by('category_name')
    serializer_class = CategorySerializer

class SubCategoryListAPIView(ListAPIView):
    queryset = SubCategory.objects.order_by('subcategory_name')
    serializer_class = SubCategorySerializer

class SubCategoriesOfCategoryListAPIView(ListAPIView):
    serializer_class = SubCategorySerializer

    def get_queryset(self):
        if self.request.method == 'GET':
            queryset = SubCategory.objects.all()
            state_name = self.request.GET.get('category', None)
            if state_name is not None:
                queryset = queryset.filter(category=state_name)
            return queryset

class ProductsOfSubCategoryListAPIView(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        if self.request.method == 'GET':
            queryset = Product.objects.all()
            state_name = self.request.GET.get('category', None)
            if state_name is not None:
                all_subCategories = get_all_subCategories(state_name)
                print("Q= ", all_subCategories[0])
                return all_subCategories[0]
            queryset = Product.objects.all()
            state_name = self.request.GET.get('subcategory', None)
            if state_name is not None:
                queryset = queryset.filter(subcategory=state_name)
                print("Q2=",queryset)
                return queryset

class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.order_by('id')
    serializer_class = ProductSerializer

    def post(self, request, *args, **kwargs):
        sub_category = request.data.get("sub-category")

        sub_category_obj = SubCategory.objects.filter(subcategory_name=sub_category).first()
        if sub_category_obj:
            sub_category_obj.save()
            Product.objects.create(product_name=request.data.get("product-name"), subcategory=sub_category_obj)
            return Response(self.serializer_class(self.get_queryset(), many=True).data)
        else:
            return Response({"status": False, "message": "Sub category is mandatory!"}, status=400)