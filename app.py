from flask import Flask, render_template, url_for, redirect, flash, request, session
import socket, re, logging, sys
import requests as fetch
import geocoder, urllib2, json

app = Flask(__name__)
app.secret_key = 'FYIR'

@app.route("/")
@app.route("/news")
def news():
    return render_template('news.html')

@app.route("/map", methods = ['GET', 'POST'])
def map():
    address = request.args.get('address')
    if address:
        print(address)
    else:
        address = "Beacon"
    my_coordinates = (38.8976763, -77.0365298)
    loc = geocoder.google(address)
    my_coordinates = loc.latlng
    places = query(loc)
    print(places)
    return render_template("map.html", my_coordinates=my_coordinates, places=places)

@app.route("/leaflet_quickstart")
def lq():
    return render_template('leaflet_quickstart.html')

def query(address):
    lat, lng = address.lat, address.lng
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
        wiki_url = wiki_path(name)
        print wiki_url
        d = {
        'name': name,
        'url': wiki_url,
        'lat': lat,
        'lng': lng,
        }
        places.append(d)
    for place in places:
        place['url'] = re.sub('http://en.wikipedia.org/', 'http://en.wikipedia.org/wiki/', place['url'])
    return places

def wiki_path(slug):
    return urllib2.urlparse.urljoin("http://en.wikipedia.org/wiki", slug.replace(' ', '_'))

def geo_loc(address):
    loc = geocoder.google(address)
    return (loc.latlng)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
