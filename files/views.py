# views.py

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from files.use_case.file_use_cases import DeleteFileUseCase, GetFilesForUserUseCase, RedirectToFilesUseCase, UploadFileUseCase

from .forms import FileForm

def redirect_to_files(request):
    use_case = RedirectToFilesUseCase()
    target_url = use_case.execute(request.user)
    return redirect(target_url)

@login_required
def file_list_view(request):
    use_case = GetFilesForUserUseCase()
    files = use_case.execute(request.user)
    return render(request, 'files/file_list.html', {'files': files})

@login_required
def file_upload_view(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            use_case = UploadFileUseCase()
            use_case.execute(request.user, request.FILES['file'])
            return redirect(reverse_lazy('file_list'))  
    else:
        form = FileForm()
    
    return render(request, 'files/upload_file.html', {'form': form})

@login_required
def file_delete_view(request, pk):
    if request.method == 'POST':
        use_case = DeleteFileUseCase()
        use_case.execute(pk)
        return redirect(reverse_lazy('file_list'))  
    else:
        use_case = GetFilesForUserUseCase()
        file_to_delete = use_case.execute(request.user).filter(pk=pk).first()
        return render(request, 'files/confirm_delete.html', {'file': file_to_delete})
