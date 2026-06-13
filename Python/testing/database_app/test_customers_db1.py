import pytest
from customers_db import CustomerDB

@pytest.fixture
def db():
    # set up
    db_instance = CustomerDB()
    db_instance.connect()
    
    yield db_instance
    
    # tear down
    db_instance.clear_customers()
    db_instance.close()


def test_insert_customer(db):
    db.insert_customer("Amrendra Bahubali","bahu@gmail.com")
    customer = db.get_customers_by_name("Amrendra Bahubali")

    assert customer is not None
    assert customer['name'] == "Amrendra Bahubali"
    assert customer['email'] == "bahu@gmail.com"

def test_get_all_customers(db):
    db.insert_customer('Virat Kohli','vk@gmail.com')
    db.insert_customer('Rohit Sharma','rh@gmail.com')

    customers = db.get_all_customers()

    assert len(customers) == 2