from datetime import datetime
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, RegistrationForm
from app.models import User, Service_Item

@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()

@app.route('/', methods=['POST', 'GET'])
@app.route('/index', methods=['POST', 'GET'])
@login_required
def index():
    if request.method == 'POST':
        si_customer = request.form['customer']
        si_item = request.form['item']
        si_item_type = request.form['item_type']
        si_brand = request.form['brand']
        si_serial_num = request.form['serial_num']
        si_req_serv = request.form['req_serv']
        new_entry = Service_Item(customer=si_customer, item=si_item, item_type=si_item_type, brand=si_brand, serial_num=si_serial_num, req_serv=si_req_serv)
        try:
            db.session.add(new_entry)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your entry'
    else:
        contents = Service_Item.query.order_by(Service_Item.date_recvd).all()
        return render_template('index.html', title='Home', contents=contents)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit(): # method evaluates to FALSE if request is GET
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/user/<username>', methods=['GET', 'POST'])
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    # service_items = [
    #     {'author': user, 'body': 'Test post #1'},
    #     {'author': user, 'body': 'Test post #2'}
    # ]
    if request.method == 'POST':
        si_content = request.form['customer']
        new_entry = Service_Item(customer=si_content)

        try:
            db.session.add(new_entry)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your entry'

    else:
        entries = Service_Item.query.order_by(Service_Item.date_recvd).all()
        return render_template('user.html', user=user, entries=entries)

@app.route('/delete/<int:id>')
def delete(id):
    item_to_delete = Service_Item.query.get_or_404(id)

    try:
        db.session.delete(item_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that task'

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    item_to_update = Service_Item.query.get_or_404(id)

    if request.method == 'POST':
        iu_customer = request.form['customer']
        iu_item = request.form['item']
        iu_item_type = request.form['item_type']
        iu_brand = request.form['brand']
        iu_serial_num = request.form['serial_num']
        iu_req_serv = request.form['req_serv']
        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating your task'
    else:
        return render_template('update.html', item_to_update=item_to_update)