from flask import Flask, jsonify, request
import requests
import xmltodict

app = Flask(__name__)
apiurl = "http://www.parkrun.org.uk/wp-content/themes/parkrun/xml/geo.xml"
data = requests.get(apiurl);

@app.route('/events', methods=['GET'])
def get_events():
    json = xmltodict.parse(data.text, attr_prefix="")    
    return jsonify(events=json['geo']['e'], meta={"status": "ok"})

@app.route('/regions', methods=['GET'])
def get_regions():
    json = xmltodict.parse(data.text, attr_prefix="")    
    return jsonify(regions=json['geo']['r'], meta={"status": "ok"})

app.run()
