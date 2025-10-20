import random
from decimal import Decimal

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils import lorem_ipsum
from app.models import User, Product, Order, OrderItem

class Command(BaseCommand):
    help = 'Creates application data'

    def handle(self, *args, **kwargs):
        # get or create superuser
        user = User.objects.filter(username='admin').first()
        if not user:
            user = User.objects.create_superuser(username='admin', password='test')

        # create products - name, desc, price, stock, image
        products = []
        product_names = [
            "A Scanner Darkly", "Coffee Machine", "Velvet Underground & Nico",
            "Enter the Wu-Tang (36 Chambers)", "Digital Camera", "Watch",
            "Bluetooth Speaker", "Wireless Mouse", "Mechanical Keyboard",
            "Smartphone", "Laptop", "Tablet", "Headphones", "Book: Dune",
            "Book: Neuromancer", "Book: Foundation", "Book: The Hobbit",
            "Book: 1984", "Book: Brave New World", "Book: Fahrenheit 451",
            "Electric Toothbrush", "Hair Dryer", "Vacuum Cleaner", "Air Purifier",
            "Desk Lamp", "Monitor", "TV", "Router", "SSD Drive", "External HDD",
            "USB Flash Drive", "Power Bank", "Fitness Tracker", "Smartwatch",
            "Camera Lens", "Tripod", "Microphone", "Guitar", "Piano Keyboard",
            "Drum Machine", "Synthesizer", "Vinyl Record", "CD Album",
            "Board Game", "Puzzle", "Toy Car", "Action Figure", "Drone",
            "RC Helicopter", "3D Printer", "Graphic Tablet"
        ]
        for i in range(50):
            products.append(
            Product(
                name=product_names[i % len(product_names)] + f" #{i+1}",
                description=lorem_ipsum.paragraph(),
                price=Decimal(str(round(random.uniform(10, 500), 2))),
                stock=random.randint(0, 20)
            )
            )

        # create products & re-fetch from DB
        Product.objects.bulk_create(products)
        products = Product.objects.all()


        # create some dummy orders tied to the superuser
        for _ in range(3):
            # create an Order with 2 order items
            order = Order.objects.create(user=user)
            for product in random.sample(list(products), 2):
                OrderItem.objects.create(
                    order=order, product=product, quantity=random.randint(1,3)
                )