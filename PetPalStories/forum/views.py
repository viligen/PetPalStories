from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import mixins as auth_mixins

from PetPalStories.forum.forms import PostCreateForm
from PetPalStories.forum.models import Post


class PostsListView(generic.ListView):
    PAGE_SIZE = 3
    model = Post
    template_name = 'forum/posts-dashboard.html'
    context_object_name = 'posts'

    paginate_by = PAGE_SIZE

    def get_queryset(self):
        query = self.request.GET.get('query', '').strip()

        object_list = self.model.objects.all()
        if query:
            object_list = object_list.filter(topic__icontains=query)
        return object_list


class PostAddView(auth_mixins.LoginRequiredMixin, generic.CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'forum/post-add.html'
    success_url = reverse_lazy('forum dashboard')

    def form_valid(self, form):
        form.instance.owner_id = self.request.user.pk
        return super().form_valid(form)