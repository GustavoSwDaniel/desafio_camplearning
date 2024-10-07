from django.test import TestCase
from files.models import Files
from files.use_case.file_use_cases import GetFilesForUserUseCase
from django.contrib.auth import get_user_model

class GetFilesForUserUseCaseTest(TestCase):
    def setUp(self):
        self.use_case = GetFilesForUserUseCase()
        User = get_user_model()
        self.user = User.objects.create_user(name='teste', email='testuser', password='12345')
        self.file1 = Files.objects.create(file_name='file1.txt', url='file1_url', user_id=self.user)
        self.file2 = Files.objects.create(file_name='file2.txt', url='file2_url', user_id=self.user)

    def test_get_files_for_user(self):
        files = self.use_case.execute(user=self.user)
        self.assertIn(self.file1, files)
        self.assertIn(self.file2, files)
