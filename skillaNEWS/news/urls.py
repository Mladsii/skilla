from django.urls import path
# Импортируем созданное нами представление
from .views import PostList, Postinfo, PostCreate, PostUpdate, PostDelete


urlpatterns = [

   path('', PostList.as_view()),
   path('<int:id>', Postinfo.as_view(), name='post_info'),
   path('create/', PostCreate.as_view(), name='post_create'),
   path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='product_delete'),

]