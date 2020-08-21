from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Jeffrey'}
    service_items = [
        {
            'receiving_staff': {'username': 'Anna'},
            'customer': 'Mario Diving',
            'product_for_service': {'item_type': 'compressor', 'brand': 'coltri'}
        },
        {
            'receiving_staff': {'username': 'Ruben'},
            'customer': 'Mark Lapid',
            'product_for_service': {'item_type': 'dive computer', 'brand': ' suunto'}
        }
    ]
    return render_template('index.html', title='Home', user=user, service_items=service_items)