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

def test_get_all_tasks(base_url):
    response = requests.request("GET", base_url)
    # print(response.text)
    try:
        data = response.json()
        num = data[-1]["id"]

        for i in range(num):
            assert "userId" in data[i].keys()
            assert "id" in data[i].keys()
            assert "title" in data[i].keys()
            assert "completed" in data[i].keys()

        assert response.status_code == 200

        save_result_in_csv_file( response.request.method, base_url,  response.status_code,"PASS")
    except AssertionError:
        save_result_in_csv_file( response.request.method, base_url,  response.status_code,"FALID")

def test_get_one_task(base_url, id):
    response = requests.request("GET", base_url + id)
    
    data = response.json()
    # print(data)
    try:
        assert "userId" in data.keys()
        assert "id" in data.keys()
        assert "title" in data.keys()
        assert "completed" in data.keys()

        assert response.status_code == 200

        save_result_in_csv_file( response.request.method, base_url + id,  response.status_code,"PASS")
    except AssertionError:
        save_result_in_csv_file( response.request.method, base_url + id,  response.status_code,"FALID")

def test_put_task(base_url, id):
    payload =  {
        "userId": 1,
        "title": "delectus aut autem", 
        "completed": "False"
        }
    response = requests.put(base_url + id, json=payload) 

    data = response.json()
    try:
        assert "userId" in data.keys()
        assert "id" in data.keys()
        assert "title" in data.keys()
        assert "completed" in data.keys()

        assert response.status_code == 200
        save_result_in_csv_file( response.request.method, base_url + id,  response.status_code,"PASS")
    
    except AssertionError:
        save_result_in_csv_file( response.request.method, base_url + id,  response.status_code,"FALID")
    # print(data)

def test_put_task_from_json_file(base_url, id,payload):
    response = requests.put(base_url + id, json=payload[1])
    
    data = response.json()
    # print(data)
    try:
        assert "userId" in data.keys()
        assert "id" in data.keys()
        assert "title" in data.keys()
        assert "completed" in data.keys()

        assert response.status_code == 200
        
        save_result_in_csv_file( response.request.method, base_url + id,  response.status_code,"PASS")
    except AssertionError:
        save_result_in_csv_file( response.request.method, base_url + id,  response.status_code,"FALID")

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

def test_post_task(base_url):
    payload =  {
        "userId": 1,
        "title": "delectus aut autem", 
        "completed": "False"
        }
    # response = requests.put(url_pix + "/create-task", json=payload) 
    response = requests.post(base_url, json=payload) 
    data = response.json()
    # print(data)
    try:
        assert "userId" in data.keys()
        assert "id" in data.keys()
        assert "title" in data.keys()
        assert "completed" in data.keys()

        assert response.status_code == 201
        save_result_in_csv_file( response.request.method, base_url,  response.status_code,"PASS")
    
    except AssertionError:
        save_result_in_csv_file( response.request.method, base_url,  response.status_code,"FALID")

def test_post_task_from_json_file(base_url,payload):
    response = requests.post(base_url, json=payload[0]) 
    data = response.json()
    # print(data)
    try:
        assert "userId" in data.keys()
        assert "id" in data.keys()
        assert "title" in data.keys()
        assert "completed" in data.keys()

        assert response.status_code == 201
        save_result_in_csv_file( response.request.method, base_url,  response.status_code,"PASS")
    
    except AssertionError:
        save_result_in_csv_file( response.request.method, base_url,  response.status_code,"FALID")

def test_delete_task(base_url):
    response = requests.delete(base_url + "/201")
    data = response.json()
    # print(data)
    try:
        assert data == {}
        assert response.status_code == 200
        save_result_in_csv_file( response.request.method, base_url,  response.status_code,"PASS")
    
    except AssertionError:
        save_result_in_csv_file( response.request.method, base_url,  response.status_code,"FALID")

