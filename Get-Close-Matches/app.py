"""
This project fetches the meaning of the input keyword as POST request from the given JSON file

Used get_close_matches function from difflib library to get the nearest words if the exact word can not be found.
Flask API created
"""

from flask import Flask, jsonify, request
from difflib import get_close_matches
from collections import OrderedDict
import json

json_app = Flask(__name__)
json_data = json.load(open('data.json'))


@json_app.route('/getmeaning', methods=['POST'])
def get_meaning():
    local_data = request.get_json()  # Fetching the data as dictionary format from the POST request
    if "word given" in local_data.keys():  # "word given" should be the key in the json payload
        try:  # this block checks if the exact match found or not
            try:
                meaning = json_data[local_data["word given"]]
            except KeyError:
                try:
                    meaning = json_data[local_data["word given"].lower()]
                except KeyError:
                    meaning = json_data[local_data["word given"].capitalize()]
            return jsonify({"meaning": meaning})
        except KeyError:

            matches = OrderedDict()
            matches["##message##"] = ["as your word could not be found, here are some matches:"]
            for match in get_close_matches(local_data["word given"].lower(), json_data.keys()):
                matches[match] = json_data[match]
            if len(matches) > 1:
                print(matches)
                return jsonify(matches)
            else:
                return jsonify({"message": "word not found"})
    else:
        return jsonify({"message": "key passed should be - word given"})


json_app.run(port=4989)
