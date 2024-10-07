from django.test import TestCase, RequestFactory
from django.contrib.auth import get_user_model
from django.contrib.sessions.middleware import SessionMiddleware

from users.use_case.create_user_use_case import CreateUserUseCase

class CreateUserUseCaseTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user_data = {
            'email': 'testuser@example.com',
            'password1': '12345Teste!!',
            'password2': '12345Teste!!', 
            'name': 'Test User'
        }

    def _add_session(self, request):
        middleware = SessionMiddleware(lambda x: x)  
        middleware.process_request(request)
        request.session.save() 

    def test_create_user_valid_data(self):
        request = self.factory.post('/fake-url/', data=self.user_data)
        self._add_session(request)

        use_case = CreateUserUseCase(request)
        form_result = use_case.execute()

        User = get_user_model()
        self.assertEqual(User.objects.count(), 1)

        user = User.objects.get()
        self.assertEqual(user.email, self.user_data['email'])
        self.assertEqual(user.name, self.user_data['name'])

        self.assertTrue(user.is_authenticated)

    def test_create_user_invalid_data(self):
        invalid_data = {
            'email': '',  
            'password1': '12345Teste!!',
            'password2': '12345Teste!!', 
            'name': 'Test User'
        }
        
        request = self.factory.post('/fake-url/', data=invalid_data)
        self._add_session(request)

        use_case = CreateUserUseCase(request)
        form_result = use_case.execute()

        User = get_user_model()
        self.assertEqual(User.objects.count(), 0)

        self.assertTrue(form_result.errors)
