from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from .auth import authenticate, login_user, logout_user, login_required

main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET'])
def index():
    return redirect(url_for('main.login'))

@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        password = request.form.get('password', '')
        if authenticate(password, current_app.config['ADMIN_PASSWORD']):
            login_user()
            return redirect(url_for('main.dashboard'))
        else:
            flash("Invalid password!", "error")
    
    return render_template('login.html')

@main_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.login'))

@main_bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')
