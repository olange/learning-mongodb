# Homework 3.1

Remove the lowest homework score for each student [Description complète](https://education.10gen.com/courses/10gen/M101P/2014_February/courseware/Week_3_Schema_Design/529dffcae2d42347509fb3a2/)

## Pièces jointes

* [hw3-1-remove.py](hw3-1-remove.py) script réalisé

## Problème

Write a program in the language of your choice that will remove the lowest homework score for each student. Since there is a single document for each student containing an array of scores, you will need to update the scores array and remove the homework. Provide the identify of the student with the highest average in the class, using given query.

## Résolution

Suppression des scores (voir [hw3-1-remove.py](hw3-1-remove.py)):

    (venv) course-m101p $ python hw3-1-remove.py 
    ...
    updated doc 199:
    scores: [{u'score': 82.11742562118049, u'type': u'exam'}, {u'score': 49.61295450928224, u'type': u'quiz'}, {u'score': 28.86823689842918, u'type': u'homework'}, {u'score': 5.861613903793295, u'type': u'homework'}]
    new scores: [{u'score': 82.11742562118049, u'type': u'exam'}, {u'score': 49.61295450928224, u'type': u'quiz'}, {u'score': 28.86823689842918, u'type': u'homework'}]

Nombre de documents après suppression:

    (venv) course-m101p $ mongo school
    > db.students.count() 
    200

Demarcus Audette's record:

    > db.students.find({_id:100}).pretty()
    {
        "_id" : 100,
        "name" : "Demarcus Audette",
        "scores" : [
            {"score" : 47.42608580155614, "type" : "exam"},
            {"score" : 44.83416623719906, "type" : "quiz"},
            {"score" : 39.01726616178844, "type" : "homework"}
        ]
    }

## Réponse

Provide the identify of the student with the highest average in the class with following query that uses the aggregation framework. The answer will appear in the _id field of the resulting document.

    > db.students.aggregate({'$unwind':'$scores'},{'$group':{'_id':'$_id', 'average':{$avg:'$scores.score'}}}, {'$sort':{'average':-1}}, {'$limit':1})

    { "result" : [ { "_id" : 13, "average" : 91.98315917172745 } ], "ok" : 1 }

    --> 13

## Préparation

    (venv) course-m101p $ mongoimport -d school -c students < hw3-1-students.e7ed0a289cbe.json 
    connected to: 127.0.0.1
    Tue Feb 25 16:02:10.702 check 9 200
    Tue Feb 25 16:02:10.702 imported 200 objects
