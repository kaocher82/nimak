from django.shortcuts import render
# +++ Import generic View +++
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.dates import YearArchiveView

# +++ Import Tag +++
from taggit.models import Tag
# +++ Import Custom models +++
from app.models import Post , Portfolio
# +++ import Utils +++
from django.utils import timezone



# === Index View Func ===
def index(request):
    return render(request, 'index.html')

# === Resume ===
def resume(request):
    return render(request, 'resume.html')

# === Portfolio ===
def portfolio(request):
    return render(request, 'portfolio.html')


# === Post Detail View ===
class TagMixin(object):
    def get_context_data(self, **kwargs):
        context = super(TagMixin, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context

# === Post Detail View ===
class PostDetailView(TagMixin, DetailView):
    model = Post
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

# === Post List View ===
class PostListView(TagMixin, ListView):
    model = Post
    paginate_by = '6'
    queryset = Post.objects.all().order_by('-pub')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

# === Post Year View ===
class PostYearArchiveView(YearArchiveView):
    queryset = Post.objects.all()
    date_field = "pub"
    make_object_list = True
    allow_future = True

# === Tag list View ===
class TagPostView(TagMixin, ListView):
    template_name = 'app/post_tag.html'
    model = Post
    paginate_by = '6'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs.get('slug'))
