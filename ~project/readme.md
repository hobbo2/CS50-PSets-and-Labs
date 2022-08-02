# Youtube Downloader

#### Video Demo: <URL https://youtu.be/Srb1oSUY3gU>

#### Description:

Get any URL from Youtube and download the video for offline use.

The project was written using python, flask and html.

# app.py:

app.py is the backend of the application. It uses the flask library to import Flask, flash, redirect, render_template, request, and a module YouTube from pytube library to import  YouTube.
pytube is used get metadata, URLs from Youtube videos and ultimately download the videos.
Flask also allows the navigation between webpages using GET and POST.In python I imported a library called pytube which gives access to a whole bunch of tools for youtube.
Varaibles were created using pytubes library which could then be displayed on the HTML side.

I had ideas to add an sql database to capture user data or to capture records of videos downloaded but I ran out of time. I repeatedly tried to connect my own Mysql database but I was clearly making a mistake or watching the wrong tutorials as I consistently got errors before I decided to move on without a logon or register page.

I initially started my page on github pages but it turned out to be easier just to run it locally on my own pc due to powercuts in my area which meant I could not access github.

# HTML:

templates folder contains the HTML code for the webpages.
This includes index.html which is the home page, and includes download.html which is where the magic happens.
download.html shows us the videos name and length before allowing the user to download said video from youtube.
I started off using bootstrap for the html but ultimately  reverted to standard W3Schools colour scheme and format as I found it easier to read their documentation and to follow their instructions.
Instead of setting a separate CSS page I decided to contain the CSS inside the HTML pages as it was more conveniant for me to revert to to change classes and update classes.
Variables created in the flask app were carried to be displayed on the html side.
Returning the thumbail of the youtuve video took ages as initially I misread the documentation due to rushing, this lead me down another rabbit hole until I returned to reread the documentation (insert facepalm) and wrote one line of code to solve that problem.

# WHY:

The use of the pirate emblem is a small tribute to piratebay and democratisation of education and information.This is designed for students in areas with limited network connection available or suffer from outages
and who may not be able to afford to pay youtube premium. Users can then save the videos for later use.
I personally used it to get educational videos as often I would find myself mid python tutorial when a network
outage hits rendering Youtube useless for a few hours.
