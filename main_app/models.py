from django.db import models
from django.urls import reverse

BERRIES = (
  ('O', "Oran"),
  ('C', "Chesto"),
  ('P', 'Pecha'),
  ('R', 'Rawst'),
  ('A', 'Aspear'),
  ('S', 'Sitrus')
)

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

  def get_absolute_url(self):
    return reverse('detail', kwargs={'pokemon_id': self.id})

class Feeding(models.Model):
  date = models.DateField('feeding date')
  berry = models.CharField(
    max_length=1, 
    choices=BERRIES, 
    default=BERRIES[0][0]
    )

  pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.get_berry_display()} on {self.date}'
  
  class Meta:
    ordering = ['-date']