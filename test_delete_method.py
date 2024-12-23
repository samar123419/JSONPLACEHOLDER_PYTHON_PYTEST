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
    return "/15"

def save_result_in_csv_file(method, endpoint, status,result):
    with open('results.csv',mode= 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        if csvfile.tell() == 0:
            writer.writerow(["method", "endpoint","status","result"])
        
        writer.writerow([method,endpoint,status,result])

# CURD, get, post, put, putch, delete


def test_status_code(base_url, id):
    response = requests.delete(base_url + id)
    try:
        assert response.status_code == 200
        save_result_in_csv_file( response.request.method, base_url,  response.status_code,"PASS")
    
    except AssertionError:
        save_result_in_csv_file( response.request.method, base_url,  response.status_code,"FALID")

def test_check_amount_of_posts(base_url,id):
    res1 = requests.get(base_url)

    before_delete_post = res1.json()
    
    response = requests.delete(base_url+id)

    res2 = requests.get(base_url)
    data_after =res2.json() 
    # print(data_after)
    
    try:
        assert len(data_after) < len(before_delete_post)
        # assert response.status_code == 200
        save_result_in_csv_file( response.request.method, base_url,  response.status_code,"PASS")
    
    except AssertionError:
        save_result_in_csv_file( response.request.method, base_url,  response.status_code,"FALID")

def test_delete_post(base_url, id):
    response = requests.delete(base_url + id)
    data = response.json()
    # print(data)
    try:
        assert data == {}
        save_result_in_csv_file( response.request.method, base_url,  response.status_code,"PASS")

    except AssertionError:
        save_result_in_csv_file( response.request.method, base_url,  response.status_code,"FALID")

def test_response_time(base_url,id):
    response = requests.delete(base_url + id)
    response_time = response.elapsed.total_seconds() * 1000  # Convert to milliseconds

    # Test: Response time is less than 300ms
    try:
        assert response_time < 300, f"Response time exceeded limit: {response_time}ms"
        save_result_in_csv_file( response.request.method, base_url,  response.status_code,"PASS")
    except AssertionError:
        save_result_in_csv_file( response.request.method, base_url,  response.status_code,"FALID")

def content_type(base_url, id):
    try:
        # Send a GET request
        response = requests.get(base_url + "/42")

        # Check if the 'Content-Type' header is present
        assert "Content-Type" in response.headers
        save_result_in_csv_file( response.request.method, base_url,  response.status_code,"PASS")
    except AssertionError as e:
        save_result_in_csv_file( response.request.method, base_url,  response.status_code,"Faild")