# send-memes-pls

Fun little project - have a window permanently open that people can send images to.

# Components:

The application has two components:

* app.py: a Flask server that receives images, or URLs pointing to images, and sends them to the client, 
* window.py: runs a window that listens to the image server using the WebSocker protocol, and displays new images when they are set.

# Running locally

* Install `requirements.txt` and `client-requirements.txt`
* Run run_local.sh
* Go to `localhost:5000` on your browser
* (Optional) If you want to open that port to external connections, to show the app to someone, you can use a tool like [ngrok](https://ngrok.com/)

# Deploying to Heroku

Follow these steps to deploy the application to Heroku:

* heroku login
* heroku create <choose name>
* heroku git:remote -a <chosen name>
* heroku config:set FLASK_SECRET_KEY=<anything> (it's only used to flash error messages to the user)
* git push heroku master
* set the following environment variables:
  * HOST: the URL of the Heroku server; 
  * PORT: the port used by Heroku (443)
* Run window.py locally
* Open your browser, go to you app's URL, and send memes