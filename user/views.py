from django.shortcuts import render, redirect
from user.models import User
from ticket_system.decorators import admin_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from user.forms import UserForm
from ticket.models import Ticket
from event.models import Comment


# Create your views here.
def deneme_profile(request):
    user = request.user
    tickets = Ticket.objects.filter(user=user)
    for ticket in tickets:
        print(ticket.event.name)
    comments = Comment.objects.filter(user=user)
    return render(request, 'profile.html', {'user': user, 'tickets': tickets, 'comments': comments},)


def edit_profile(request):
    if request.method == 'POST':
        form = UserForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('profile_page')
    else:
        form = UserForm(request.POST, instance=request.user)
    return render(request, 'user_update.html', {'form': form})
