use agg
db.products.aggregate([
    {$group:
     {
	 _id: {'manufacturer':"$manufacturer"},
	 num_products:{$sum:1}
     }
    }
])


