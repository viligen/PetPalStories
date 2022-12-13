from django.contrib import messages
from django.utils.deprecation import MiddlewareMixin


class CustomHeaderMiddleware(MiddlewareMixin):
    def __call__(self, request):
        response = super().__call__(request)
        response['X-My-Header'] = "PetPalStories"
        return response


class CustomMessageMiddleware(MiddlewareMixin):
    def __call__(self, request):
        if not request.user.is_authenticated:
            messages.warning(request, 'Please sign in or sign up to gain full access to all features')

        response = super().__call__(request)
        return response