import pytest
from customers_db import CustomerDB

def test_insert_customer():
    db = CustomerDB()
    db.connect()

    db.insert_customer("Amrendra Bahubali","bahu@gmail.com")
    customer = db.get_customers_by_name("Amrendra Bahubali")

    assert customer is not None
    assert customer['name'] == "Amrendra Bahubali"
    assert customer['email'] == "bahu@gmail.com"

    db.clear_customers()
    db.close()

def test_get_all_customers():
    db = CustomerDB()
    db.connect()

    db.insert_customer('Virat Kohli','vk@gmail.com')
    db.insert_customer('Rohit Sharma','rh@gmail.com')

    customers = db.get_all_customers()

    assert len(customers) == 2

    db.clear_customers()
    db.close()