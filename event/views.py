from django.shortcuts import render

# Create your views here.
def deneme_event(request):
    return render(request, 'event_details.html', {})

def deneme_home(request):
    return render(request, 'home.html', {})

