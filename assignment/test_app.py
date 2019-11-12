from app import app
from flask import json

def test_getCustomerCharge():
    response = app.test_client().post(
        '/getCustomerCharge',
        data=json.dumps({"noOfBooks":10,	"noOfDays":3}),
        content_type='application/json',
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert data['Total Price'] == "30 Rs"