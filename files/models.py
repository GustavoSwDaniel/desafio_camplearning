from django.db import models

from users.models import CustomUser

class Files(models.Model):
    file_name = models.CharField(max_length=120, default=None)
    url = models.FileField(upload_to='uploads/')  
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  

    class Meta:
        ordering = ['-uploaded_at']
