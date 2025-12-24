from captcha.fields import CaptchaField
from django import forms 
from .models import Category, Engineer, Auto
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.core.exceptions import ValidationError

# class AddPost(forms.Form):
#     title = forms.CharField(max_length=255, min_length=10, label="Заголовок", widget=forms.TextInput(attrs={'class': 'form-input'}), 
#                             error_messages={'min_length':'Слишком короткий заголовок', 'required': 'Без заголовка никак'})
#     slug = forms.SlugField(max_length=255, label="Слаг", validators=[MinLengthValidator(5, message="Минимум 5 символов"),
#                                                                     MaxLengthValidator(100, message="Максимум 100 символов")])
#     content = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 5}), label="Контент")
#     is_published = forms.BooleanField(label="Статус публикации", required=False, initial=True)
#     cat = forms.ModelChoiceField(queryset=Category.objects.all(), label="Категория", empty_label="Категория не выбрана")
#     engineer = forms.ModelChoiceField(queryset=Engineer.objects.all(), label="Инженер", empty_label="Не выбран")

#     def clean_title(self):
#         title = self.cleaned_data["title"]
#         av = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ0123456789-?!$#@_"

#         if not(set(title) <= set(av)):
#             raise ValidationError("Должны пристуствовать только русские символы, дефис и пробел")

class AddPost(forms.ModelForm):   
    #прописываем для того чтобы были значения у нас вместо черточек, а так можжно и без них
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), label="Категория", empty_label="Категория не выбрана")
    engineer = forms.ModelChoiceField(queryset=Engineer.objects.all(), label="Инженер", empty_label="Не выбран", required=False)                                                    
    class Meta:
        model = Auto
        fields = ['title', 'slug', 'content','photo', 'is_published', 'cat', 'engineer']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 50, 'rows': 5})
        }
        labels = {'slug': 'URL'}

    

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title)>50:
            raise ValidationError("Слишком длинный заголовок боее 50 символов")
        
        return title

        
class UploadFileForm(forms.Form):
    file = forms.FileField(label="Файл")
    
    
class ContactForm(forms.Form):
    name = forms.CharField(label="Имя", max_length=255)
    email = forms.CharField(label="Email")
    contact = forms.CharField(widget=forms.Textarea(attrs={'cols': '60', 'rows': '10'}))
    captcha = CaptchaField()