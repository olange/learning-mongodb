use agg
db.zips.aggregate([
    {$match:
     {
	 state:"NY"
     }
    }
])


