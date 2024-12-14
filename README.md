Setup Instructions:

1. create a git repository on your github.
2. clone into the empty git repository on your pc. (git clone "your repository's link")
3. create .gitignore file and add names of files you don't want git to track.
4. create a python virtual environment for your project. (python3 -m venv "your_env_name")
5. activate your virtual environment. (source "your_env_name"/bin/activate)
6. install Django in your virtual environment. (pip install django)
7. create a Django project. (django-admin startproject "project_name")
8. create a Django app. (python manage.py startapp "app_name")
9. register app in settings.py file.
10. add all untracked files to git, commit changes and push your repository back to github. (git add, git commit, git push)

