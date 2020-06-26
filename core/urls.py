from django.urls import path
from products import views as product_views

app_name = "core"

urlpatterns = [path("", product_views.all_products, name="home")]
