from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('inner-page/', views.inner_page),
    path('portfolio-details/', views.portfolio_details),
    path('students/', views.students),
    path('teachers/', views.teachers),
    path('insert/', views.insert)

]