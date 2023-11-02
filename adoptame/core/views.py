from django.shortcuts import render

from pet.models import Specie, Pet

def index(request):
    pets = Pet.objects.filter(adopted=False)
    species = Specie.objects.all()

    context = {
        'species': species,
        'pets': pets
    }

    return render(request, 'core/index.html', context)

def contact(request):
    return render(request, 'core/contact.html')
