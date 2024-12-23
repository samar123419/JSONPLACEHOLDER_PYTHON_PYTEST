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


def test_status_code(base_url, id, payload):
    response = requests.put(base_url + id, json=payload[1]) 
    try:
        assert response.status_code == 201
        save_result_in_csv_file( response.request.method, base_url,  response.status_code,"PASS")
    except AssertionError:
        save_result_in_csv_file( response.request.method, base_url,  response.status_code,"FALID")

def test_response_format(base_url , id , payload):

    response = requests.put(base_url + id, json=payload[1])     
    data = response.json()
    print(type(data))
    try:
         assert isinstance(data, dict)
    except AssertionError:
        save_result_in_csv_file( response.request.method, base_url,  response.status_code,"FALID")


def test_post_id(base_url, payload, id):
    response = requests.put(base_url + id, json=payload[1]) 
    data = response.json()
    print(data)
    try:
        assert "id" in data.keys()
        save_result_in_csv_file( response.request.method, base_url,  response.status_code,"PASS")
    
    except AssertionError:
        save_result_in_csv_file( response.request.method, base_url,  response.status_code,"FALID")

def test_userID(base_url, payload, id):
    response = requests.put(base_url + id, json=payload[0]) 
    data = response.json()
    try:
        assert "userId" in data.keys()
        save_result_in_csv_file( response.request.method, base_url,  response.status_code,"PASS")
    
    except AssertionError:
        save_result_in_csv_file( response.request.method, base_url,  response.status_code,"FALID")

def test_body(base_url, payload , id):
    # response = requests.put(url_pix + "/create-task", json=payload) 
    response = requests.put(base_url + id, json=payload[0]) 
    data = response.json()
    # print(data)
    try:
        
        assert "body" in data.keys()

        save_result_in_csv_file( response.request.method, base_url,  response.status_code,"PASS")
    
    except AssertionError:
        save_result_in_csv_file( response.request.method, base_url,  response.status_code,"FALID")

def test_title(base_url,payload, id):  
    response = requests.put(base_url + id, json=payload[0]) 
    data = response.json()
    # print(data)
    try:
        
        assert "title" in data.keys()

        save_result_in_csv_file( response.request.method, base_url,  response.status_code,"PASS")
    
    except AssertionError:
        save_result_in_csv_file( response.request.method, base_url,  response.status_code,"FALID")




# def test_put_task(base_url, id,payload):
#     response = requests.put(base_url + id, json=payload[1])
    
#     data = response.json()
#     # print(data)
#     try:
#         assert "userId" in data.keys()
#         assert "id" in data.keys()
#         assert "title" in data.keys()
#         assert "completed" in data.keys()

#         assert response.status_code == 200
        
#         save_result_in_csv_file( response.request.method, base_url + id,  response.status_code,"PASS")
#     except AssertionError:
#         save_result_in_csv_file( response.request.method, base_url + id,  response.status_code,"FALID")
