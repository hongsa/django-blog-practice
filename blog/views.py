from django.shortcuts import render, get_object_or_404,redirect
from blog.models import Post
from blog.forms import PostForm


def index(request):
    return render(request, 'blog/index.html')


def post_list(request):
    post_list = Post.objects.all()
    return render(request, 'blog/post_list.html', {
        'post_list': post_list,
    })

def post_detail(request, pk):
    post = get_object_or_404(Post,pk=pk)
    return render(request,'blog/post_detail.html', {
        'post': post,
    })

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog:post_list')
    else:
        form=PostForm()
    return render(request,'blog/post_form.html', {
        'form': form,
    })

def post_edit(request, pk):
    post = get_object_or_404(Post,pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            #redirt로 인스턴스를 보낸 것은 model에 def get_absolute_url에서 이게 있으면 checking해서 이곳으로 url 보냄
            return redirect(post)
    else:
        form=PostForm(instance=post)
    return render(request,'blog/post_form.html', {
        'form': form,
    })

def post_delete(request, pk):
    post = get_object_or_404(Post,pk=pk)

    if request.method == 'POST':
        post.delete()
        return redirect('blog:post_list')

    return render(request, 'blog/post_confirm_delete.html')


