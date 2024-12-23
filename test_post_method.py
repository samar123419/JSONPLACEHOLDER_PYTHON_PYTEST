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

def test_post_task(base_url):
    payload =  {
        "userId": 1,
        "title": "delectus aut autem", 
        "completed": "False"
        }
    response = requests.post(base_url, json=payload) 
    data = response.json()
    print(type(data))
    try:
        assert "userId" in data.keys()
        assert "id" in data.keys()
        assert "title" in data.keys()
        assert "completed" in data.keys()

        assert response.status_code == 201
        save_result_in_csv_file( response.request.method, base_url,  response.status_code,"PASS")
    
    except AssertionError:
        save_result_in_csv_file( response.request.method, base_url,  response.status_code,"FALID")

def test_post_status_code(base_url, payload):
    response = requests.post(base_url, json=payload[0]) 
    # data = response.json()
    # print(data)
    try:
        assert response.status_code in [200, 201]
        save_result_in_csv_file( response.request.method, base_url,  response.status_code,"PASS")
    except AssertionError:
        save_result_in_csv_file( response.request.method, base_url,  response.status_code,"FALID")

def test_post_task_from_json_file(base_url,payload):
    response = requests.post(base_url, json=payload[0]) 
    # data = response.json()
    # print(data)
    try:
        assert response.status_code == 201
        save_result_in_csv_file( response.request.method, base_url,  response.status_code,"PASS")
    
    except AssertionError:
        save_result_in_csv_file( response.request.method, base_url,  response.status_code,"FALID")

def test_response_format(base_url, payload):
    response = requests.post(base_url, json=payload[0])     
    data = response.json()
    print(type(data))
    try:
        #  assert isinstance(data, dict)
        assert response.status_code == 201
    except AssertionError:
        save_result_in_csv_file( response.request.method, base_url,  response.status_code,"FALID")

def test_check_amount_of_posts(base_url, payload):
    res1 = requests.get(base_url)

    before_delete_post = res1.json()
    
    response = requests.post(base_url, json=payload[0])

    res2 = requests.get(base_url)
    data_after =res2.json() 
    # print(data_after)
    
    try:
        assert len(data_after) < len(before_delete_post)
        save_result_in_csv_file( response.request.method, base_url,  response.status_code,"PASS")
    
    except AssertionError:
        save_result_in_csv_file( response.request.method, base_url,  response.status_code,"FALID")

def test_id_post(base_url, payload):

    response = requests.post(base_url, json=payload[0]) 
    data = response.json()
    # print(data)
    try:
        assert "id" in data.keys()
        save_result_in_csv_file( response.request.method, base_url,  response.status_code,"PASS")
    
    except AssertionError:
        save_result_in_csv_file( response.request.method, base_url,  response.status_code,"FALID")



