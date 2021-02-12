from django.db import models
from django.utils import timezone
from users.models import CustomUser

#model for request
class StudentRequest(models.Model):

    TYPE_CHOICES = [
        ('SD', 'Submission Deadline'),
        ('T2', 'TYPE2'),
        ('T3', 'TYPE3'),
        ('OT', 'Other')
    ]

    ACCEPT_STATUS = [
        ('PN', 'Pending'),
        ('AC', 'Accepted'),
        ('RJ', 'Rejected')
    ]
    requestType = models.CharField(max_length=2, choices=TYPE_CHOICES)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(CustomUser, related_name="student_requests", on_delete=models.CASCADE)
    reciever = models.ForeignKey(CustomUser, related_name="lecturer_requests", on_delete=models.CASCADE)
    accept_status = models.CharField(max_length=2, choices=ACCEPT_STATUS, default='PN')

    def __str__(self):
        return self.title

