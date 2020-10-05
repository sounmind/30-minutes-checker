from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('setting/', views.setting, name="setting"),
    path('search/', views.search, name="search"),
    path('user/', views.user, name="user"),
    path('action/create/', views.create, name="action-create"),
    path('action/edit/<int:id>', views.edit, name="action-edit"),
    path('action/delete/<int:id>', views.delete, name="action-delete")
]
