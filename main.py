from fastapi import FastAPI
from models import Product
from database import session,engine
import database_model
app= FastAPI()

database_model.Base.metadata.create_all(bind=engine)  # This creates Tables cor us
products = [
    Product(id=1, name="Phone", description="A smartphone", price=699.99, quantity=50),
    Product(id=2, name="Laptop", description="A powerful laptop", price=999.99, quantity=30),
    Product(id=3, name="Pen", description="A blue ink pen", price=1.99, quantity=100),
    Product(id=4, name="Table", description="A wooden table", price=199.99, quantity=20),
]
def init_db():
    db=session()
    count=db.query(database_model.Product).count
    if count==0:
        for i in products:
            db.add(database_model.Product(**i.model_dump()))
        db.commit()

init_db()
@app.get('/')
def greet():
    return {"Message":"From The Fast API"}

@app.get("/products")
def get_products():
    # db=session()
    # db.query()
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

@app.put('/product')
def update(id:int,product:Product):
    for i in range(len(products)):
        if products[i].id==id:
            products[i]=product
            return 'Product Updated Sucessfully'
    return 'Product not found'

@app.delete('/product')
def product_delete(id:int):
    for i in range(len(products)):
        if products[i].id==id:
            del products[i]
            return 'Product Deleted'
    return 'Product Not Found'
