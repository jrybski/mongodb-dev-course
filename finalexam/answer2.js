db.messages.aggregate([
    {$unwind:"$headers.To"},
    {$group: { _id:{"sender": "$headers.From", "recipient": "$headers.To"},"num_msg": {$sum: 1}}},
    {$sort: {"num_msg":-1}},
    {$limit: 5}
])
