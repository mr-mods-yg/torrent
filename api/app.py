from flask import Flask, render_template
from torrent import search
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route("/<name>")
def torrent(name):
    data = search(name)
    data = data['torrents']
    return render_template('streamer.html',data=data)

if __name__ == '__main__':
    app.run()
