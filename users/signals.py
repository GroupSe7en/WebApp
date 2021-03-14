from django.db.models.signals import m2m_changed
from.models import CustomUser, StudentProfile, LecturerProfile
from django.dispatch import receiver

# @receiver(post_save, sender=CustomUser)
@receiver(signal=m2m_changed, sender=CustomUser.groups.through)
def create_profile(instance, action, reverse, model, pk_set, using, *args, **kwargs):
    if action == 'post_add':
        if instance.groups.filter(name='Lecturer').exists():
            LecturerProfile.objects.create(user=instance)
        elif instance.groups.filter(name='Student').exists():
            StudentProfile.objects.create(user=instance)

@receiver(signal=m2m_changed, sender=CustomUser.groups.through)
def save_profile(instance, action, reverse, model, pk_set, using, *args, **kwargs):
    if instance.groups.filter(name='Student').exists():
        instance.studentprofile.save()
    elif instance.groups.filter(name='Lecturer').exists():
        instance.lecturerprofile.save()