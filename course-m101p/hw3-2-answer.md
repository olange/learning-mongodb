# Homework 3.2

Making your blog accept posts [Description complète](https://education.10gen.com/courses/10gen/M101P/2014_February/courseware/Week_3_Schema_Design/529e0064e2d42347509fb3a6/)

## Pièces jointes

* [hw3-2-blogPostDAO.py](hw3-2-blogPostDAO.py) script modifié
* [hw3-2and3-3.cb3a025ac81c.zip](hw3-2and3-3.cb3a025ac81c.zip) application blog fournie par MongoDB

## Problème

In this homework you will be enhancing the blog project to insert entries into the posts collection. After this, the blog will work. It will allow you to add blog posts with a title, body and tags and have it be added to the posts collection properly.

We have provided the code that creates users and allows you to login (the assignment from last week). To get started, please download [hw3-2and3-3.cb3a025ac81c.zip](hw3-2and3-3.cb3a025ac81c.zip) from the Download Handout link and unpack. You will be using these file for this homework and the [HW 3.3](hw3-3-answer.md).

The areas where you need to add code are marked with XXX. You need only touch the [BlogPostDAO.py](hw3-2-blogPostDAO.py) file. There are three locations for you to add code for this problem. Scan that file for `XXX` to see where to work.

## Résolution

Ajouter un nouveau post:

    class BlogPostDAO:
        …

        def insert_entry( self, title, post, tags_array, author):
            …
            try:
                # XXX HW 3.2 Work Here to insert the post
                self.posts.insert( post, j=True)
                …

Retourner 10 derniers posts:

        def get_posts( self, num_posts):
            # XXX HW 3.2 Work here to get the posts
            cursor = self.posts.find().sort([( "date", DESCENDING)]).limit( num_posts)
            …

Retourner un post selon son permalink:

        def get_post_by_permalink( self, permalink):
            # XXX Work here to retrieve the specified post
            post = self.posts.find_one( { "permalink": permalink })
            …

## Réponse

    (venv)~/Sources/learning-mongodb/course-m101p/hw3-2and3-3 $ python validate.py 
    Welcome to the HW 3.2 and HW 3.3 validation tester
    Trying to create a test user  MHHqhyv
    Found the test user  MHHqhyv  in the users collection
    User creation successful. 
    Trying to login for test user  MHHqhyv
    User login successful.
    Trying to submit a post with title  zxCJIVOmrlwzSJPkcpOVOdKknvIzRW
    Submission of single post successful
    Trying to submit a post with title  RUxxZqlZzumJLHumcfOhQquhpdGfVb
    Submission of second post successful
    Trying to grab the blog home page at url  http://localhost:8082/
    Block index looks good.
    Found blog post in posts collection
    Tests Passed for HW 3.2. Your HW 3.2 validation code is 89jklfsjrlk209jfks2j2ek
    Trying to submit a blog comment for post with title zxCJIVOmrlwzSJPkcpOVOdK
    Can't add blog comments (so HW 3.3 not yet complete)

    --> 89jklfsjrlk209jfks2j2ek

## Préparation

Ajouter `reloader=True` à `bottle.run` dans `blog.py` (voir [Bottle Tutorial › Development › Autoreloading](http://bottlepy.org/docs/dev/tutorial.html#auto-reloading)):

    …
    bottle.debug( True)
    bottle.run( host='localhost', port=8082, reloader=True)

Démarrer le serveur:

    (venv) course-m101p/hw3-2and3-3 $ python blog.py
    Bottle v0.12.3 server starting up (using WSGIRefServer())...
    Listening on http://localhost:8082/
    Hit Ctrl-C to quit.
