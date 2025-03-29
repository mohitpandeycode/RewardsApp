from django.db import models

# Create your models here.

class App(models.Model):
    CATEGORY_CHOICES = [
        ("Social Media", "Social Media"),
        ("Entertainment", "Entertainment"),
        ("Communication", "Communication"),
        ("Productivity", "Productivity"),
        ("Education", "Education"),
    ]

    SUBCATEGORY_CHOICES = [
        ("Social Networking", "Social Networking"),
        ("Messaging", "Messaging"),
        ("Content Sharing", "Content Sharing"),
        ("Professional Networking", "Professional Networking"),
        ("Community", "Community"),
        ("Task Management", "Task Management"),
        ("Music", "Music"),
        ("Learning", "Learning"),
    ]

    app_image = models.ImageField(upload_to="app_images/", default="app_images/default.jpg")
    app_name = models.CharField(max_length=255, unique=True)
    download_link = models.URLField()
    app_category = models.CharField(max_length=255, choices=CATEGORY_CHOICES, default="")
    subcategory = models.CharField(max_length=255, choices=SUBCATEGORY_CHOICES, default="")
    points = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.app_name
