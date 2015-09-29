from django.db import models

class Product(models.Model):
	description = models.CharField(max_length=200)
	lookupcode = models.IntegerField()
	price = models.DecimalField(max_digits=9, decimal_places=2)
	itemType = models.PositiveSmallIntegerField()
	cost = models.DecimalField(max_digits=9, decimal_places=2)
	quantity = models.IntegerField()
	reorderPoint = models.IntegerField()
	restockLevel = models.IntegerField()
	parentItem = models.ForeignKey('self')
	extendedDescription = models.TextField()
	active = models.BooleanField()
	msrp = models.DecimalField(max_digits=9, decimal_places=2)
	dateCreated = models.DateField(auto_now=False, auto_now_add=True)
