from flask import Flask, jsonify
import requests
import feedparser
from flask_cors import CORS
from bs4 import BeautifulSoup

app = Flask(__name__)
CORS(app)

@app.route("/api/medium-posts")
def get_medium_posts():
    feed_url = "https://medium.com/feed/@annie.chakraborty"  # replace with yours
    feed = feedparser.parse(feed_url)

    posts = []
    for entry in feed.entries:
        posts.append({
            "title": entry.title,
            "link": entry.link,
            "published": entry.published,
            "summary": entry.summary
        })
    return jsonify(posts)

@app.route('/api/profile')
def get_linkedin_data():
    url = "enter url"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html')
    print(soup)
    return {
        "data": str(soup)
    }

@app.route('/api/contact')
def contact_me():
    print()

if __name__ == "__main__":
    app.run(debug=True)

