from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit(): # method evaluates to FALSE if request is GET
        flash(f'Login requested for user {form.username.data}, remember_me={form.remember_me.data}')
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)