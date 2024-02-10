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
    path('details/',views.show,name='details'),
    path('add/',views.add,name='add'),
]
