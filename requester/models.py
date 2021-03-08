from django.db import models
from django.utils import timezone
from users.models import CustomUser
from django.urls import reverse

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

    def get_absolute_url(self):
        return reverse('request-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    studentrequest = models.ForeignKey(StudentRequest, related_name="comments", on_delete=models.CASCADE)
    author =  models.ForeignKey(CustomUser, related_name="comment_author", on_delete=models.CASCADE)
    body = models.TextField()
    date_commented = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '%s - %s' %(self.studentrequest.title, self.author)

    def get_absolute_url(self):
        return reverse('request-detail', kwargs={'pk': self.studentrequest.pk})

class CommentReply(models.Model):
    comment = models.ForeignKey(Comment, related_name="replies", on_delete=models.CASCADE)
    author =  models.ForeignKey(CustomUser, related_name="reply_author", on_delete=models.CASCADE)
    body = models.TextField()
    date_replied = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '%s - Reply to %s' %(self.comment.studentrequest.title, self.comment.author)

    def get_absolute_url(self):
        return reverse('request-detail', kwargs={'pk': self.comment.studentrequest.pk})