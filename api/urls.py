from django.urls import path
from . import views

urlpatterns = [
    # get all product just product dont detail
    path('get_all_product/',views.get_all_data.as_view(),name='get_all_data'),
    path('get_detail_product/<int:id>',views.get_detail_product.as_view(),name='get_detail_data'),
    path('add_to_card/',views.add_card_shop.as_view(),name='card_shop'),
    path('show_card_shop/',views.show_card_shop.as_view(),name='show_card_shop'),
    path('send_order/',views.send_order.as_view(),name='send_order'),
    path('category/',views.get_category.as_view(),name='category'),
    path('search/',views.search.as_view(),name='search_page')
]
