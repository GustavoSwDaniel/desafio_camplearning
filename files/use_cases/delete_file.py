from django.shortcuts import get_object_or_404

from files.models import Files


class DeleteFileUseCase:
    def execute(self, pk: int):
        file_to_delete = get_object_or_404(Files, pk=pk)
        file_to_delete.delete()  
