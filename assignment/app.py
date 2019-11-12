from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/getCustomerCharge", methods=["POST"])
def getCustomerCharge():
    mydata = request.get_json()
    book_price = {"regular":1.5,"fiction":3,"novels":1.5}
    total_price=0
    for item in mydata:
        total_price += mydata[item]["noOfBooks"]*mydata[item]["noOfDays"]*book_price[mydata[item]["typeOfBooks"]]
    return jsonify({"Total Price":f'{total_price} Rs'})


app.run(port=5050)