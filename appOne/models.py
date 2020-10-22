from django.db import models

class showmanager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 3:
            errors["TitleOfShow"] = 'Title should be at least 3 characters'
        if len(postData['network']) < 2:
            errors["NetworkOfShow"] = 'Network should be at least 1 character'
        return errors


class show(models.Model):
    Title = models.CharField(max_length=255)
    Network = models.CharField(max_length=255)
    Release_date = models.DateField()
    Description = models.TextField(default="")
    objects = showmanager()
# Create your models here.


# MultiValueDictKey error getting information that its not expecting 