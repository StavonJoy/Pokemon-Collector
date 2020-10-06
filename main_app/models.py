from django.db import models

# Create your models here.
class Pokemon(models.Model):
  name = models.CharField(max_length=100)
  type = models.CharField(max_length=100)
  height = models.IntegerField()
  weight = models.IntegerField()
  description = models.TextField(max_length=250)
  level = models.IntegerField()

  def __str__(self):
    return self.name