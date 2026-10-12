from flask import Blueprint ,  render_template , request , redirect 
from models import URL
from db import db
import secrets , string

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html')

@views.route('/shorten' , methods=["POST"])
def shorten():
    url =  request.form.get('url').strip()
    if not url.startswith(('http://' , 'https://')):
        url = "https://" + url    
    if URL.query.filter_by(long_url=url).first():
        existing_url = URL.query.filter_by(long_url=url).first()
        return f"Short url is http://localhost:5000/{existing_url.short_code}"
    
    digits = string.digits + string.ascii_letters
    code = ''.join(secrets.choice(digits) for i in range(7))
    while URL.query.filter_by(short_code=code).first():
        code  = ''.join(secrets.choice(digits) for i in range(7))

    new_url = URL(long_url=url, short_code=code)
    db.session.add(new_url)
    db.session.commit()

    return f"Short url is http://localhost:5000/{code}"

@views.route('/<code>')
def redirect_to_original_url(code):
    url = URL.query.filter_by(short_code=code).first()
    if url:
        return redirect(url.long_url)
    else:
        return render_template("error404.html") ,404

