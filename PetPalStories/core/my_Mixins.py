from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect


class OwnerRequiredMixin(LoginRequiredMixin):

    def dispatch(self, request, *args, **kwargs):

        url_user_pk = kwargs.get('pk', None)

        if url_user_pk and url_user_pk != request.user.pk:
            messages.error(request, 'You are not authorized to see this page')
            return redirect('index')

        return super().dispatch(request, *args, **kwargs)


def is_owner(request, obj):
    if obj.owner != request.user:
        messages.error(request, 'You are not authorized to see this page')
        return redirect('index')