from django.shortcuts import render
from .models import Post, Like
from django.views.generic import View, TemplateView
from django.http import JsonResponse
# Create your views here.
def post_view(request):
    qs = Post.objects.all()
    user = request.user
    context = {
        'qs': qs,
        'user': user,
    }
    return render(request, 'posts/main.html', context)


class PostJsonListView(View):
    def get(self, *args, **kwargs):
        print(kwargs)
        upper = kwargs.get('num_posts')
        lower = upper-3
        posts = list(Post.objects.values()[lower:upper])
        return JsonResponse({'data': posts}, safe=False)