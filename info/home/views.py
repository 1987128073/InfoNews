from flask import session, current_app

from info.home import home_blue


@home_blue.route('/')
def index():
    session['name'] = 'zs'
    return 'copy '

