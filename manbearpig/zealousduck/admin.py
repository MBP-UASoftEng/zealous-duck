from django.contrib import admin

# Register your models here.

from .models import Product
from .models import Employee
from .models import Transaction
from .models import TransactionEntry
from .models import TenderEntry

class QuantityListFilter(admin.SimpleListFilter):
	title = ('In Stock')
	parameter_name = 'instock'
	
	def lookups(self, request, model_admin):
		return (
			('yes', ('Yes')),
			('no', ('No')),
		)
	
	def queryset(self, request, queryset):
		if self.value() == 'yes':
			return queryset.filter(quantity__gte=1)
		if self.value() == 'no':
			return queryset.filter(quantity__lte=0)			

class ProductAdmin(admin.ModelAdmin):
	list_display = ('description', 'quantity', 'price', 'itemID', 'lookupcode', 'itemType')
	list_filter = ['active', 'itemType', QuantityListFilter]
	search_fields = ['description', 'extendedDescription', 'itemID', 'lookupcode']

admin.site.register(Product, ProductAdmin)
admin.site.register(Employee)
admin.site.register(Transaction)
admin.site.register(TransactionEntry)
admin.site.register(TenderEntry)
