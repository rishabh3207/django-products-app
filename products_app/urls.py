from django.urls import path

from products_app.views import CategoryListAPIView, SubCategoryListAPIView, ProductListCreateAPIView, SubCategoriesOfCategoryListAPIView, ProductsOfSubCategoryListAPIView


urlpatterns = [

    path('category/', CategoryListAPIView.as_view(), name="category-list"),
    path('category/search/', SubCategoriesOfCategoryListAPIView.as_view(), name="category-search-list"),
    path('sub-category/', SubCategoryListAPIView.as_view(), name="sub-category-list"),
    path('product/', ProductListCreateAPIView.as_view(), name="product-list"),
    path('product/search/', ProductsOfSubCategoryListAPIView.as_view(), name="product-search-list"),
]