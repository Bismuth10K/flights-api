import requests
import json

def q16():
    req = requests.get("http://localhost:5000/users")
    return req


def q17_get_hubert():
    req = requests.get('http://localhost:5000/users/hubert')
    return req


def q17_patch():
    headers={'content-type': 'application/json'}
    req = requests.patch('http://localhost:5000/users/hubert', data=json.dumps({'password':'111'}), headers=headers)
    return req


def q17_add_user():
    headers={'content-type': 'application/json'}
    payload={'username': 'hubulle', 'password': '222'}
    req = requests.post('http://localhost:5000/users/', data=json.dumps(payload), headers=headers)
    return req


# print(q16().json())
# print(q17_get_hubert().json())
# print(q17_patch().json())
print(q17_add_user().json())
print(q16().json())