from django.shortcuts import render, redirect
from django.views import generic
from django.contrib import auth
from blog.models import Post, Comment
from blog.forms import CommentForm


def IndexView(request):
    template_name = 'blog/index.html'
    context = {
        'object_list': Post.objects.all(),
        'username': auth.get_user(request).username,
    }
    return render(request, template_name, context)


def DetailView(request, pk):
    template_name = 'blog/detail.html'
    context = {
        'post': Post.objects.get(id=pk),
        'comments': Comment.objects.filter(comment_post_id=pk),
        'comment_form': CommentForm,
        'username': auth.get_user(request).username,
    }
    return render(request, template_name, context)


class AddComment(generic.View):

    def post(self, request, pk):

        if 'pause' not in request.session:
            form = CommentForm(request.POST)

            if form.is_valid():

                comment = form.save(commit=False)
                comment.comment_post = Post.objects.get(id=pk)
                form.save()
                request.session.set_expiry(60)
                request.session['pause'] = True

        return redirect('blog:detail', pk)







