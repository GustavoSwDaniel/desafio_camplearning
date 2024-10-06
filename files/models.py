from django.db import models

class Files(models.Model):
    file_name = models.CharField(max_length=120, default=None)
    url = models.FileField(upload_to='uploads/')  
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-uploaded_at']
