# files/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from files.use_cases.upload_file import UploadFileUseCase
from .models import Files
from .forms import FileForm
import uuid

def file_list_view(request):
    files = Files.objects.all()
    return render(request, 'files/file_list.html', {'files': files})


def file_upload_view(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        upload_file_use_case = UploadFileUseCase()
        response = upload_file_use_case.execute(form=form, file=request.FILES)
        if response:
            return redirect(reverse_lazy('file_list'))  
    else:
        form = FileForm()
    return render(request, 'files/upload_file.html', {'form': form})


def file_delete_view(request, pk):
    file_to_delete = get_object_or_404(Files, pk=pk)
    if request.method == 'POST':
        file_to_delete.delete()  
        return redirect(reverse_lazy('file_list'))  
    return render(request, 'files/confirm_delete.html', {'file': file_to_delete})
