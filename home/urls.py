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
    path('action/detail/<int:id>/', views.action_detail, name="action-detail"),
    path('action/create/', views.action_create, name="action-create"),
    path('action/edit/<int:id>/', views.action_edit, name="action-edit"),
    path('action/delete/<int:id>/', views.action_delete, name="action-delete"),
    path('tag/view/', views.tag_view, name="tag-view"),
    path('tag/create/', views.tag_create, name="tag-create"),
    path('tag/edit/<int:id>/', views.tag_edit, name="tag-edit"),
    path('tag/delete/<int:id>/', views.tag_delete, name="tag-delete"),
]
