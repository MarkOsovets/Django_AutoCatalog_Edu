from django.contrib import admin, messages
from .models import Auto, Category

class EngineerFilter(admin.SimpleListFilter):
    title = "Есть ли инженер"
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return [
            ('unknown', "Неизвестен")
            ('known', "Известен")
        ]

        def queryset(self, request, queryset):
            if self.value() == "unknown":
                return queryset.filter(husband__isnull=False)
            elif self.value() == "known":
                return queryset.filter(husband__isnull=True)


@admin.register(Auto)
class AutoAdmin(admin.ModelAdmin):
    fields = ['title', 'content', 'slug', 'cat', 'engineer', 'tags']
    list_display = ('title', 'slug', 'content', 'time_create', 'is_published', 'brief_info')
    list_display_links = ('title', 'content')
    ordering = ['-time_create', 'title']
    list_editable = ('is_published',)
    list_per_page = 3   
    actions = ['set_publish', 'set_draft']
    search_fields = ['title']
    list_filter = ['cat__name', 'is_published']
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ('tags',)

    @admin.display(description="Краткое описание", ordering='content')
    def brief_info(self, auto: Auto):
        return f"Описание {len(auto.content)} символов."

    @admin.action(description="Опубликовать выбранные записи")
    def set_publish(self, request, queryset):
        count = queryset.update(is_published=Auto.Status.PUBLISHED)
        self.message_user(request, f"Измененно {count} записей")
    

    @admin.action(description="Снять с публикации выбранные записи")
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Auto.Status.DRAFT)
        self.message_user(request, f"{count} записей снято с публикации!", messages.WARNING)

    #def save(self, *args, **kwargs):
    #    self.slug = slugify(self.title)
    #    super().save(*args, **kwargs)



@admin.register(Category)
class CatAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
# Register your models here.
#admin.site.register(Auto, AutoAdmin)