from django.contrib import admin
from django.urls import path,include
from .views import Todolist,Tododetail,TodoCreate,TodoDelete,TodoUpdate

urlpatterns = [
    path('list/',Todolist.as_view(),name= 'list'),
    path('detail/<int:pk>',Tododetail.as_view(),name= 'detail'),
    path('create/',TodoCreate.as_view(), name= 'create'),
    #modelの複数のデータから一つを特定するときにpkを使う
    path('delete/<int:pk>',TodoDelete.as_view(),name= 'delete'),
    path('update/<int:pk>',TodoUpdate.as_view(),name= 'update')
   
    ]
