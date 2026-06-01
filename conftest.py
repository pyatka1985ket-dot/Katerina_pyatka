import pytest
from endpoints.create_object import CreatedObject
from endpoints.delete_object import DeleteObject




@pytest.fixture()
def obj_id():
    created_object = CreatedObject()
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }

    created_object.new_object(payload)
    yield created_object.response_json['id']
    delete_object = DeleteObject()
    delete_object.delete_by_id(created_object.response_json['id'])
