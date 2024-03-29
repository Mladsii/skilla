from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.urls import reverse
from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.cache import cache

# Create your models here.

class Autor(models.Model):  # наследуемся от класса Model
    autorUser = models.OneToOneField(User, on_delete=models.CASCADE)
    reit_pos_Autor = models.FloatField(default=0)

    def update_rating(self):
        sum_rait_post = self.post_set.aggregate(postRating= Sum('rating'))
        pRat =0
        pRat += sum_rait_post.get('potrRating')

        sum_rait_com_aut = self.autorUser.comment_set.aggregate(comRating = Sum('rating'))
        cRat = 0
        cRat += sum_rait_com_aut.get('comRating')


        self.reit_pos_Autor = pRat * 3 + cRat
        self.save()

    def __str__(self):
        return f"{self.autorUser}"



class Category(models.Model):
    sport = 'sp'
    politic = 'pl'
    obrazovanie = 'ob'
    comedy = 'cm'

    CATEGORY = (
        (sport, 'Спорт'),
        (politic, 'Политика'),
        (obrazovanie, 'Образование'),
        (comedy, 'Комедия')
    )
    name_cat = models.CharField(max_length= 2, unique=True,
                           choices=CATEGORY)

    subscribers = models.ManyToManyField(User, related_name='categories')

    def __str__(self):
        return f"{self.name_cat}"

class Subscriber(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='subscriptions',
    )
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='subscriptions',
    )



class Post(models.Model):
    autor = models.ForeignKey(Autor, on_delete= models.CASCADE)

    def __str__(self):
        return f'{self.category}'

    article = 'ar'
    news = 'nw'
    POST = (
        (article, 'Статья'),
        (news, 'Новость')
    )


    data = models.DateTimeField(auto_now_add = True)
    st_or_nw = models.CharField(max_length=2, choices=POST,default=article)
    header_post=models.CharField(max_length=255)
    test_post = models.TextField()
    rating = models.FloatField()
    category =models.ManyToManyField(Category, through = 'PostCategory')

    def like(self):
        self.rating +=1
        self.save()

    def dislike(self):
        self.rating -=1
        self.save()


    def preview(self):
        return self.test_post[0:123] + '....'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # сначала вызываем метод родителя, чтобы объект сохранился
        cache.delete(f'product-{self.pk}')  # затем удаляем его из кэша, чтобы сбросить его


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text_comment = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    rating =models.FloatField(default=0.0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()



