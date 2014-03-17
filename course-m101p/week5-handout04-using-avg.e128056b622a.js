use agg
db.products.aggregate([
    { $group: {
    	_id: { "category":"$category"},
        avg_price:{ $avg: "$price"}
    }}
])


