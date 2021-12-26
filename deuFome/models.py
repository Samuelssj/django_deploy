from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class MakeOrder(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    final_date = models.DateTimeField(blank=True, null=True)

    def send_Order(self):
        self.final_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

