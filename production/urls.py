from django.urls import path
from production.views import product_view,create_product_view,delete_product_view,all_product_view


app_name= "production"
urlpatterns = [
    path("<int:id>/", product_view, name="product"),
    path("<int:id>/delete", delete_product_view, name="delete product"),
    path("create", create_product_view , name="create"),
    path("all", all_product_view , name="view all"),
]