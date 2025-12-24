from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Auto.Status.PUBLISHED)#возращает все записи , которые публичны
    


# Create your models here.
class Auto(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, "Черновик"
        PUBLISHED = 1, "Опубликовано"
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    #slug = models.SlugField(max_length=255, blank=True, db_index=True, default="")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="Slug")
    content = models.TextField(blank=True, verbose_name="Контент")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", default=None,
                              blank=True, null=True, verbose_name="Фото")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания записи")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время обновления записи")
    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
    default=Status.DRAFT, verbose_name="Статус")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категории")
    tags = models.ManyToManyField("TagPost", blank=True, related_name="tags", verbose_name="Теги")
    engineer = models.OneToOneField('Engineer', on_delete=models.SET_NULL, 
                                   null=True, blank=True, related_name="autos", verbose_name="Инженер")
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL,
                               related_name='posts', null=True, default=None)


    def __str__(self):
        return self.title

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        verbose_name = "Автомобиль"
        verbose_name_plural = "Автомобили"
        ordering = ['-time_create']


    def get_absolute_url(self):
        return reverse("post", kwargs={"post_slug": self.slug})#где self это наша запись в БД
        

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def get_absolute_url(self):
        return reverse("category", kwargs={"cat_slug": self.slug})
        

class TagPost(models.Model):
    tag = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.tag
    
    def get_absolute_url(self):
        return reverse("tag", kwargs={"tag_slug": self.slug})
    

class Engineer(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True)

    def __str__(self):
        return self.name
    
class UploadFiles:
    file = models.FileField(upload_to="uploads_model")
