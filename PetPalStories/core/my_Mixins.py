from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic.detail import SingleObjectMixin


class OwnershipRequiredMixin(LoginRequiredMixin):

    def dispatch(self, request, *args, **kwargs):

        url_user_pk = kwargs.get('pk', None)

        if url_user_pk and url_user_pk != request.user.pk:
            messages.error(request, 'You were not authorized to see this content. You have been redirected to home page')
            return redirect('index')

        return super().dispatch(request, *args, **kwargs)


class IsOwnerMixin(SingleObjectMixin, LoginRequiredMixin):
    obj = None

    def get_object(self, queryset=None):
        self.obj = super().get_object(queryset)

        return self.obj

    def dispatch(self, request, *args, **kwargs):
        self.get_object(queryset=None)

        if hasattr(self.obj, 'owner') is not None and self.obj.owner_id != request.user.pk:
            messages.error(request, 'You were not authorized to see this content. You have been redirected to home page')
            return redirect('index')

        return super().dispatch(request, *args, **kwargs)