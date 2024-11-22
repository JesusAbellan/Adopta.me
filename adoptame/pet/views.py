from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .forms import NewPetForm, EditPetForm
from django.db.models import Q
from .models import Pet, Specie, Race

def pets(request):
    query = request.GET.get('query','')
    maxAge = request.GET.get('maxAge', 20)
    specie_id = request.GET.get('specie', 0)
    race_id = request.GET.get('race', 0)
    species = Specie.objects.all()
    races = Race.objects.all()
    pets = Pet.objects.filter(adopted=False)

    if query:
        pets = pets.filter(Q(name__icontains=query) | Q(description__icontains=query))

    if specie_id:
        pets = pets.filter(specie_id=specie_id)

    if race_id:
        pets = pets.filter(race_id=race_id)

    pets = pets.filter(age__lte=maxAge)

    return render(request, 'pet/pets.html', {
        'pets':pets,
        'query':query,
        'maxAge': int(maxAge),
        'species': species,
        'specie_id': int(specie_id),
        'races': races,
        'race_id': int(race_id)
    })

def detail(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    context = {'pet': pet}

    return render(request, 'pet/detail.html', context)

@login_required
def new(request):
    if request.method == 'POST':
        form = NewPetForm(request.POST, request.FILES)

        if form.is_valid():
            pet = form.save(commit=False)
            pet.created_by = request.user
            pet.save()

            return redirect('pet:detail', pk=pet.id)
    else:
        form = NewPetForm()

    return render(request, 'pet/form.html', {'form': form, 'title': 'Tu nueva mascota'})


@login_required
def edit(request, pk):
    pet = get_object_or_404(Pet, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditPetForm(request.POST, request.FILES, instance=pet)

        if form.is_valid():
            form.save()

            return redirect('pet:detail', pk=pet.id)
    else:
        form = EditPetForm(instance=pet)

    return render(request, 'pet/form.html', {'form': form, 'title': 'Edita tu mascota'})

@login_required
def delete(request, pk):
    pet = get_object_or_404(Pet, pk=pk, created_by=request.user)
    pet.delete()

    return redirect('dashboard:index')

def get_races(request):
    specie_id = request.GET.get('specie')
    races = Race.objects.filter(specie=specie_id).order_by('name')

    response_data = {
        "races": list(races)
    }

    return JsonResponse(response_data)
