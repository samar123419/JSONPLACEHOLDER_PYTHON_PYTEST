import csv
import requests
import json
import pytest

#to print will testing: pytest  .\test_exercise2-postman-pytest.py -k test_put_task -v -s

@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com/todos"

@pytest.fixture
def id():
    return "/1"

@pytest.fixture
def payload():
    with open("test_data.json","r") as file:
        return json.load(file)

def save_result_in_csv_file(method, endpoint, status,result):
    with open('results.csv',mode= 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        if csvfile.tell() == 0:
            writer.writerow(["method", "endpoint","status","result"])
        
        writer.writerow([method,endpoint,status,result])

# CURD, get, post, put, putch, delete


def test_patch_task(base_url, id):
    payload =  {
        "title": "patching the new task"
        }
    response = requests.patch(base_url + id, json=payload) 
    try:
        assert response.status_code == 200
        save_result_in_csv_file( response.request.method, base_url + id,  response.status_code,"PASS")
    
    except AssertionError:
        save_result_in_csv_file( response.request.method, base_url + id,  response.status_code,"FALID")