from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash
from flask import Flask
import os

import geocoder
import urllib2
import json

#db = SQLAlchemy()
app = Flask(__name__)
app.secret_key = '12ff9a90818fe6ebe152a67cf052dfd6f09485ed07fa32aec9349cdcc6157642'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/learningflask'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['HEROKU_POSTGRESQL_GOLD_URL']
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'
    uid = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True)
    pwdhash = db.Column(db.String(128))

    def __init__(self, firstname, lastname, email, password):
        self.firstname = firstname.title()
        self.lastname = lastname.title()
        self.email = email.lower()
        self.set_password(password)

    def set_password(self, password):
        self.pwdhash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pwdhash, password)

class Place(object):
    def meters_to_walking_time(self, meters):
        return int(meters / 80)

    def wiki_path(self, slug):
        return urllib2.urlparse.urljoin("http://en.wikipedia.org/wiki", slug.replace(' ', '_'))

    def address_to_latlng(self, address):
        g = geocoder.google(address)
        return (g.lat, g.lng)

    def query(self, address):
        lat, lng = self.address_to_latlng(address)
        print lat, lng

        query_url = 'https://en.wikipedia.org/w/api.php?action=query&list=geosearch&gscoord=' + str(lat) + '|' + str(lng) + '&gsradius=5000&gslimit=10&format=json'
        g = urllib2.urlopen(query_url)
        results = g.read()
        g.close()

        data = json.loads(results)
        print(data)

        places = []
        for place in data['query']['geosearch']:
            name = place['title']
            meters = place['dist']
            lat = place['lat']
            lng = place['lon']
            wiki_url = self.wiki_path(name)
            walking_time = self.meters_to_walking_time(meters)
            d = {
            'name': name,
            'url': wiki_url,
            'time': walking_time,
            'lat': lat,
            'lng': lng,
            }
            places.append(d)
        return places
