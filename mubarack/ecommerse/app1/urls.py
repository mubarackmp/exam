from django.contrib import admin
from django.urls import path,include
from app1 import views


app_name ='app1'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='home'),
    path('logine/',views.userlogin,name='logine'),
    path('signupe/',views.usersignup,name='signupe'),
    path('logoute/',views.userlogout,name='logoute'),
    path('shop/<int:p_id>',views.shop,name='shop'),
    path('add/',views.add,name='add'),
    path('addtocart/<int:prod_id>',views.addtocart,name='addtocart'),
    path('removefromcart/<int:item_id>',views.removecart,name='remove'),
    path('cart/',views.showcart,name='cart'),
    path('delete/<int:dele>',views.deletey,name='delete'),
]
