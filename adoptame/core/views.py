from django.shortcuts import render, redirect

from pet.models import Specie, Pet
from .forms import SignupForm

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

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {'form': form})
