use agg

db.grades.aggregate([
    {$unwind: "$scores"},
    {$match: {$or: [{"scores.type":"exam"}, {"scores.type": "homework"}] }},
    {$group: {_id: {student: "$student_id", class: "$class_id"}, student_avg: {$avg: "$scores.score"}}},
    {$group: {_id: "$_id.class", class_avg: {$avg: "$student_avg"}}},
    {$sort:  {class_avg: 1}},
    {$project: {_id: 0, class_id: "$_id", class_avg: "$class_avg"}}
])
