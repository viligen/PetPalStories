from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from PetPalStories.common.models import SignedPetition


@receiver(signal=post_save, sender=SignedPetition)
def send_email_on_goal_reach(instance, created, **kwargs):
    if not created:
        return

    petition = instance.petition
    all_signatures_for_petition = SignedPetition.objects.filter(petition=petition).count()
    user_email = petition.owner.email
    if all_signatures_for_petition == petition.goal:
        send_mail(
            subject='Your petition reached its goal!',
            message=f'Congratulations, your petition with title "{petition.title}" just reached its goal regarding unique signatures! You can increase the goal or contact the addressed authorities and stop the petition.',
            from_email=None,
            recipient_list=(user_email, ),
    )