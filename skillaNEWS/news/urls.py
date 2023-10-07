from django.urls import path
# Импортируем созданное нами представление
from .views import PostList, Postinfo


urlpatterns = [

   path('', PostList.as_view()),
   path('<int:id>', Postinfo.as_view(), name='post_info')

]