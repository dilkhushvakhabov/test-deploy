from django.shortcuts import render
from .models import Profile


def index_view(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = None
    return render(request, 'index.html', {'profile': profile})
