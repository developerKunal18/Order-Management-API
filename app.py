from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# ---------- Config ----------
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///orders.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# ---------- Order Model ----------
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    product = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(50), default="Pending")

# Create DB
with app.app_context():
    db.create_all()

# ---------- View Orders ----------
@app.route("/orders", methods=["GET"])
def get_orders():
    orders = Order.query.all()

    return jsonify([
        {
            "id": order.id,
            "customer_name": order.customer_name,
            "product": order.product,
            "quantity": order.quantity,
            "status": order.status
        }
        for order in orders
    ])

# ---------- Create Order ----------
@app.route("/orders", methods=["POST"])
def create_order():
    data = request.get_json()

    order = Order(
        customer_name=data["customer_name"],
        product=data["product"],
        quantity=data["quantity"]
    )

    db.session.add(order)
    db.session.commit()

    return jsonify({
        "message": "Order created"
    })

# ---------- Update Order Status ----------
@app.route("/orders/<int:order_id>", methods=["PUT"])
def update_order(order_id):
    data = request.get_json()

    order = Order.query.get(order_id)

    if order:
        order.status = data["status"]

        db.session.commit()

        return jsonify({
            "message": "Order updated"
        })

    return jsonify({
        "message": "Order not found"
    }), 404

# ---------- Delete Order ----------
@app.route("/orders/<int:order_id>", methods=["DELETE"])
def delete_order(order_id):
    order = Order.query.get(order_id)

    if order:
        db.session.delete(order)
        db.session.commit()

        return jsonify({
            "message": "Order deleted"
        })

    return jsonify({
        "message": "Order not found"
    }), 404

# ---------- Run ----------
if __name__ == "__main__":
    app.run(debug=True)
