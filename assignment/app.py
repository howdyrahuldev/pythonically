from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/getCustomerCharge", methods=["POST"])
def getCustomerCharge():
    mydata = request.get_json()
    book_price = {"regular":1.5,"fiction":3,"novels":1.5}
    total_price=0
    for item in mydata:
        if mydata[item]["typeOfBooks"] == "regular":
            if mydata[item]["noOfDays"] == 1:
                total_price += mydata[item]["noOfBooks"]*2
            elif mydata[item]["noOfDays"] >= 2:
                part_price = 1
                total_price += mydata[item]["noOfBooks"] * book_price[
                    mydata[item]["typeOfBooks"]] * (mydata[item]["noOfDays"]-2) + mydata[item]["noOfBooks"]*2*part_price


        elif mydata[item]["typeOfBooks"] == "novels":
            if 0 < mydata[item]["noOfDays"] < 3:
                total_price += mydata[item]["noOfBooks"]*4.5
            elif mydata[item]["noOfDays"] >= 3:
                total_price += mydata[item]["noOfBooks"]*mydata[item]["noOfDays"]*book_price[mydata[item]["typeOfBooks"]]


        else:
            total_price += mydata[item]["noOfBooks"] * mydata[item]["noOfDays"] * book_price[mydata[item]["typeOfBooks"]]

    return jsonify({"Total Price":f'{total_price} Rs'})


app.run(port=5050)