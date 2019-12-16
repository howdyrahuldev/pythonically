from flask import Flask, jsonify, request

app = Flask("xyz")



def calculate_price(category, no_of_days, no_of_books):
    #print(category,no_of_days,no_of_books)
    book_price_days = {"regular": [1.5,1,2], "fiction": [3,0,0], "novels": [1.5,2,4.5]}

    book_chosen = book_price_days[category]
    price = book_chosen[2]*book_chosen[1]*no_of_books
    if no_of_days > book_price_days[category][1]:
        price = price + (no_of_days-book_chosen[1])*book_chosen[0]* no_of_books

    return price


@app.route("/get-customer-charge", methods=["GET"])
def get_customer_charge():
    mydata = request.get_json()
    total_price = 0
    for item in mydata["books"]:
        total_price += calculate_price(item["typeOfBooks"], item["noOfDays"], item["noOfBooks"])
    return jsonify({"Total Price":f'{total_price} Rs'})


app.run(port=5050)