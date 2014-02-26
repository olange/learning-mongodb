# Homework 3.3

Making your blog accept comments [Description complète](https://education.10gen.com/courses/10gen/M101P/2014_February/courseware/Week_3_Schema_Design/529e0109e2d42347509fb3aa/)

## Pièces jointes

* [hw3-3-blogPostDAO.py](hw3-3-blogPostDAO.py) script modifié
* [hw3-2and3-3.cb3a025ac81c.zip](hw3-2and3-3.cb3a025ac81c.zip) application blog fournie par MongoDB

## Problème

In this homework you will add code to your blog so that it accepts comments. You will be using the same code as you downloaded for [HW 3.2](hw3-2-answer.md).

Once again, the area where you need to work is marked with an `XXX in the [blogPostDAO.py](hw3-3-blogPostDAO.py) file. There are one location. You don't need to figure out how to retrieve comments for this homework because the code you did in 3.2 already pulls the entire blog post (unless you specifically projected to eliminate the comments) and we gave you the code that pulls them out of the JSON document.

This assignment has fairly little code, but it's a little more subtle than the previous assignment because you are going to be manipulating an array within the Mongo document. 

## Résolution

Ajouter un nouveau commentaire à un post:

    class BlogPostDAO:
        …

        def add_comment(self, permalink, name, email, body):
            …
            try:
                # XXX HW 3.3 Work here to add the comment to the designated post
                self.posts.update( { "permalink": permalink}, \
                                   { "$push": { "comments": comment }})
                last_error = db.runCommand({"getLastError":1})
                return last_error['n']          # return the number of documents updated
            …

## Réponse

    (venv) course-m101p/hw3-2and3-3 $ python validate.py 
    Welcome to the HW 3.2 and HW 3.3 validation tester
    …
    Trying to submit a blog comment for post with title ldXXwoAXbAeSPtVHXTWKOhNRBMrOWy
    Successfully added blog comments
    Tests Passed for HW 3.3. Your HW 3.3 validation code is jk1310vn2lkv0j2kf0jkfs

    --> jk1310vn2lkv0j2kf0jkfs

## Préparation

Cf. «Préparation» dans réponse [HW 3.2](hw3-2-answer.md#préparation).