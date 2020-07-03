from django.db import models

class Agent(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100)
    mobile_number = models.CharField(max_length = 15)
    profile_pic = models.ImageField(upload_to = 'agents/profile pic')

    def __str__(self):
        return self.name 
