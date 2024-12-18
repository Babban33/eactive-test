from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.models import User

# Define a Blueprint
main = Blueprint('main', __name__)

@main.route('/hello')
def hello():
    return "Hello World!"

@main.route('/users')
def users():
    all_users = User.query.all()
    return render_template('users.html', users=all_users)

@main.route('/new_user', methods=['GET', 'POST'])
def new_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        role = request.form['role']
        new_user = User(name=name, email=email, role=role)
        db.session.add(new_user)
        db.session.commit()
        flash('User added successfully!')
        return redirect(url_for('main.users'))
    return render_template('new_user.html')

@main.route('/users/<int:id>')
def user_detail(id):
    user = User.query.get_or_404(id)
    return render_template('user_detail.html', user=user)