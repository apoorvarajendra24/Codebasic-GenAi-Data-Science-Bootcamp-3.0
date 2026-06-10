from fastapi import FastAPI
from enum import Enum
app = FastAPI()

# endpoint
@app.get("/")
def get_home():
    return "Hello"

@app.get("/hello/{name}")
def get_greeting(name):
    return f"Hello {name}"


# fastapi uses type hints to validate inputs
class AvailableCuisine(str,Enum):
    indian = 'indian'
    mexican = 'mexican'
    italian = 'italian'
    japanese = 'japanese'

food_items = {
    'indian': ['samosa','dosa','idli'],
    'mexican' : ['tacos','mexican noddles'],
    'italian' : ['pasta','pizza'],
    'japanese' : ['momos','ramen','sushi']
}

@app.get("/get_items/{cuisine}")
def get_cuisine(cuisine: AvailableCuisine):    # python type hint
    # items = food_items.get(cuisine)
    # if not items:
    #     return f"{cuisine} cuisine is not available."
    
    return food_items.get(cuisine)

#FastAPI automatically returns a validation error because it uses the type hint int to check the input.


coupon_code = {
    1 : '10%',
    2 : '20%',
    3 : '30%'
}

@app.get("/get_coupon/{code}")
async def get_items(code: int):
    return {"discount_amount" : coupon_code.get(code)}