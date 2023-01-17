from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Mort_cust(BaseModel):
    name: str
    salary: int
    age: int
    Type: str
    token: str


customer = {
    2 : {
        "name":"Mike",
        "salary" : 20,
        "age": 25,
        "Type": "home"
    },
    4 : {
        "name":"Jack",
        "salary" : 25,
        "age": 24,
        "Type": "Business"
    }
}

import jwt


def encode_user():
    encoded_data = jwt.encode(payload={"user": "sys-test-admin", "access": " approved"},
                              key='sy-secret',
                              algorithm="HS256")
                    
    return encoded_data

def decode_user(token: str):
    """
    :param token: jwt token
    :return:
    """
    decoded_data = jwt.decode(jwt=token,
                              key='sy-secret',
                              algorithms=["HS256"])

    return decoded_data

@app.get("/")
def index():
    return {"user":"SourabhMy"}

@app.get("/customer-details/{customer_id}")
def customer_details(customer_id: int):
    return customer[customer_id]

@app.get("/customer-det-name")
def customer_det_name(name: str):
    for customer_id in customer:
        if customer[customer_id]["name"] == name:
            return customer[customer_id]
    return {"Data": "not found"}

@app.post("/add_cust")
def add_cust(mort_cust: Mort_cust):
    new_token = mort_cust.token
    status = decode_user(new_token)["access"]
#    return status
#    print("status is " + status)
    new_custname = mort_cust.name
    return f"new customer name is {new_custname} and status is {status}"