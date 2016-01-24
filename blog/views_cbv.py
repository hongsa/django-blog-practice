from django.core.urlresolvers import reverse_lazy
from django.shortcuts import resolve_url
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from blog.models import Post
from blog.forms import PostForm

index = TemplateView.as_view(template_name = 'blog/index.html')

class IndexView(TemplateView):
    template_name = 'blog/index.html'

index = IndexView.as_view()

post_list = ListView.as_view(model=Post, paginate_by=3)


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetailView,self).get_context_data(**kwargs)
        context['hello'] = 'world'
        return context

post_detail = PostDetailView.as_view()

# post_detail = DetailView.as_view(model=Post)


post_new = CreateView.as_view(model=Post, form_class=PostForm,
                              success_url=reverse_lazy('blog:post_list'))

# class PostEditView(UpdateView):
#     model = PostForm
#     form_class = PostForm
#
#     def get_success_url(self):
#         return resolve_url(self.object)

# post_edit = PostEditView.as_view()

post_edit = UpdateView.as_view(model=Post, form_class=PostForm)


post_delete = DeleteView.as_view(model=Post,success_url=reverse_lazy('blog:post_list'))