from django.urls import path, register_converter
from . import views
from . import convertors

register_converter(convertors.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.Home.as_view(), name='index'),
    path('about/', views.about, name='about'),
    path('addpage/', views.AddPage.as_view(), name='add_post'),
    path('contact/', views.ContactFormView.as_view(), name='contact'),
    path('login/', views.login, name='login'),
    path('post/<slug:post_slug>/', views.ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>', views.AutoCategory.as_view(), name='category'),
    path('tag/<slug:tag_slug>/', views.ShowTagPostlist.as_view(), name='tag'),
    path('edit/<int:pk>/', views.UpdatePage.as_view(), name='edit_page'),
    path('login/', views.login, name='login'),
]