from django import template
import auto.views as views
from auto.models import Category

register = template.Library()


@register.inclusion_tag('auto/list_categories.html')
def show_categories(cat_selected=0):
    cats = Category.objects.all()
    return {'cats': cats, 'cat_selected': cat_selected}


@register.simple_tag
def get_menu():
    return menu