from django.db import models

class Url(models.Model):
    url = models.URLField()
    short_url = models.CharField(max_length=30)

    def __str__(self):
        return self.short_url
