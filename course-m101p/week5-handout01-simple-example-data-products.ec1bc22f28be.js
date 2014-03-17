
use agg
db.products.drop()

db.products.insert({'name':'iPad 16GB Wifi', 'manufacturer':"Apple", 
		    'category':'Tablets', 
		    'price':499.00})
db.products.insert({'name':'iPad 32GB Wifi', 'category':'Tablets', 
		    'manufacturer':"Apple", 
		    'price':599.00})
db.products.insert({'name':'iPad 64GB Wifi', 'category':'Tablets', 
		    'manufacturer':"Apple", 
		    'price':699.00})
db.products.insert({'name':'Galaxy S3', 'category':'Cell Phones', 
		    'manufacturer':'Samsung',
		    'price':563.99})
db.products.insert({'name':'Galaxy Tab 10', 'category':'Tablets', 
		    'manufacturer':'Samsung',
		    'price':450.99})
db.products.insert({'name':'Vaio', 'category':'Laptops', 
		    'manufacturer':"Sony", 
		    'price':499.00})
db.products.insert({'name':'Macbook Air 13inch', 'category':'Laptops', 
		    'manufacturer':"Apple", 
		    'price':499.00})
db.products.insert({'name':'Nexus 7', 'category':'Tablets', 
		    'manufacturer':"Google", 
		    'price':199.00})
db.products.insert({'name':'Kindle Paper White', 'category':'Tablets', 
		    'manufacturer':"Amazon", 
		    'price':129.00})
db.products.insert({'name':'Kindle Fire', 'category':'Tablets', 
		    'manufacturer':"Amazon", 
		    'price':199.00})
