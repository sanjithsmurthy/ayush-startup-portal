from django.shortcuts import render
import json
from .models import Animation

def load_animation_data():
    with open('path/to/typing.json', 'r') as file:
        data = json.load(file)
    
    animation = Animation(name=data['nm'], data=data)
    animation.save()

def index(request):
    return render(request, 'app/index.html')

def animation_view(request):
    animation = Animation.objects.first()  # Simplified for example
    return render(request, 'animation_template.html', {'animation': animation}