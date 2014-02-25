# Homework 2.2

[Description complète](https://education.10gen.com/courses/10gen/M101P/2014_February/courseware/Week_2_CRUD/52939732e2d423246e7c43e9/)

## Pièces jointes

* [hw2-2-remove.py](hw2-2-remove.py)

## Problème

Write a program in the language of your choice that will remove the grade of type "homework" with the lowest score for each student from the dataset that you imported in HW 2.1. Since each document is one grade, it should remove one document per student.

Provide the identity of the student with the highest average in the class, using given query. The answer will appear in the _id field of the resulting document.

## Résolution

Suppression des documents (voir [hw2-2-remove.py](hw2-2-remove.py)):

    (venv) course-m101p $ python hw2-2-remove.py 
    Removing {u'student_id': 0, u'_id': ObjectId('50906d7fa3c412bb040eb57a'), u'type': u'homework', u'score': 63.98402553675503}
    Removing {u'student_id': 1, u'_id': ObjectId('50906d7fa3c412bb040eb57e'), u'type': u'homework', u'score': 44.31667452616328}
    Removing {u'student_id': 2, u'_id': ObjectId('50906d7fa3c412bb040eb582'), u'type': u'homework', u'score': 97.75889721343528}
    Removing {u'student_id': 3, u'_id': ObjectId('50906d7fa3c412bb040eb586'), u'type': u'homework', u'score': 92.71871597581605}
    ...

Nombre de documents après suppression:

    (venv) course-m101p $ mongo students
    MongoDB shell version: 2.4.9
    connecting to: students

    > db.grades.count()
    600

Student who holds the 101st best grade across all grades:

    > db.grades.find().sort({'score':-1}).skip(100).limit(1)
    { "_id" : ObjectId("50906d7fa3c412bb040eb709"), "student_id" : 100, "type" : "homework", "score" : 88.50425479139126 }

Top five students sorted by student_id, score:

    > db.grades.find({},{'student_id':1, 'type':1, 'score':1, '_id':0}).sort({'student_id':1, 'score':1, }).limit(5)
    { "student_id" : 0, "type" : "quiz", "score" : 31.95004496742112 }
    { "student_id" : 0, "type" : "exam", "score" : 54.6535436362647 }
    { "student_id" : 0, "type" : "homework", "score" : 63.98402553675503 }
    { "student_id" : 1, "type" : "homework", "score" : 44.31667452616328 }
    { "student_id" : 1, "type" : "exam", "score" : 74.20010837299897 }

## Réponse

Provide the identity of the student with the highest average in the class with following query that uses the aggregation framework. The answer will appear in the _id field of the resulting document.

    > db.grades.aggregate({'$group':{'_id':'$student_id', 'average':{$avg:'$score'}}}, {'$sort':{'average':-1}}, {'$limit':1})
    {"result" : [ {"_id" : 54, "average" : 96.19488173037341 } ], "ok" : 1 }

    --> 54
