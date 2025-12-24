from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.template.loader import render_to_string
from .models import Auto, Category, TagPost, UploadFiles
from .forms import AddPost, UploadFileForm, ContactForm
from django.views import View
from django.views.generic import TemplateView , ListView, DetailView, FormView,CreateView, UpdateView
from .utils import DataMixin
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

menu = [{'title': 'About', 'url_name': 'about'},
        {'title': 'Add post', 'url_name': 'add_post'},
        {'title': 'Feedback', 'url_name': 'contact'},
        {'title': 'Login', 'url_name': 'login'},
        ]

data_db = [{"id":1, "title": "Kia Carnival", "content": "60 mph in 7.0 seconds", "is_public": True},
{"id":2, "title": "Toyota Sienna Hybrid", "content": "required 7.5 seconds to reach 60 mph.", "is_public": False},
{"id":3, "title": "Chrysler Voyager", "content": "7.3-second sprint to 60 mph.", "is_public": True}]

cats_db = [{'id':1, 'name':"Минивены"}, {'id':2, 'name':"Универсалы"}, {'id':3, 'name':"Микроавтобусы"}]

# Create your views here.
# def index(request):
#     # t = render_to_string('index.html')
#     # return HttpResponse(t)
#     posts = Auto.publised.all()
#     data = {
#         'title': 'Home page',
#         'menu': menu,
#         'posts': posts,
#         'cat_selected': 0,
#     }
#     return render(request, 'auto/index.html', context=data)

class Home(DataMixin,ListView):
    #model = Auto
    template_name = 'auto/index.html'
    context_object_name = 'posts'
    title_page = 'Главная страница'
    cat_selected=0
    def get_queryset(self):
        return Auto.published.all()
    
    # extra_context = {
    #     'title': 'Главная страница',
    #     'menu': menu,
    #     'posts': Auto.publised.all(),
    #     'cat_selected': 0
    # }
    
    # template_name = 'auto/index.html'
    # extra_content = {
    #     'title': 'Главная страница',
    #     'menu': menu,
    #     'posts': Auto.publised.all(),
    #     'cat_selected': 0
    # }
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = 'Главная страница'
    #     context['menu'] = menu
    #     context['posts'] = Auto.publised.all(),
    #     context['cat_selected'] = int(self.request.GET.get('cat_id', 0))

#def handle_uploaded_file(f):
#    with open(f"uploads/{f.name}", "wb+") as destination:
#        for chunk in f.chunks():
#            destination.write(chunk)

# def upload(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             #handle_uploaded_file(form.cleaned_data['file'])
#             fp = UploadFiles(file=form.cleaned_data['file'])
#             fp.save()
#     else:
#         form = UploadFileForm()
#     return render(request, 'auto/upload.html', {'title': "О сайте", 'menu': menu, 'form': form})

@login_required
def about(request):
    contact_list = Auto.published.all()
    paginator = Paginator(contact_list, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'auto/about.html', {'title': "О сайте", 'page_obj': page_obj})

# def add_page(request):
#     if request.method == 'POST':
#         form = AddPost(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
        #     try:
        #         Auto.objects.create(**form.cleaned_data)
        #         redirect('home')
            # except:
            #     form.add_error(None, "Ошибка добавления поста")
    # else:
    #     form = AddPost()

    # data = {
    #     'menu': menu,
    #     'title': 'Добавление поста',
    #     'form': form
    # }
    # return render(request, 'auto/addpost.html', data)

# class AddPage(View):
#     def get(self, request):
#         form = AddPost()
#         data = {
#             'menu': menu,
#             'title': 'Добавление поста',
#             'form': form
#         }
#         return render(request, 'auto/addpost.html', data)
#     def post(self, request):
#         form = AddPost(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#         data = {
#             'menu': menu,
#             'title': 'Добавление поста',
#             'form': form
#         }
#         return render(request, 'auto/addpost.html', data)

class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPost
    template_name = 'auto/addpost.html'
    title_page = "Добавление статьи"
    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)
    def form_valid(self, form):#form это как раз заполненная форма 
        w = form.save(commit=False)#обьект новой записи от БД, но записывать непосредственно в БД мы не будем
        w.author = self.request.user#атрибуту author мы присвоем текущего пользователя
        return super().form_valid(form)
    
class UpdatePage(DataMixin,UpdateView):
    model = Auto
    fields = ['title', 'content', 'photo', 'is_published', 'cat']
    template_name = 'auto/addpost.html'
    success_url = reverse_lazy('index')
    title_page = "Редактирование статьи"

class ContactFormView(LoginRequiredMixin, DataMixin, FormView):
    form_class = ContactForm
    template_name = 'auto/contact.html'
    success_url = reverse_lazy('index')
    title_page = "Обратная связь"
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

def login(request):
    return HttpResponse("Authorized")

# def show_post(request, post_slug):
#     post = get_object_or_404(Auto, slug=post_slug)
#     data = {
#         'title': post.title,
#         'menu': menu,
#         'post': post,
#         'cat_selected': 1,
#     }
#     return render(request, 'auto/post.html', data)

class ShowPost(DataMixin, DetailView):
    #model = Auto
    template_name = "auto/post.html"
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title=context['post'].title)
    
    def get_object(self, queryset=None):
        return get_object_or_404(Auto.published, slug=self.kwargs[self.slug_url_kwarg])


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>page not found</h1>")

# def show_category(request, cat_slug):
#     category = get_object_or_404(Category, slug=cat_slug)
#     posts = Auto.objects.filter(cat_id = category.pk)
#     print(posts)
#     data = {
#         'title':f'Рубрика: {category.name}',
#         'menu': menu,
#         'post': posts, 
#         'cat_selected': category.pk,
#             }
#     return render(request, 'auto/index.html', context=data)
class AutoCategory(DataMixin,ListView):
    template_name = 'auto/index.html'
    context_object_name = 'posts'
    # allow_empty=False

    def get_queryset(self):
        return Auto.published.filter(cat__slug=self.kwargs['cat_slug'])
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
    
        if context['posts']:
            cat = context['posts'][0].cat
            title = "Категория " + cat.name
            cat_selected = cat.pk
        else:
            cat = None
            title = "В этой категории пока нет постов"
            cat_selected = 0
    
        return self.get_mixin_context(context,
                                  title=title,
                                  cat_selected=cat_selected)
            
            
    
class ShowTagPostlist(DataMixin,ListView):
    template_name = 'auto/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        self.tag = get_object_or_404(TagPost, slug=self.kwargs['tag_slug'])
        return self.tag.tags.filter(is_published=Auto.Status.PUBLISHED)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = TagPost.objects.get(slug=self.kwargs['tag_slug'])
        return self.get_mixin_context(context, title="Тег: " + tag.tag)
