from django.db import models

class Spotifytoken(models.Model):
    user_id = models.CharField(max_length=500, unique=True)
    refresh_token = models.CharField(max_length=500)
    access_token = models.CharField(max_length=500)
    expires_in = models.CharField(max_length=50)
    token_type = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return f"USER_ID = {self.user_id}"
