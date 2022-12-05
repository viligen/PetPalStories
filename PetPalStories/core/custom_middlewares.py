from django.utils.deprecation import MiddlewareMixin


class CustomHeaderMiddleware(MiddlewareMixin):
    @staticmethod
    def process_request(request):
        request.META['HTTP_CUSTOM_HEADER'] = "PetPalStories"