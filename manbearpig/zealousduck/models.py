from django.db import models

# Create your models here.

class Product(models.Model):
        description = models.CharField(max_length=200)
        itemID = models.PositiveSmallIntegerField()
	lookupcode = models.CharField(max_length=30)
        price = models.DecimalField(max_digits=10, decimal_places=2)
        itemType = models.PositiveSmallIntegerField()
        cost = models.DecimalField(max_digits=10, decimal_places=2)
        quantity = models.IntegerField()
        reorderPoint = models.IntegerField()
        restockLevel = models.IntegerField()
        parentID = models.PositiveSmallIntegerField()
        extendedDescription = models.TextField()
        active = models.BooleanField()
        msrp = models.DecimalField(max_digits=10, decimal_places=2)
        dateCreated = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return self.description

class Employee(models.Model):
	name_first = models.CharField(max_length=100)
	name_last = models.CharField(max_length=100)
	active = models.BooleanField()
	type = models.PositiveSmallIntegerField()
	password = models.CharField(max_length=100)
	timestamp = models.DateField(auto_now=False, auto_now_add=True)

class Transaction(models.Model):
	cashierID = models.ForeignKey(Employee)
	amount = models.DecimalField(max_digits=10, decimal_places=2)
	transactionType = models.PositiveSmallIntegerField()
	parent = models.ForeignKey('self')
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

class TenderEntry(models.Model):
	transactionID = models.ForeignKey(Transaction)
	tenderType = models.PositiveSmallIntegerField()
	amount = models.DecimalField(max_digits=10, decimal_places=2)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

class TransactionEntry(models.Model):
	transactionID = models.ForeignKey(Transaction)
	productID = models.ForeignKey(Product)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	quantity = models.IntegerField()
