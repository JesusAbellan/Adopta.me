from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .forms import NewPetForm, EditPetForm
from .models import Pet

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
