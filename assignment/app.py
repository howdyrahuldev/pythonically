from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/getCustomerCharge", methods=["POST"])
def getCustomerCharge():
    mydata = request.get_json()
    return jsonify({"Total Price":f'{mydata["noOfBooks"]*mydata["noOfDays"]} Rs'})

app.run(port=5050)