from . import views
from django.urls.conf import path

urlpatterns = [


      path('register',views.register,name='register'),
      path('login',views.login,name='login'),
      path('logout',views.logout,name='logout')

]