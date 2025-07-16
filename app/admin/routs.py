from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models import User, Product, Order
from app import db


@login_required
def dashboard():
    if current_user.role != 'admin':
        flash('Access denied: Admins only.', 'danger')
        return redirect(url_for('chat.chat'))
    user_count = User.query.count()
    product_count = Product.query.count()
    order_count = Order.query.count()
    return render_template('admin/dashboard.html', user_count=user_count, product_count=product_count, order_count=order_count)

@login_required
def manage_users():
    if current_user.role != 'admin':
        flash('Access denied: Admins only.', 'danger')
        return redirect(url_for('chat'))
    users = User.query.all()
    return render_template('admin/users_manage.html', users=users)

@login_required
def update_user_role():
    if current_user.role != 'admin':
        flash('Access denied: Admins only.', 'danger')
        return redirect(url_for('chat'))
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        new_role = request.form.get('role')
        user = User.query.get(user_id)
        if user:
            user.role = new_role
            db.session.commit()
            flash('User role updated successfully.', 'success')
        else:
            flash('User not found.', 'danger')
    return redirect(url_for('admin.manage_users'))