# send-memes-pls

This project allows uploading images to a server and sending them to two possible destinations:

* a simple window that runs in your desktop;
* an RGB led matrix!

# Components:

The application has two components:

* The server:
  * app.py: a Flask server that receives images, or URLs pointing to images, and sends them to the client, 
* The client(s): 
  * window.py: runs a window that listens to the image server using the WebSocker protocol, and displays new images when they are set.
  * pyled-client.py: runs a program that sends the images to a led matrix (tested with a Raspberry Pi since it can both run the client and control the matrix).
  

# Running locally

You can test the application locally with the simple window client by following these steps

* Install `requirements.txt` and `client-requirements.txt`
* Run run_local.sh
* Go to `localhost:5000` on your browser
* (Optional) If you want to open that port to external connections, to show the app to someone, you can use a tool like [ngrok](https://ngrok.com/)

# Deploying the server to Heroku

Install Heroku: https://devcenter.heroku.com/articles/heroku-cli

Follow these steps to deploy the application to Heroku:

* heroku login
* heroku create <choose name>
* heroku git:remote -a <chosen name>
* heroku config:set FLASK_SECRET_KEY=<anything> (it's only used to flash error messages to the user)
* git push heroku master
* set the following environment variables with `export`:
  * HOST: the URL of the Heroku server; 
  * PORT: the port used by Heroku (443)
* Run window.py locally
* Open your browser, go to you app's URL, and send memes


# Connecting to a led matrix 

Sending images to a led matrix was tested with a Raspberry Pi.

First, read the information on this repository: https://github.com/hzeller/rpi-rgb-led-matrix

You must be able to run the [sample programs provided by them](https://github.com/hzeller/rpi-rgb-led-matrix/tree/master/examples-api-use).

Afterwards, install the [Python bindings](https://github.com/hzeller/rpi-rgb-led-matrix/tree/master/bindings/python)

Finally, it should just be a matter of running `pyled-client.py`, and the images should show up in the matrix!
