from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

User = get_user_model()

@method_decorator(csrf_exempt, name='dispatch')
class UserRegisterView(View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            email = data.get('email')
            password = data.get('password')
            if not email or not password:
                return JsonResponse({'error': 'Email and password are required.'}, status=400)
            
            if User.objects.filter(email=email).exists():
                return JsonResponse({'error': 'User with this email already exists.'}, status=400)
            
            user = User.objects.create_user(email=email, password=password)
            return JsonResponse({'message': 'User created successfully.'}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

class UserLoginView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            email = data.get('email')
            password = data.get('password')
            if not email or not password:
                return JsonResponse({'error': 'Email and password are required.'}, status=400)

            user = authenticate(request, email=email, password=password)
            if user is None:
                return JsonResponse({'error': 'Invalid credentials.'}, status=401)
            
            refresh = RefreshToken.for_user(user)
            return JsonResponse({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)