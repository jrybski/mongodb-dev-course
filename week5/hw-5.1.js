use agg

db.posts.aggregate([
    {$unwind: "$comments"},
    {$group: {_id: "$comments.author", total_comments: {$sum: 1}}},
    {$sort: {total_comments: -1}},
    {$limit: 1}
])
