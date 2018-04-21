from django.test import TestCase
from .models import Card, List


class ScrumboardCardTester(TestCase):
    def setUp(self):
        list1 = List.objects.create(name="List 1")
        Card.objects.create(list=list1, title='card1',description='card1 desc',story_points=1,business_value=1)

    
    def test_cards(self):
        card1 = Card.objects.get(title='card1')
        self.assertEqual(card1.description, 'card1 desc')

class ScrumboardListTester(TestCase):
    def setUp(self):
        list1 = List.objects.create(name="List 1")


    def test_list(self):
        list1 = List.objects.get(name='List 1')
        self.assertEqual(list1.name, 'List 1')