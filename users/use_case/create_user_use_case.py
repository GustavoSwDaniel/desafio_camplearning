from django.contrib.auth import login
from django.shortcuts import redirect
from users.forms import UserForm

class CreateUserUseCase:
    def __init__(self, request):
        self.request = request
        self.form = UserForm()

    def execute(self):
        if self.request.method == 'POST':
            self.form = UserForm(self.request.POST)
            if self.form.is_valid():
                user = self.form.save()
                login(self.request, user)
                return redirect('file_list')
        return self.form

