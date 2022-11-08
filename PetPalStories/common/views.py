from django.shortcuts import render, redirect


def index_view(request):

    if request.user.is_authenticated:
        return redirect('stories')
    return render(request, 'common/index.html')