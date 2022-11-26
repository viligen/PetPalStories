from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

UserModel = get_user_model()


@receiver(signal=post_save, sender=UserModel)
def send_email_on_signup(instance, created, **kwargs):
    if not created:
        return
    user_email = instance.email
    send_mail(
        subject='Welcome to PetPalStories!',
        message='Hi, you have successfully created your profile at PetPalStories. Enjoy!',
        from_email=None,
        recipient_list=(user_email, ),
    )