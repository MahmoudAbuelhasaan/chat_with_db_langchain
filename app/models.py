from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import UserMixin
from datetime import datetime

from app import db

class User(db.model):
    id = db.Columne(db.Integer, primary_key=True)
    username = db.Columne(db.string(80),unique=True,nullable=False)
    email = db.Columne(db.string(120),unique=True,nullable=False)
    password_hash = db.Columne(db.string(120),nullable=False)
    created_at = db.Columne(db.DateTime, default=datetime.utcnow)
    role = db.Column(db.String(120), default='customer')


    def set_password(self, password):
        self.password_hash = Bcrypt.generate_password_hash(password).decode('utf-8')


    def cheack_password(self, password):
        return Bcrypt().check_password_hash(self.password_hash, password)
    
    def has_access_to_table(self, table_name):
        role_permissions = {
            'customers': ['orders','products','category'],
            'manager': ['users','orders','products','category'],
            'admin': ['users','category' 'products', 'orders','chat_sessions','orders_items','customers']
           
        }
        return table_name in role_permissions.get(self.role, [] ) 
       

class ChatSession(db.model):
    id = db.Columne(db.Integer,primary_key=True)
    user_id = db.Columne(db.Integer, db.ForeignKey('user.id'), nullable=False)
    question = db.Columne(db.Text, nullable=False)
    response = db.Columne(db.Text, nullable=False)
    create_at = db.Columne(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User', backref=db.backref('chat_sessions'))

class Product(db.model):
    id = db.Columne(db.Integer, primary_key=True)
    name = db.Columne(db.String(120), nullable=False)
    description = db.Columne(db.Text, nullable=True)
    price = db.Columne(db.Float, nullable=False)
    stock_quantity = db.Columne(db.Integer, nullable=False)
    category_id = db.Columne(db.Integer, db.ForeignKey('category.id'), nullable=False)
    created_at = db.Columne(db.DateTime, default=datetime.utcnow)




class category(db.model):
    id = db.Columne(db.Integer, primary_key=True)
    name = db.Columne(db.String(120), unique=True, nullable=False)
    description = db.Columne(db.Text, nullable=True)

    products = db.relationship('Product', backref='category')
  


class Customer(db.model):
    id = db.Columne(db.Integer, primary_key=True)
    first_name = db.Columne(db.String(80), nullable=False)
    last_name = db.Columne(db.String(80), nullable=False)
    email = db.Columne(db.String(120), unique=True, nullable=False)
    phone_number = db.Columne(db.String(20), nullable=True)
    address = db.Columne(db.String(255), nullable=True)
    orders = db.relationship('Order', backref='customer')

class Order(db.model):
    id = db.Columne(db.Integer, primary_key=True)
    customer_id = db.Columne(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    order_date = db.Columne(db.DateTime, default=datetime.utcnow)
    status = db.Columne(db.String(50), nullable=False, default='pending')
    order_items = db.relationship('OrderItem', backref='order',casecade='all, delete-orphan',lazy=True)
    total_amount = db.Columne(db.Float, nullable=False)
    shipping_address = db.Columne(db.String(255), nullable=True)
    
    
class OrderItem(db.model):
    id = db.Columne(db.Integer, primary_key=True)
    order_id = db.Columne(db.Integer, db.ForeignKey('order.id'), nullable=False)
    product_id = db.Columne(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Columne(db.Integer, nullable=False)
    price = db.Columne(db.Float, nullable=False)

    product = db.relationship('Product', backref='order_items')
  