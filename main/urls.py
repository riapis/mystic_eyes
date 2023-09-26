from django.urls import path
from main.views import show_main, add_card, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user\
, logout_user, increase_card, decrease_card, delete_card
app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('add-card', add_card, name='add_card'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('product/<int:product_id>/increase/', increase_card, name='increase_card'),
    path('product/<int:product_id>/decrease/', decrease_card, name='decrease_card'),
     path('delete_card/<int:product_id>/', delete_card, name='delete_card'),
]