from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('mobile_list/<str:brand_name>', views.mobile_list, name='mobile_list'),
    path('mobile_details/<str:model_name>', views.mobile_details, name='mobile_details'),
    path('compare_mobile/<str:mobile1>/<str:mobile2>', views.compare_mobile, name='compare_mobile'),
    path('write_review/<str:mobile>', views.write_review, name='write_review'),
    path('login', views.login_view, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout_view, name='logout')
]