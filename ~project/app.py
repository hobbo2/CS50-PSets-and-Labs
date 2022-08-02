
from flask import Flask, render_template, flash, request
from pytube import YouTube

app = Flask(__name__)
app.secret_key = 'super secret key'

# remove cache
@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route('/', methods = ['GET','POST'])
def home():
    if request.method == 'POST':
        try:
            url = str(request.form.get('url'))
            yt = YouTube(url)
            title = yt.title
            thumbnail = yt.thumbnail_url
            minutes = int(yt.length/60)
            seconds = yt.length - minutes*60
            return render_template('download.html',title = title, minutes = minutes, seconds = seconds, thumbnail = thumbnail)
        except:
            return render_template('index.html')
    else:
        flash("INVALID YOUTUBE URL...")
        return render_template('index.html')


@app.route('/download',methods= ['POST', 'GET'])
def meta_data():
    if request.method == 'POST':
        try:
            url = str(request.form.get('url'))
            yt = YouTube(url)
            yd = yt.streams.get_highest_resolution()  
            yd.download()
            title = yt.title
            thumbnail = yt.thumbnail_url
            minutes = int(yt.length/60)
            seconds = yt.length - minutes*60
            # click download to download
            flash('Downloading....')
            return render_template('download.html',title = title, minutes = minutes, seconds = seconds, thumbnail = thumbnail)
        except: RuntimeError
        return render_template('index.html')


if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.run()