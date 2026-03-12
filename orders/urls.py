from django.urls import path
from . import views

urlpatterns = [

    path('', views.index),

    path('order/', views.order),

    path('payment/', views.payment),

    path('scanner/', views.scanner),

    path('success/', views.success),

    path('details/', views.details),

    path('admin-login/', views.admin_login),

    path('dashboard/', views.dashboard),

    path('delete/<int:id>/', views.delete_order),

]
