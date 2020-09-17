# testing_socail
#requirements - python 3.6 >> 3.8
#virtualenv -

#commands to run program-

pip install virtualenv

#create virtualenv 
command - virtualenv -p python3 env

#activate envirement

command -source env/bin/activate (for windows - CALL env/bin/activate.bat)

#install packages

command- pip install -r requirements.txt ( in root directory)

#create database

command- python manage.py makemigrations and python manage.py migrate

#run program

command - python manage.py runserver



# for api documentation open testing.postman.json in postman
