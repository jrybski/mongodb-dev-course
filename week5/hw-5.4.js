use agg

db.zips.aggregate([
    {$project: {_id:0, zip: "$_id", pop: "$pop", city: "$city", first_char: {$substr : ["$city",0,1]}}},
    {$match:   {first_char: {$regex: '^[0-9]{1}$'}}},
    {$group:   {_id: "all", total_pop: {$sum: '$pop'}}}
])
