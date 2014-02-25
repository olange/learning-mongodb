# Homework 2.3

[Description complète](https://education.10gen.com/courses/10gen/M101P/2014_February/courseware/Week_2_CRUD/52939a93e2d423246e7c43f7/)

## Pièces jointes

* [hw2-3-userDAO.py](hw2-3-userDAO.py) script modifié
* [hw2-3.4a405a23b442.zip](hw2-3.4a405a23b442.zip) application blog fournie par MongoDB

## Problème

We have removed two pymongo statements from `userDAO.py` and marked the area where you need to work with XXX. You should not need to touch any other code. The pymongo statements that you are going to add will add a new user upon sign-up and validate a login by retrieving the right user document.

## Résolution

Validation du login:

    class UserDAO:
        ...

        def validate_login(self, username, password):
            ...
            try:
                # XXX HW 2.3 Students Work Here
                user = self.users.find_one( { '_id': username})
            ...

Ajout d'un utilisateur:

        def add_user(self, username, password, email):
            ...
            try:
                # XXX HW 2.3 Students work here
                self.users.insert( user)
            ...

## Réponse

    (venv) course-m101p/hw2-3 $ python validate.py
    Welcome to the HW 2.3 validation tester
    Trying to create a test user  aqOmuEl
    Found the test user  aqOmuEl  in the users collection
    User creation successful. 
    Trying to login for test user  aqOmuEl
    User login successful.
    Validation Code is  jkfds9834j98fnm39njf0920fn2

    --> jkfds9834j98fnm39njf0920fn2
