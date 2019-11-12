from app import app
from flask import json

def test_getCustomerCharge():
    response = app.test_client().post(
        '/getCustomerCharge',
        data=json.dumps({   "1":{"typeOfBooks":"fiction","noOfBooks":1,"noOfDays":10},
	                        "2":{"typeOfBooks":"regular","noOfBooks":3,"noOfDays":10},
	                        "3":{"typeOfBooks":"novels","noOfBooks":1,"noOfDays":30}}),
        content_type='application/json',
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert data['Total Price'] == "120.0 Rs"