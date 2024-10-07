from django.shortcuts import render

from users.user_case.create_user_use_case import CreateUserUseCase

def create_user(request):
    use_case = CreateUserUseCase(request)
    form = use_case.execute()

    return render(request, 'users/register_user.html', {'form': form})
