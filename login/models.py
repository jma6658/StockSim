from django.db import models

class Login(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.TextField()
    password = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Login"
