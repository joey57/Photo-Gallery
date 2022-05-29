# Photo-Gallery
Gall-Art

## Description
Gall-art is a photo gallery to display beautiful pictures and art. Users can view the photos on the landing page. The photos are uploaded using django admin. The user can search for different categories of art or pictures. Users can see photos based on locations.

## User Stories 
- Users can view different photos
- Users can search photos based on different categories.
- Users can search photos based on different locations.
- Admin can upload images from django admin dashboard

## Live site

## Technologies used
* Django Framework - used to create the application. 
* Heroku - used to deploy the application. 

## Set up and installation
#### Clone the Repo
####  Activate virtual environment
Activate virtual environment using python as default handler
    `virtualenv -p /usr/bin/python virtual && source virtual/bin/activate`
For windows users use this to activa your environment
   ` source virtual/Scripts/activate`    
####  Install dependencies
Install dependancies that will create an environment for the app to run `pip install -r requirements.txt`
####  Create the Database
    - psql
    - CREATE DATABASE <DBNAME>;
####  .env file
Create .env file and add the following filling where appropriate:

    SECRET_KEY = '<Secret_key>'
    DBNAME = '<DBNAME>'
    USER = '<Username>'
    PASSWORD = '<password>'
    DEBUG = True
#### Run initial Migration
    python3.6 manage.py makemigrations gallery
    python3.6 manage.py migrate
#### Run the app
    python3.6 manage.py runserver
    Open terminal on localhost:8000

## Known Bugs
No known bugs so far.

## Contact Information
If you have any questions feel free to contact me.

## License
* MIT LICENSE
* Copyright (c) 2022 Joyce Njoroge

