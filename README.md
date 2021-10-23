
<h1 align="center">Simple Shop</h1>


<p align="left">This online shop enable clients to browse products, add them to the cart, go through
the checkout process, pay with a credit card, and obtain an invoice.</p>
Images :
 <img height="200" src="https://github.com/steellsas/Shop/blob/main/document/pay%20creadit.png" width="200"/> 
 <img  src="https://github.com/steellsas/Shop/blob/main/document/cart.jpg?raw=true"/>
 <img  src="https://github.com/steellsas/Shop/blob/main/document/Product%20List.png"/>
 <img  src="https://github.com/steellsas/Shop/blob/main/document/orderadminlist.jpg"/>
 <img  src="https://github.com/steellsas/Shop/blob/main/document/checkout.jpg"/>

In this project, I do:
- Created a product catalog
- Shopping cart using Django sessions
- Created custom context processors
- Manage customer orders
- Configure Celery in  project with RabbitMQ as a message broker
- Send asynchronous notifications to customers using Celery
- Integrate a payment gateway into your project
- Export orders to CSV files
- Create custom views for the administration site
- Generate PDF invoices dynamically



## Built With

- Python 3.9
- Django
- SQLLite
- Celery (forasynchronous task)
- BrainTree 
- HTML
- CSS
- 
#Instruction

- clone project code
- create venv
- pip install requirements.txt
- Migrate  Db project
- Create superuser
- Install add  RabbitMQ
- create braintree aacount for test payment
