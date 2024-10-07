
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

from files.models import Files
from files.utils import generate_unique_name


class RedirectToFilesUseCase:
    def execute(self, user):
        if user.is_authenticated:
            return '/files/'
        else:
            return '/users/login/'

class GetFilesForUserUseCase:
    def execute(self, user):
        return Files.objects.filter(user_id=user)

class UploadFileUseCase:
    def execute(self, user, uploaded_file):
        new_filename = generate_unique_name(original_name=uploaded_file.name)
        file_path = default_storage.save(new_filename, ContentFile(uploaded_file.read()))

        Files.objects.create(url=file_path, file_name=new_filename, user_id=user)

class DeleteFileUseCase:
    def execute(self, file_id):
        file_to_delete = get_object_or_404(Files, pk=file_id)
        file_to_delete.delete()
        return reverse_lazy('file_list')
