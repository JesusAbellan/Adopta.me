from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, get_object_or_404, redirect
from .models import PetOwner
from .forms import EditPetOwnerForm

@user_passes_test(lambda u: u.is_superuser)
def index(request):
    users = PetOwner.objects.all()

    context = {
        'users': users
    }

    return render(request, 'user/index.html', context)


@user_passes_test(lambda u: u.is_superuser)
def edit(request, pk):
    pet = get_object_or_404(PetOwner, pk=pk)

    if request.method == 'POST':
        form = EditPetOwnerForm(request.POST, request.FILES, instance=pet)

        if form.is_valid():
            form.save()

            return redirect('user:index')
    else:
        form = EditPetOwnerForm(instance=pet)

    return render(request, 'user/form.html', {'form': form, 'title': f'Editar {PetOwner.username}' })

@user_passes_test(lambda u: u.is_superuser)
def delete(request, pk):
    pet = get_object_or_404(PetOwner, pk=pk)
    pet.delete()

    return redirect('user:index')
