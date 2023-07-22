from django.urls import path
from . import views

urlpatterns = [
    path('', views.bloglist, name='bloglist'),
    path('<int:pk>/', views.blogdetail, name='blogdetail'),
    path('write/', views.write, name='write'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('<int:pk>/new_comment', views.new_comment, name='new_comment'),
    path('update_comment/<int:pk>', views.update_comment, name='update_comment'),
    path('delete_comment/<int:pk>/', views.delete_comment, name='delete_comment'),
    path('category/<str:slug>/', views.category_page, name='category_page'),
    path('tag/<str:slug>/', views.tag_page, name='tag_page'),
]