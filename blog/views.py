from django.shortcuts import render, redirect
from django.views import generic
from django.contrib import auth
from django.core.paginator import Paginator
from blog.models import Post, Comment, Category
from blog.forms import CommentForm


def IndexView(request, page_number=1):
    template_name = 'blog/index.html'
    all_posts = Post.objects.all()
    current_page = Paginator(all_posts, 4)
    context = {
        'object_list': current_page.page(page_number),
        'username': auth.get_user(request).username,
        'categories': Category.objects.all(),
    }
    return render(request, template_name, context)


def DetailView(request, pk):
    template_name = 'blog/detail.html'
    context = {
        'post': Post.objects.get(id=pk),
        'comments': Comment.objects.filter(comment_post_id=pk),
        'comment_form': CommentForm,
        'username': auth.get_user(request).username,
        'categories': Category.objects.all(),
    }
    return render(request, template_name, context)


def CategoryView(request, pk, page_number=1):
    template_name = 'blog/category.html'
    category_posts = Post.objects.filter(post_category_id=pk)
    current_page = Paginator(category_posts, 4)
    context = {
        'object_list': current_page.page(page_number),
        'category': Category.objects.get(id=pk),
        'username': auth.get_user(request).username,
        'categories': Category.objects.all(),
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








