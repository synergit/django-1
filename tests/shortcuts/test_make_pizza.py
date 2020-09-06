from django.shortcuts import make_pizza
from django.test import SimpleTestCase


class MakePizzaTests(SimpleTestCase):
    def test_make_pizza(self):
        self.assertEqual(make_pizza(), 'pizza')