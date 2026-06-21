# models.py is used to define the database models/classes 
# that represent the structure of the application's data.

from pydantic import BaseModel
# Base model is used to do data validation like quantity or id cannot be negative, JSON Conversion
# When we use Base model we don't need the constructor
class Product(BaseModel):
    id:int
    name:str
    description:str
    price:float
    quantity:int
        