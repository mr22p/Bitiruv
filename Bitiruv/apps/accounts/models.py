from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profiles/', default='default.png')
    project_name = models.CharField(max_length=200)
    project_description = models.TextField()
    project_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.user.username