from django.test import TestCase

# Create your tests here.

import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Product

class ProductMethodTests(TestCase):

	def test_create_product(self):
		p = Product();
		p.description = 'Test Product';
        	p.itemID = 1337;
		p.lookupcode = '133713371337'
		self.assertEqual(p.in_stock(), False)
