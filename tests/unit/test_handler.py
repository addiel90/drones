import os
import sys
import json
import requests
from requests.structures import CaseInsensitiveDict

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(THIS_DIR, "../..", 'src'))

def test_get_drone_GET():
    _url="http://127.0.0.1:5000/drones/f82383d8-f17f-11ec-98dc-fbac941fa328"
    response = requests.get(_url)
    assert response.status_code == 200   
    assert response.ok is True
    
def test_get_drone_BadRequest_GET():
    _url="http://127.0.0.1:5000/drones/f82383d8-f17f-11ec-9dc-fbac941fa328"
    response = requests.get(_url)
    assert response.status_code == 400   
    assert response.ok is False
    
def test_get_battery_capacity_GET():
    _reques_data={"serial_number":"f8238360-f17f-11ec-98d8-d71374c94aea"}
    headers = CaseInsensitiveDict()
    headers["Accept"] = "*/*"
    headers["Content-Type"] = "application/vnd.api+json"
    _url="http://127.0.0.1:5000/drones/battery"
    response = requests.get(_url, data=json.dumps(_reques_data), headers=headers)
    assert response.status_code == 200   
    assert response.ok is True
    assert "battery_capacity" in response.text
    
def test_get_battery_capacity_BadRequest_GET():
    _reques_data={"serial_number":"f8238360-f17f-11c-98d8-d71374c94aea"}
    headers = CaseInsensitiveDict()
    headers["Accept"] = "*/*"
    headers["Content-Type"] = "application/vnd.api+json"
    _url="http://127.0.0.1:5000/drones/battery"
    response = requests.get(_url, data=json.dumps(_reques_data), headers=headers)
    assert response.status_code == 400   
    assert response.ok is False
    assert "Drone not found" in response.text 