from django.test import TestCase
from files.models import Files
from files.use_case.file_use_cases import DeleteFileUseCase
from django.contrib.auth import get_user_model

class DeleteFileUseCaseTest(TestCase):
    def setUp(self):
        User = get_user_model()
        self.use_case = DeleteFileUseCase()
        self.user = User.objects.create_user(name='teste', email='testuser', password='12345')
        self.file = Files.objects.create(file_name='file_to_delete.txt', url='file_url', user_id=self.user)

    def test_delete_file(self):
        self.use_case.execute(file_id=self.file.id)
        self.assertFalse(Files.objects.filter(id=self.file.id).exists())
