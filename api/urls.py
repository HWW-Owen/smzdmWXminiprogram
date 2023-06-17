from api import views
from django.urls import path


#127.0.0.1:8000/api/
urlpatterns = [
    path('product/',views.ProductListView.as_view(), name='product'),
    path('create/',views.ProductCreateView.as_view(),name='create'),
    path('update/',views.ProductUpdateView.as_view(),name='update'),
    path('delete/',views.ProductDeleteView.as_view(),name='delete'),
    path('tips/', views.TipView.as_view(), name='tips'),
    path('banner/',views.ProductCarouselView.as_view(),name='banner'),
    path('products/', views.ProductList.as_view(), name='product_list'),
    path('user-products/', views.UserProductList.as_view(), name='user_product_list'),
    path('user-products/<int:pk>/', views.UserProductDetail.as_view(), name='user_product_detail'),
    path('getproduct/',views.getproduct,name='get_product'),
    path('getTip/',views.getTip,name="get_Tip"),
    path('getcomment/',views.getcomment,name='get_comment'),
    path('getsubscribe',views.getsubsribe,name='get_subscribe'),
    path('product_price_history',views.product_price_history,name='product_price_history')
  
]

