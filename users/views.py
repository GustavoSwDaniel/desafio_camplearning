from django.shortcuts import redirect, render
from django.contrib.auth import login

from users.forms import UserForm


def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('file_list')
    else:
        form = UserForm()
    return render(request, 'users/register_user.html', {'form': form})
