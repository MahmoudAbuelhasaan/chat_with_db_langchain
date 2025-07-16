import click
from flask.cli import with_appcontext
from app import db
from app.models import Product, category, OrderItem, Customer, Order
from datetime import datetime, timedelta
import random
from faker import Faker

fake = Faker()

@click.command(name='seed_db')
@with_appcontext
def seed_db():
    # db.drop_all()
    # db.create_all()

    # Create categories
    categories = []
    for _ in range(5):
        cat = category(
            name=fake.unique.word().capitalize(),
            description=fake.sentence()
        )
        db.session.add(cat)
        categories.append(cat)

    db.session.commit()

    # Create products
    products = []
    for _ in range(20):
        prod = Product(
            name=fake.unique.word().capitalize(),
            description=fake.text(max_nb_chars=200),
            price=round(random.uniform(10.0, 500.0), 2),
            stock_quantity=random.randint(10, 100),
            category_id=random.choice(categories).id,
            created_at=fake.date_time_between(start_date='-1y', end_date='now')
        )
        db.session.add(prod)
        products.append(prod)

    db.session.commit()

    # Create customers
    customers = []
    for _ in range(10):
        cust = Customer(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.unique.email(),
            phone_number=fake.phone_number(),
            address=fake.address()
        )
        db.session.add(cust)
        customers.append(cust)

    db.session.commit()

    # Create orders with order items
    for _ in range(15):
        cust = random.choice(customers)
        order = Order(
            customer_id=cust.id,
            order_date=fake.date_time_between(start_date='-6mo', end_date='now'),
            status=random.choice(['pending', 'shipped', 'delivered', 'cancelled']),
            shipping_address=cust.address,
            total_amount=0.0  # will update after adding items
        )
        db.session.add(order)
        db.session.flush()  # ensures order.id is available

        order_total = 0.0
        for _ in range(random.randint(1, 5)):
            product = random.choice(products)
            quantity = random.randint(1, 3)
            price = product.price * quantity
            item = OrderItem(
                order_id=order.id,
                product_id=product.id,
                quantity=quantity,
                price=price,
                product=product
            )
            order_total += price
            db.session.add(item)

        order.total_amount = round(order_total, 2)

    db.session.commit()
    click.echo("Database seeded successfully.")
