from django.contrib import admin

# Register your models here.

from .models import Product
from .models import Employee
from .models import Transaction
from .models import TransactionEntry
from .models import TenderEntry

class ProductAdmin(admin.ModelAdmin):
	list_display = ('description', 'quantity', 'price', 'itemID', 
'lookupcode', 'itemType')
	list_filter = ['active', 'itemType']
	search_fields = ['description', 'extendedDescription', 'itemID', 'lookupcode']

admin.site.register(Product, ProductAdmin)
admin.site.register(Employee)
admin.site.register(Transaction)
admin.site.register(TransactionEntry)
admin.site.register(TenderEntry)
