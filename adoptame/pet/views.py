from django.shortcuts import render, get_object_or_404
from .models import Pet

def detail(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    context = {'pet': pet}

    return render(request, 'pet/detail.html', context)
