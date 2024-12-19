from flask import session, redirect, url_for

def is_authenticated():
    return session.get('authenticated', False)

def authenticate(password, admin_password):
    if password == admin_password:
        return True
    return False

def login_user():
    session['authenticated'] = True

def logout_user():
    session.pop('authenticated', None)

def login_required(func):
    def wrapper(*args, **kwargs):
        if not is_authenticated():
            return redirect(url_for('main.login'))
        return func(*args, **kwargs)
    wrapper.__name__ = func.__name__  # preserve function name
    return wrapper
