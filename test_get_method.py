import requests
import json
import pytest
import csv 
@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com/todos"

@pytest.fixture
def id():
    return "/23"
  

def save_result_in_csv_file(method, endpoint, status,result):
    with open('results.csv',mode= 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        if csvfile.tell() == 0:
            writer.writerow(["method", "endpoint","status","result"])
        
        writer.writerow([method,endpoint,status,result])

# CURD, get, post, put, putch, delete

def test_get_status_code(base_url):
    response =  requests.get(base_url)
    # print(response.text)
    try:
        assert response.status_code == 200
        save_result_in_csv_file( response.request.method, base_url,  response.status_code,"PASS")
    except AssertionError:
        save_result_in_csv_file( response.request.method, base_url,  response.status_code,"FALID")

def test_get_response_format(base_url):
    response = requests.request("GET", base_url)
    data = response.json()
    # print(response.text)
    try:
         assert isinstance(data, list)
         print(len(data))
        
    except AssertionError:
        save_result_in_csv_file( response.request.method, base_url,  response.status_code,"FALID")

def test_userId_in_posts(base_url):
    response = requests.request("GET", base_url)
    # print(response.text)
    try:
        data = response.json()
        num = len(data)

        for i in range(num):
            assert "userId" in data[i].keys()

        save_result_in_csv_file( response.request.method, base_url,  response.status_code,"PASS")
    except AssertionError:
        save_result_in_csv_file( response.request.method, base_url,  response.status_code,"FALID")

def test_id_in_posts(base_url):
    response = requests.request("GET", base_url)
    # print(response.text)
    try:
        data = response.json()
        num = len(data)

        for i in range(num):
            assert "id" in data[i].keys()

        save_result_in_csv_file( response.request.method, base_url,  response.status_code,"PASS")
    except AssertionError:
        save_result_in_csv_file( response.request.method, base_url,  response.status_code,"FALID")

def test_title_in_posts(base_url):
    response = requests.request("GET", base_url)
    # print(response.text)
    try:
        data = response.json()
        num = len(data)

        for i in range(num):
            assert "title" in data[i].keys()

        save_result_in_csv_file( response.request.method, base_url,  response.status_code,"PASS")
    except AssertionError:
        save_result_in_csv_file( response.request.method, base_url,  response.status_code,"FALID")

def test_body_in_posts(base_url):
    response = requests.request("GET", base_url)
    # print(response.text)
    try:
        data = response.json()
        num = len(data)

        for i in range(num):
            assert "body" in data[i].keys()

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




