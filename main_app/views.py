from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

class Pokemon:
  def __init__(self, name, type, height, weight, description, level):
    self.name = name
    self.type = type
    self.height = height
    self.weight = weight
    self.description = description
    self.level = level

pokemon = [
  Pokemon('Eevee', 'normal', '1 ft', '14.3 lbs', 'It has the ability to alter the composition of its body to suit its surrounding environment.', 15),
  Pokemon('Vulpix', 'fire', '2 ft', '21.8 lbs', 'While young it has six gorgeous tails. When it grows, several new tails are sprouted.', 6),
  Pokemon('Mareep', 'electric', '2 ft', '17.2 lbs', 'Clothing made from Mareep’s fleece is easily charged with static electricity, so a special process is used on it.', 10)
]

def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
  return render(request, 'about.html')

def pokemon_index(request):
  return render(request, 'pokemon/index.html', {'pokemon': pokemon })
