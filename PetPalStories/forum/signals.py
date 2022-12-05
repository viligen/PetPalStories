from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from PetPalStories.forum.models import Comment


@receiver(signal=post_save, sender=Comment)
def send_email_on_post_comment(instance, created, **kwargs):
    if not created:
        return
    user_email = instance.parent_post.owner.email
    send_mail(
        subject='A new comment to your post',
        message=f'Hello there {instance.parent_post.owner.username}, '
                f'you have just received a new comment to your post : "{instance.parent_post.topic}"',
        from_email=None,
        recipient_list=(user_email,),
    )