# Youtube Downloader

#### Video Demo: <URL https://youtu.be/Srb1oSUY3gU>

#### Description:

Get any URL from Youtube and download the video for offline use.

The project was written using python, flask and html.

## app.py:

app.py is the backend of the application. It uses the flask library and a module YouTube from pytube library to get metadata, URLs from Youtube videos and ultimately download the videos. Flask also allows the navigation between webpages using GET and POST.In python I imported a library called pytube which gives access to a whole bunch of tools for youtube.
I had ideas to add an sql database to capture user data or to capture records of videos downloaded but I ran out of time.

## HTML:

templates folder contains the HTML code for the webpages.
This includes index.html which is the home page, and includes download.html which is where the magic happens.
download.html shows us the videos name and length before allowing the user to download said video from youtube.

## WHY:

The use of the pirate emblem is a small tribute to piratebay and democratisation of education and information.This is designed for students in areas with limited network connection available or suffer from outages
and who may not be able to afford to pay youtube premium. Users can then save the videos for later use.
I personally used it to get educational videos as often I would find myself mid python tutorial when a network
outage hits rendering Youtube useless for a few hours.
