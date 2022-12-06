from django.utils.deprecation import MiddlewareMixin


class CustomHeaderMiddleware(MiddlewareMixin):
    def __call__(self, request):
        response = super().__call__(request)
        response['X-My-Header'] = "PetPalStories"
        return response