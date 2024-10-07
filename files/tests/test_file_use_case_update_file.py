import os
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from unittest import mock
from moto import mock_aws
import boto3
from django.contrib.auth import get_user_model

from files.models import Files
from files.use_case.file_use_cases import UploadFileUseCase


class UploadFileUseCaseTest(TestCase):
    bucket_name = "enowshopv2" # Bucket Pessoal de teste
    def setUp(self):
        self.mock_aws = mock_aws()
        self.mock_aws.start()

        self.aws_credentials = {
            'AWS_ACCESS_KEY_ID': 'fake_access_key',
            'AWS_SECRET_ACCESS_KEY': 'fake_secret_key',
            'AWS_STORAGE_BUCKET_NAME': self.bucket_name,
            'AWS_S3_REGION_NAME': 'us-east-1',
        }
        self.patcher = mock.patch.dict('os.environ', self.aws_credentials)
        self.patcher.start()

        self.s3_client = boto3.resource('s3')
        self.s3_client.create_bucket(Bucket="{}".format(self.bucket_name))
        User = get_user_model()
        self.user = User.objects.create_user(
            email='testuser@example.com',
            password='12345Teste!!',
            name='teste'
        )

       
        
        self.use_case = UploadFileUseCase()

    def tearDown(self):
        self.mock_aws.stop()
        self.patcher.stop()  

    def test_file_upload(self):
        uploaded_file = SimpleUploadedFile("testfile.txt", b"file_content", content_type="text/plain")
        
        self.use_case.execute(user=self.user, uploaded_file=uploaded_file)
        
      
