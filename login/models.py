from django.db import models

class Login(models.Model):
    id = models.IntegerField(primary_key=True)
    accesstoken = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Login"
