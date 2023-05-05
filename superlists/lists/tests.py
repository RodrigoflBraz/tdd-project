from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page

class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTrue(
            any(row.text == '1: Estudar testes funcionais' for row in rows),
            "New to-do item did not appear in table"
            )
