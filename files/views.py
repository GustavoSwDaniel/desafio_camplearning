# files/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.contrib.auth.decorators import login_required

from files.utils import generate_unique_name
from .models import Files
from .forms import FileForm


def redirect_to_files(request):
    if request.user.is_authenticated:
        return redirect('/files/')
    else:
        return redirect('/users/login/')

@login_required 
def file_list_view(request):
    files = Files.objects.filter(user_id=request.user)
    return render(request, 'files/file_list.html', {'files': files})

@login_required 
def file_upload_view(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            new_filename = generate_unique_name(original_name=uploaded_file.name)

            file_path = default_storage.save(new_filename, ContentFile(uploaded_file.read()))

            Files.objects.create(url=file_path, file_name=new_filename, user_id=request.user)
            return redirect(reverse_lazy('file_list'))  
    else:
        form = FileForm()
    
    return render(request, 'files/upload_file.html', {'form': form})

@login_required 
def file_delete_view(request, pk):
    file_to_delete = get_object_or_404(Files, pk=pk)
    if request.method == 'POST':
        file_to_delete.delete()  
        return redirect(reverse_lazy('file_list'))  
    return render(request, 'files/confirm_delete.html', {'file': file_to_delete})
