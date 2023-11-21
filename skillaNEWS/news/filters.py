from django.forms import DateTimeInput
from django_filters import FilterSet,DateTimeFilter
from .models import Post , Category

# Создаем свой набор фильтров для модели Product.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.



class PostFilter(FilterSet):

    data = DateTimeFilter(
        field_name='data',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )
    class Meta:
       # В Meta классе мы должны указать Django модель,
       # в которой будем фильтровать записи.
       model = Post

       # В fields мы описываем по каким полям модели
       # будет производиться фильтрация.
       fields = {
           # поиск по названию
           'header_post': ['icontains'],
           # количество товаров должно быть больше или равно
           'category': ['gt'],

       }