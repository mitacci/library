from django.db import models


# Create your models here.
class Profile(models.Model):
    NAMES_MAX_LEN = 30
    first_name = models.CharField(
        max_length=NAMES_MAX_LEN,
    )
    last_name = models.CharField(
        max_length=NAMES_MAX_LEN,
    )
    image_url = models.URLField()

    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):
    TITLE_MAX_LEN = 30
    TYPE_MAX_LEN = 30
    title = models.CharField(
        max_length=TITLE_MAX_LEN,
    )
    description = models.TextField()
    image = models.URLField()
    type = models.CharField(
        max_length=TYPE_MAX_LEN,
    )