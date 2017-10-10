#-*-coding:utf-8-*-

from flask import Flask, render_template, session, redirect, url_for, current_app
from flask_bootstrap import Bootstrap
from spider import getnews, getfund, getstock
from form import LoginForm
from flask_mail import Mail, Message
from config import ADMINS

app = Flask(__name__)
app.config.from_object('config')



bootstrap = Bootstrap(app)
mail = Mail(app)

numbers = ['sh000300']

# with app.app_context():
#     # within this block, current_app points to app.
#     msg = Message('test flask', sender=ADMINS[0], recipients=ADMINS)
#     msg.body = 'text body'
#     msg.html = '<b>HTML</b> body'
#     mail.send(msg)


@app.route('/')
def index():
    return render_template('index.html', numbers=numbers, news=getnews(), funddatas=getfund('160215'), stockdatas=getstock('sh000001'))
@app.route('/404')
def error():
    return render_template('404.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/login', methods=['Get', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        session['username'] = form.username.data
        session['HasLogin'] = True
        return redirect(url_for('index'))
    return render_template('login.html', form=form)
@app.route('/logout')
def logout():
    session['HasLogin'] = False
    return render_template('logout.html')

if __name__ == '__main__':
    app.run()
