# Creating the django project and app
1. First create a folder
2. Then add virtual enviroment using `py -m venv myvenv`
3. Activate the env
4. install django `pip install django`
5. start the project and start the app `django-admin startproject IA` and `django-admin startapp myapp` 
6. cd into the project directory and run the server, this will create the sqlite database
7. Go to the folder and move project out of the directory to root the reason is we want to run `manage.py` from the root always
8. Now change the python interprretrer


# change the basic settings
1. add the app in the installed apps 'myapp.apps.MyappConfig' settings
2. Create `urls.py` inside the `myapp` folder
3. Create function `home` with `HttpResponse` 
4. add the function path inside the `myapp.urls`
5. include the `myapp.urls` inside the `project.urls`
6. run the migrations
7. run the server

