# from django.db.models.signals import post_save
# from.models import StudentRequest
# from django.dispatch import receiver
# from notifications.signals import notify

# @receiver(signal=post_save, sender=StudentRequest)
# def notifyNewPost(instance, action, reverse, model, pk_set, using, *args, **kwargs):
#     notify.send(instance.author, recipient=instance.receiver, verb='replied to comment on', action_object=instance, level="info", timestamp=timezone.now())