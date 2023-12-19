from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.template.loader import render_to_string
from .tasks import notify_about_new_post

from news.models import PostCategory

from skillaNEWS import settings


@receiver(m2m_changed, sender=PostCategory.post)
def notify_about_new_post(sender, instance, action,  **kwargs):
    if action == "post_add":
        notify_about_new_post.delay(instance.id)

# def send_notifications (preview, pk,  header_post, subscribers):
#     html_context = render_to_string(
#         'post_created_email.html',
#         {
#             'text': preview,
#             'link': f'{settings.SITE_URL}/news/{pk}'
#
#         }
#     )
#
#     msg = EmailMultiAlternatives(
#         subject= header_post,
#         body='',
#         from_email= settings.DEFAULT_FROM_EMAIL,
#         to=subscribers
#
#     )
#
#     msg.attach(html_context, 'text/html')
#     msg.send()
#
# @receiver(m2m_changed, sender= PostCategory)
# def notify_about_new_post( sender, instance, **kwargs):
#     if kwargs ['action'] == 'post_add':
#         categories = instance.category.all()
#         subscribers:list[str] = []
#         for category in categories:
#             subscribers += category.subscribers.all()
#
#         subscribers = [s.email for s in subscribers]
#
#         send_notifications(instance.preview(),instance.pk,instance.header_post, subscribers)





