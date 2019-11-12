from app import app
from flask import json

def test_getCustomerCharge1():
    response = app.test_client().post(
        '/getCustomerCharge',
        data=json.dumps({   "1":{"typeOfBooks":"fiction","noOfBooks":1,"noOfDays":10},
	                        "2":{"typeOfBooks":"regular","noOfBooks":3,"noOfDays":10},
	                        "3":{"typeOfBooks":"novels","noOfBooks":1,"noOfDays":30}}),
        content_type='application/json',
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert data['Total Price'] == "117.0 Rs"

def test_getCustomerCharge2():
    response = app.test_client().post(
        '/getCustomerCharge',
        data=json.dumps({   "1":{"typeOfBooks":"fiction","noOfBooks":1,"noOfDays":10},
	                        "2":{"typeOfBooks":"regular","noOfBooks":1,"noOfDays":1},
	                        "3":{"typeOfBooks":"novels","noOfBooks":1,"noOfDays":30}}),
        content_type='application/json',
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert data['Total Price'] == "77.0 Rs"


def test_getCustomerCharge3():
    response = app.test_client().post(
        '/getCustomerCharge',
        data=json.dumps({   "1":{"typeOfBooks":"fiction","noOfBooks":1,"noOfDays":10},
	                        "2":{"typeOfBooks":"regular","noOfBooks":1,"noOfDays":1},
	                        "3":{"typeOfBooks":"novels","noOfBooks":1,"noOfDays":2}}),
        content_type='application/json',
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert data['Total Price'] == "36.5 Rs"