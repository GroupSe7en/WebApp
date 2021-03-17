from django.db.models.signals import post_save
from.models import StudentRequest
from django.dispatch import receiver
from notifications.signals import notify

@receiver(post_save, sender=StudentRequest)
def newRequest(sender, instance, created, **kwargs):
    if created:
        notify.send(instance.author, recipient=instance.reciever, verb='posted new request - ', action_object=instance, level="info")