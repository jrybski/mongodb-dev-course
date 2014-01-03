use agg

db.zips.aggregate([
    {$match: {state: {$in: ["CA", "NY"]}}},
    {$group: {_id : {city: "$city", state: "$state"}, city_pop: {$sum: "$pop"}}},
    {$match: {city_pop: {$gt: 25000}}},
    {$group: {_id: "$city", avg_pop: {$avg: "$city_pop"}}}
])
