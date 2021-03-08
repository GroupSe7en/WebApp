from django.contrib import admin
envfrom django.contrib import admin
from .models import StudentRequest, Comment, CommentReply

admin.site.register(StudentRequest)
admin.site.register(Comment)
admin.site.register(CommentReply)
