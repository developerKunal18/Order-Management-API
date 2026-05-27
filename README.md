# Order Management API

A backend API for managing customer orders.

## Features
- Create orders
- View all orders
- Update order status
- Delete orders
- SQLAlchemy ORM
- JSON API responses

## Technologies Used
- Python
- Flask
- Flask-SQLAlchemy
- SQLite3

## Installation

pip install flask flask-sqlalchemy

## Run

python app.py

## API Endpoints

GET /orders  
POST /orders  
PUT /orders/<id>  
DELETE /orders/<id>

## Example JSON

{
    "customer_name": "Rahul",
    "product": "Laptop",
    "quantity": 1
}

## Update Status Example

{
    "status": "Shipped"
}

## Purpose
focuses on order workflow management systems.
