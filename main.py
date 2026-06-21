from fastapi import FastAPI
from models import Product
app= FastAPI()

@app.get('/')
def greet():
    return {"Message":"From The Fast API"}
products = [
    Product(id=1, name="Phone", description="A smartphone", price=699.99, quantity=50),
    Product(id=2, name="Laptop", description="A powerful laptop", price=999.99, quantity=30),
    Product(id=3, name="Pen", description="A blue ink pen", price=1.99, quantity=100),
    Product(id=4, name="Table", description="A wooden table", price=199.99, quantity=20),
]
@app.get("/products")
def get_products():
    return products
@app.get("/product/{id}")
def get_product_by_id(id:int):
    for i in products:
        if i.id==id:
            return i
    return 'Product not Found'
    
@app.post('/product')
def add_to_list(product:Product):
    products.append(product)
    return product