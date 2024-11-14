from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from pet.models import Pet

@login_required
def index(request):
    pets = Pet.objects.filter(created_by=request.user)

    return render(request, 'dashboard/index.html', {'pets': pets})
