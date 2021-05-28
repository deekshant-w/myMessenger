from django.db import models
from django.utils import timezone

class Message(models.Model):
    heading = models.CharField(max_length=256)
    tags = models.CharField(max_length=256)
    message = models.TextField()
    files = models.ForeignKey(to='Attatchments',on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.heading or self.message[:20] or self.tags[:20] or self.edited

def nameTime(instance, filename):
    parts = filename.split('.')
    unq = timezone.now().strftime("%y_%m_%d_%H_%M_%S")
    return f'{parts[0]}_{unq}.{parts[1]}'

class Attatchments(models.Model):
    file = models.FileField(upload_to=nameTime)

    def __str__(self) -> str:
        return self.file.name