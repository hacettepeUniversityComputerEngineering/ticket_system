from django.shortcuts import render

# Create your views here.
def deneme_profile(request):
    return render(request, 'profile.html', {})
