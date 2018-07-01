from django.test import TestCase
from django.core.urlresolvers import resolve, reverse
from django.http import HttpRequest

from .views import menu_list, menu_detail, item_detail



class MenuTest(TestCase):

    def test_homepage_displays_from_root_url(self):
        home_page = resolve('/')
        self.assertEqual(home_page.func, menu_list)

    def test_menu_detail_from_menu_url(self):
        blanditiis = resolve('/menu/32/')
        self.assertEqual(blanditiis.func, menu_detail)

    def test_menu_item_from_url(self):
        soda = resolve('/menu/item/1/')
        self.assertEqual(soda.func, item_detail)

    def test_menu_list_returns_html(self):
        request = HttpRequest()
        response = menu_list(request)
        html = response.content.decode('utf8')
        self.assertIn('<title>Soda Fountain</title>', html)
