from flask import Blueprint ,  render_template , request
from models import URL
import secrets , string

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html')

@views.route('/shorten' , methods=["POST"])
def shorten():
    url =  request.form.get('url').strip()
    if URL.query.filter_by(long_url=url).first():
        existing_url = URL.query.filter_by(long_url=url).first()
        return f"Short url is http://localhost:5000/{existing_url.short_code}"
    
    digits = string.digits + string.ascii_letters
    code = ''.join(secrets.choice(digits) for i in range(7))
    return code