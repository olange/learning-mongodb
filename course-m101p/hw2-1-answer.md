# Homework 2.1

Analyzing a data set [Description complète](https://education.10gen.com/courses/10gen/M101P/2014_February/courseware/Week_2_CRUD/529396dee2d423246e7c43e6/)

## Pièces jointes

* [hw2-1-grades.ef42a2b3e7ff.json](hw2-1-grades.ef42a2b3e7ff.json) fichier JSON avec données

## Problème

Now it’s your turn to analyze the data set. Find all exam scores greater than or equal to 65, and sort those scores from lowest to highest. What is the student_id of the lowest exam score above 65: 115, 22, 48, 67, 87 or 114?

## Résolution

    db.grades.find( { "score": { $gte: 65}}).sort( { "score": 1})
    { "_id" : ObjectId("50906d7fa3c412bb040eb5cf"), "student_id" : 22, "type" : "exam", "score" : 65.02518811936324 }
    { "_id" : ObjectId("50906d7fa3c412bb040eb70a"), "student_id" : 100, "type" : "homework", "score" : 65.29214756759019 }
    { "_id" : ObjectId("50906d7fa3c412bb040eb676"), "student_id" : 63, "type" : "homework", "score" : 65.31038121884853 }
    ...

## Réponse

    22

## Préparation

    (venv) course-m101p $ mongoimport -d students -c grades < grades.ef42a2b3e7ff.js 
    connected to: 127.0.0.1
    Tue Feb 18 15:44:34.158 check 9 800
    Tue Feb 18 15:44:34.158 imported 800 objects

    (venv) course-m101p $ mongo
    MongoDB shell version: 2.4.9

    > use students
    switched to db students

    > db.grades.count()
    800

    > db.grades.aggregate({'$group':{'_id':'$student_id', 'average':{$avg:'$score'}}}, {'$sort':{'average':-1}}, {'$limit':1})
    {
        "result" : [
            {
                "_id" : 164,
                "average" : 89.29771818263372
            }
        ],
        "ok" : 1
    }
