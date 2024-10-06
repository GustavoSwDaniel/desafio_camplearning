import uuid
from files.forms import FileForm
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from files.models import Files


class UploadFileUseCase:
    def generate_unique_name(self, original_name: str):
        file_type = original_name[-3:]
        new_name = f'{str(uuid.uuid4()).replace('-', '')}.{file_type}'
        return new_name

    def execute(self, form: FileForm, file):
        if form.is_valid():
            uploaded_file = file['file']
            new_filename = self.generate_unique_name(original_name=uploaded_file.name)

            file_path = default_storage.save(new_filename, ContentFile(uploaded_file.read()))
            Files.objects.create(url=file_path, file_name=new_filename)
            return True
        return False