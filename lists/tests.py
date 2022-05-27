from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from lists.views import home_page
from django.template.loader import render_to_string
import re

# Create your tests here.
class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func,home_page)

    def assertEqualExceptCSRF(self, html_code1, html_code2):
        csrf_regex = r'<input[^>]+csrfmiddlewaretoken[^>]+>'
        self.assertEqual(re.sub(csrf_regex, '', html_code1),re.sub(csrf_regex, '', html_code2))

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqualExceptCSRF(response.content.decode(),expected_html)

    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'

        response = home_page(request)
        self.assertIn('A new list item',response.content.decode())
        expected_html = render_to_string(
            'home.html',
            {'new_item_text':'A new list item'},
        )
        self.assertEqualExceptCSRF(response.content.decode(),expected_html)