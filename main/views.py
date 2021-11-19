from django.shortcuts import render
from .models import Profile


def index_view(request):
    profile = None
    if request.user.is_authenticated:
        try:
            profile = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            pass
    return render(request, 'index.html', {'profile': profile})
