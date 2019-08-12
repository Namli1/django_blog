from django.shortcuts import render
from blog.models import BlogPost, BlogComment, BlogAuthor
from django.views import generic
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
def index(request):
    num_posts = BlogPost.objects.all().count()
    num_authors = BlogAuthor.objects.all().count()

    context = {
        'num_posts' : num_posts,
        'num_authors' : num_authors,
    }

    return render(request, 'index.html', context=context)

class BlogPostListView(generic.ListView):
    model = BlogPost
    paginate_by = 5

class BlogPostDetailView(generic.DetailView):
    model = BlogPost

class AuthorListView(generic.ListView):
    model = BlogAuthor
    paginate_by = 5

class AuthorDetailView(generic.ListView):
    model = BlogPost
    paginate_by = 5
    template_name = 'blog/blog_list_by_author.html'

    def get_queryset(self):
        """
        Return list of Blog objects created by BlogAuthor (author id specified in URL)
        """
        #Getting the Primary Key (pk) from the URL-elements via self.kwargs['pk'] (in kwargs, the elements are stored)
        id = self.kwargs['pk']
        #Getting the author object with the specified pk (see above)
        target_author = get_object_or_404(BlogAuthor, pk=id)
        #returning the filtered model
        return BlogPost.objects.filter(author=target_author)

    def get_context_data(self, **kwargs):
        # get the context from AuthorDetailView first (obligatory)
        context = super(AuthorDetailView, self).get_context_data(**kwargs)
        # add an object to it, here the BlogAuthor-Object for the specified pk
        context['blogger'] = get_object_or_404(BlogAuthor, pk= self.kwargs['pk'])
        return context


class BlogCommentAdd(LoginRequiredMixin, CreateView):
    model = BlogComment
    fields = ['description']

    def get_context_data(self, **kwargs):
        context = super(BlogCommentAdd, self).get_context_data(**kwargs)
        context['title'] = get_object_or_404(BlogPost, pk = self.kwargs['pk'])
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = get_object_or_404(BlogPost, pk = self.kwargs['pk'])
        return super(BlogCommentAdd, self).form_valid(form)

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.kwargs['pk'],})


class BlogCommentDelete(DeleteView):
    model = BlogComment
    success_url = reverse_lazy('posts')

class BlogPostCreate(LoginRequiredMixin, CreateView):
    model = BlogPost
    fields = ['title', 'text']
    def form_valid(self, form):
        form.instance.author, created = BlogAuthor.objects.get_or_create(user=self.request.user, defaults={'bio': 'I am a blog author, you can see my posts below.'},)
        #TODO: Test if BlogPostCreate also works with user who is not an BlogAuthor object => Does not work
        return super(BlogPostCreate, self).form_valid(form)

class BlogPostDelete(LoginRequiredMixin, DeleteView):
    model = BlogPost
    success_url = reverse_lazy('all-posts')

    #def get_queryset(self):
     #   id = self.request.user.id
      #  target_author = get_object_or_404(BlogAuthor, pk=id)
       # return BlogPost.objects.filter(author=target_author)



