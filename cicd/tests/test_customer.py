import json


def test_customer_created(client, empty_db):
    data = {
        'name': 'Tahreem Arif',
        'address': 'Test street 123',
        'email': 'tahreemarif34@gmail.com',
        'gender': 'female'
    }

    response = client.post(
        '/customers', data=json.dumps(data), mimetype='application/json'
    )
    response_data = json.loads(response.data)

    assert response.status_code == 201
    assert response_data['message'] == "Customer created successfully!!"
    assert response_data['status_code'] == 201
    assert 'customer_id' in response_data



