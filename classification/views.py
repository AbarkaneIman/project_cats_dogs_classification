import os
from django.conf import settings
from django.shortcuts import render


def home(request):
    # Dossiers des images
    cats_dir = os.path.join(settings.STATICFILES_DIRS[0], 'images/cats')
    dogs_dir = os.path.join(settings.STATICFILES_DIRS[0], 'images/dogs')
    
    # Liste des fichiers image dans chaque dossier
    cats_images = [f for f in os.listdir(cats_dir) if f.endswith(('.jpg', '.png', '.jpeg', '.gif'))]
    dogs_images = [f for f in os.listdir(dogs_dir) if f.endswith(('.jpg', '.png', '.jpeg', '.gif'))]
    
    return render(request, 'classification/interface1.html', {'cats_images': cats_images, 'dogs_images': dogs_images})


# Vue pour afficher l'interface1
def interface1(request):
    return render(request, 'classification/interface1.html')
