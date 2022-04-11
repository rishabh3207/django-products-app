
Deployed in https://rk-django-products.herokuapp.com/

Below are Backend APIs:
1 - API to get all categories.
 Example: https://rk-django-products.herokuapp.com/api/v1/category/
2 - API to get subcategories for a category.
Example: https://rk-django-products.herokuapp.com/api/v1/category/search/?category=Electronics
3 - API to get all products for a category.
Example: https://rk-django-products.herokuapp.com/api/v1/product/search/?category=Sports
4 - API to get all products for a subcategory.
Example: https://rk-django-products.herokuapp.com/api/v1/product/search/?subcategory=Laptops
5 - API to post new product under existing subcategory and category.
Example: 
POST https://rk-django-products.herokuapp.com/api/v1/product/
{
    "product-name": "Window 2019",
    "sub-category": "Laptops"
}
