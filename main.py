from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from models import Product
from database import session,engine
from sqlalchemy.orm import Session
import database_model
app= FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],   # Frontend running link
    allow_methods=["*"],        # when we do any action in frontend, we want to say ok to backend
    allow_headers=["*"]
)

database_model.Base.metadata.create_all(bind=engine)  # This creates Tables for us

def init_db():
    db=session()
    count=db.query(database_model.Product).count
    if count==0:
        for i in products:
            db.add(database_model.Product(**i.model_dump()))
        db.commit()

def get_db():
    db=session()
    try:
        yield db
    finally:
        db.close()
@app.get('/')
def greet():
    return {"Message":"From The Fast API"}

@app.get("/products")
def get_products(db:Session=Depends(get_db)):
    products=db.query(database_model.Product).all()
    return products

@app.get("/products/{id}")
def get_product_by_id(id:int,db:Session=Depends(get_db)):
    product1=db.query(database_model.Product).filter(database_model.Product.id==id).first()
    if product1:
        return product1
    else:
        return "Product Not found"
    

@app.post('/products')
def add_to_list(product:Product,db:Session=Depends(get_db)):
    db.add(database_model.Product(**product.model_dump()))
    db.commit()
    return product

@app.put('/products/{id}')
def update(id:int,product:Product,db:Session=Depends(get_db)):
    product1=db.query(database_model.Product).filter(database_model.Product.id==id).first()
    if product1:
        product1.name=product.name
        product1.description=product.description
        product1.price=product.price
        product1.quantity=product.quantity
        db.commit()
        return "Product updated"
    else:
        return "Product Not Found"
@app.delete('/products/{id}')
def product_delete(id:int,db:Session=Depends(get_db)):
    product1=db.query(database_model.Product).filter(database_model.Product.id==id).first()
    if product1:
        db.delete(product1)
        db.commit()
        return "Product deleted Sucessfully"
    else:
        return 'Product Not Found'
