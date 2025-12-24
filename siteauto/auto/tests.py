from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
from .models import Auto

# Create your tests here.
class GetPagesTestCase(TestCase):
    fixtures = ['auto_auto.json', 'auto_engineer.json', 'auto_category.json', 'auto_tagpost.json']
    
    def setUp(self):
        pass
    
    def test_mainpage(self):
        path = reverse('index')
        response = self.client.get(path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        # self.assertIn('auto/index.html', response.template_name)
        self.assertEqual(response.context_data['title'], "Главная страница")
        self.assertTemplateUsed(response, 'auto/index.html')

    
    def test_redirect_addpage(self):
        path = reverse('add_post')
        redirect_uri = reverse('users:login') + "?next=" + path
        response = self.client.get(path)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, redirect_uri)#первый параметр запрос и втроой куда надо перейти
        
    def test_data_mainpage(self):
        a = Auto.published.all().select_related('cat')
        path = reverse('index')
        response = self.client.get(path)
        self.assertQuerySetEqual(response.context_data['posts'], a[:5])
        
    def test_paginate_mainpage(self):
        path = reverse('index')
        page = 2
        paginate_by = 5
        response = self.client.get(path + f'?page={page}')
        a = Auto.published.all().select_related('cat')
        self.assertQuerySetEqual(response.context_data['posts'], a[(page-1)*paginate_by:page*paginate_by])
    
    
    def test_content_post(self):
        a = Auto.published.get(pk=2)
        path = reverse('post', args=[a.slug])
        response = self.client.get(path)
        self.assertEqual(a.content, response.context_data['post'].content)
    

    def tearDown(self):
        pass