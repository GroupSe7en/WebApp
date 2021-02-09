# from django.db import models
# from django.utils import timezone
# from django.contrib.auth.models import User

# #model for request
# class StudentRequest(models.Model):

#     title = models.CharField(max_length=100)
#     content = models.TextField()
#     date_posted = models.DateTimeField(default=timezone.now)
#     author = models.ForeignKey(User, related_name="student_requests", on_delete=models.CASCADE)
#     reciever = models.ForeignKey(User, related_name="lecturer_requests", on_delete=models.CASCADE)
#     accept_status = models.BooleanField(default=False)

#     def __str__(self):
#         return self.title
