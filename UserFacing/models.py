from django.db import models
from AdminFacing.models import App
from django.contrib.auth.models import AbstractUser
import uuid
from django.utils import timezone
import datetime
# Create your models here.

class CustomUser(AbstractUser):
    uid = models.UUIDField(max_length=100, default=uuid.uuid4, editable=False)
    phone_number = models.IntegerField(unique=True,null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.username
    

class OTP(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    timestamp = models.DateTimeField(auto_now_add=True)
    expiry = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.expiry = timezone.now() + datetime.timedelta(minutes=5)
        super(OTP, self).save(*args, **kwargs)

    def __str__(self):
        return f"OTP for {self.user.username}"

    def is_valid(self):
        return timezone.now() <= self.expiry
    

class UserDownload(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    app = models.ForeignKey(App, on_delete=models.CASCADE)
    downloaded_at = models.DateTimeField(auto_now_add=True)
    screenshot = models.ImageField(upload_to='screenshots/', null=True, blank=True)
    is_downloaded = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.user.username} downloaded {self.app.app_name}"