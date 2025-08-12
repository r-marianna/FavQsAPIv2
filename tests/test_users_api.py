import requests
from faker import Faker

ENDPOINT = "https://favqs.com/api"
API_KEY = "1046e159e3ecc9cc6c6e8b07eff857fb"
fake = Faker()


def test_can_create_user():
  payload = create_user_payload()
  unauth_headers = headers()
  
  create_user_response = create_user(payload, unauth_headers)

  assert create_user_response.status_code == 200, "User is not created"

  data = create_user_response.json()
  print(data)
  
  login = data['login']
  user_token = data['User-Token']

  assert login == payload["user"]["login"], "Login does not match"

  auth_headers = headers(user_token)
  
  get_user_response = get_user(login, auth_headers)
  assert get_user_response.status_code == 200, "Get user failed"
  get_user_data = get_user_response.json()
  print(get_user_data)
  assert get_user_data["account_details"]["email"] == payload["user"]["email"], "Email does not match"

def test_can_update_user():
  payload = create_user_payload()
  unauth_headers = headers()
  
  create_user_response = create_user(payload, unauth_headers)
  assert create_user_response.status_code == 200, "User creation failed"
  create_user_data = create_user_response.json()
  print(create_user_data)
  
  login = create_user_data['login']
  user_token = create_user_data['User-Token']
  
  update_payload = { 
    "user": {
      "login": fake.user_name(),
      "email": fake.email()
    }
  }

  auth_headers = headers(user_token)
  update_user_response = update_user(login, update_payload, auth_headers)

  assert update_user_response.status_code == 200, "User update failed"

  update_user_data = update_user_response.json()
  print(update_user_data)

  assert update_user_data["message"] == 'User successfully updated.', "Update message does not match"

  updated_login = update_payload['user']['login']
  get_updated_user = get_user(updated_login, auth_headers)

  assert get_updated_user.status_code == 200, "Get updated user failed"

  get_updated_user_data = get_updated_user.json()
  print(get_updated_user_data)

  get_updated_user_data_email = get_updated_user_data["account_details"]["email"]
  get_updated_user_data_login = get_updated_user_data["login"]

  assert get_updated_user_data_email == update_payload["user"]["email"] and get_updated_user_data_email != payload["user"]["email"], "Email not updated"
  assert get_updated_user_data_login == updated_login and get_updated_user_data_login != payload["user"]["login"], "Login not updated"



def headers(user_token=None):
  headers = {
        "Authorization": f'Token token="{API_KEY}"',
        "Content-Type": "application/json",
    }
  if user_token:
    headers["User-Token"] = user_token
  return headers

def create_user(payload, base_headers):
  return requests.post(f"{ENDPOINT}/users", json=payload, headers=base_headers)

def update_user(login, payload, headers):
  return requests.put(f"{ENDPOINT}/users/{login}", json=payload, headers=headers)

def create_user_payload():
  return { 
    "user": {
      "login": fake.user_name(),
      "email": fake.email(),
      "password": fake.password()
    }
}

def get_user(login, headers):
  return requests.get(f"{ENDPOINT}/users/{login}", headers=headers)