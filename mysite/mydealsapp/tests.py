from django.test import TestCase
from mydealsapp.models import product

# Create your tests here.

class ProductTestCase(TestCase):
	
	def setUp(self):
		print('setUp activity')
		product.ojects.create(name='bujji',description = 'my app', costitem = 1000, stockquantity = '2',volume = 2000)
		product.ojects.create(name='bangaram',description = 'my dog', costitem = 5000, stockquantity = '3', volume = 15000)

	def test_product_info(self):
	   
	    qs=product.objects.all()
	    self.assertEqual(qs.count(),2)
	    p1=product.objects.get(CostItem = 1000)	
	    p2=product.objects.get(CostItem = 5000)
	    self.assertEqual(p1,get_volume,2000)
	    self.assertEqual(p2.get_volume,15000)
