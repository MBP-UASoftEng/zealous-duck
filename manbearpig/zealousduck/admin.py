from django.contrib import admin

# Register your models here.

from .models import Product
from .models import Employee
from .models import Transaction
from .models import TransactionEntry
from .models import TenderEntry

admin.site.register(Product)
admin.site.register(Employee)
admin.site.register(Transaction)
admin.site.register(TransactionEntry)
admin.site.register(TenderEntry)

