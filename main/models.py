from django.db import models
from django.utils import timezone

class Message(models.Model):
    heading = models.CharField(max_length=256, blank=True, null=True)
    tags = models.CharField(max_length=256,blank=True, null=True)
    message = models.TextField(blank=True)
    files = models.ManyToManyField(to='Attatchments', related_name='message',blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    user = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self) -> str:
        return self.heading or self.message[:20] or self.tags[:20] or self.edited.__str__()

def nameTime(instance, filename):
    parts = filename.split('.')
    unq = timezone.now().strftime("%y_%m_%d_%H_%M_%S")
    return f'{parts[0]}_{unq}.{parts[1]}'

class Attatchments(models.Model):
    file = models.FileField(upload_to=nameTime)

    def __str__(self) -> str:
        return self.file.name