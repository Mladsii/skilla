from django.urls import path
# Импортируем созданное нами представление
from .views import PostList, Postinfo, PostDetail, PostCreate, PostUpdate, PostDelete, subscriptions


urlpatterns = [

   path('', PostList.as_view(), name='post_list'),
   path('<int:id>', Postinfo.as_view(), name='post_info'),
   path('<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('create/', PostCreate.as_view(), name='post_create'),
   path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('subscriptions/', subscriptions, name='subscriptions'),

]