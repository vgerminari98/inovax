from django.db import models

class Ebook(models.Model):
    title = models.CharField(max_length=255, unique=True)
    file = models.FileField(upload_to='ebooks/')
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
