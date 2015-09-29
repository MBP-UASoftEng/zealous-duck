csv_file="/home/tplacek/GNC-Similar-Data-Reduced.csv"
dhome="/home/tplacek/zealous-duck/manbearpig"

import sys,os
sys.path.append(dhome)
os.environ['DJANGO_SETTINGS_MODULE'] = 'manbearpig.settings'

from zealousduck.models import Product

import csv
dataReader = csv.reader(open(csv_file), delimiter=',', quotechar='"')

for row in dataReader:
	if row[0] != 'BinLocation':
		p = Product()
		p.itemID=row[18]
		print row[18]
		p.description=row[8] 
		p.lookupcode=row[19]
		p.price=row[23]
		p.itemType=row[32]
		p.cost=row[33]
		p.quantity=row[34]
		p.reorderPoint=row[35]
		p.restockLevel=row[36]
		p.parentID=row[41]
		p.extendedDescription=row[48]
		p.active= not row[70]
		p.active= not p.active
		p.msrp=row[73]
		p.dateCreated=row[74]
		p.save()
