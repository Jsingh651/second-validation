from ast import Or
from flask_app import app
from flask import Flask, session, redirect, render_template, request
from flask_app.models.cokkies import Order
@app.route('/')
def index():
    return render_template('neworder.html')

@app.route('/show/orders')
def show_order():
    orders = Order.get_all()
    return render_template('showinfo.html',orders = orders)

@app.route('/create/order',methods = ['POST'])
def create_order():
    if not Order.validate(request.form):
        session['name'] = request.form['name']
        session['type'] = request.form['type']
        session['amount'] = request.form['amount']
        return redirect('/')
    Order.create(request.form)
    return redirect('/show/orders')

@app.route('/edit/<int:id>')
def edit_page(id):
    data = {'id': id}
    orders = Order.get_one(data)
    return render_template('editinfo.html',orders = orders)

@app.route('/update/order',methods = ['POST'])
def update ():
    if not Order.validate(request.form):
        return redirect('/')
    Order.update(request.form)
    return redirect('/show/orders')