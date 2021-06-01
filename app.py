#importing all the libraries 
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
import json
from datetime import datetime
from flask import session
from flask import sessions

#reading config.json file 
with open('config.json', 'r') as c:
    parameters = json.load(c)["parameters"]
with open('config.json', 'r') as d:
    anchors = json.load(d)["anchors"]
with open('config.json', 'r') as e:
    websitecreds = json.load(e)["websitecreds"]



#setting the smtp server configs of using flask_mail
app = Flask(__name__)
app.secret_key = 'super-secret-key'
app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = parameters['gmail-user'],
    MAIL_PASSWORD=  parameters['gmail-password']
)
mail = Mail(app)


#passing the SQLAlchemy URI
local_server = True
if(local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = parameters['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = parameters['prod_uri']



#setting up tables as classes and methods as field

#TABLE1- Contacts: for the contact form
db = SQLAlchemy(app)
class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    phone_num = db.Column(db.String(12), nullable=False)
    msg = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    email = db.Column(db.String(20), nullable=False)

#TABLE2-posts for plugging posts
class Posts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    tagline = db.Column(db.String(120), nullable=False)
    slug = db.Column(db.String(21), nullable=False)
    content = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    img_file = db.Column(db.String(12), nullable=True)




#declaring the various routes

#home-page
@app.route("/")
def home():
    posts = Posts.query.filter_by().all()[0:parameters['number_of_posts']]
    #returning all the json variable lists with the template file
    return render_template('index.html', parameters=parameters,anchors=anchors,websitecreds=websitecreds, posts=posts)


#about-page
@app.route("/about")
def about():
    #returning all the json variable lists with the template file
    return render_template('about.html', parameters=parameters,anchors=anchors,websitecreds=websitecreds)


#contact form
@app.route("/contact", methods = ['GET', 'POST'])
def contact():
    if(request.method=='POST'):
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        entry = Contacts(name=name, phone_num = phone, msg = message, date= datetime.now() ,email = email )
        db.session.add(entry)
        db.session.commit()
        #using flask_mail to send email everytime a new contact request is made
        mail.send_message('New message from ' + name,
                          sender=email,
                          recipients = [parameters['gmail-recipient']],
                          body = message + "\n" + phone
                          )
    #returning all the json variable lists with the template file
    return render_template('contact.html', parameters=parameters,anchors=anchors,websitecreds=websitecreds)


@app.route("/post/<string:post_slug>", methods=['GET'])
def post_route(post_slug):
    post = Posts.query.filter_by(slug=post_slug).first()
    return render_template('post.html', parameters=parameters, post=post,anchors=anchors,websitecreds=websitecreds)



# #admin-login
# @app.route("/admin-dashboard", methods=['GET','POST'])
# def adminlogin():
#     #returning all the json variable lists with the template file
#     return render_template('login.html',parameters=parameters)

@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard():

    if ("user" in session and session['user']==parameters['admin_user']):
            posts = Posts.query.all()
            return render_template("dashboard.html", parameters=parameters,anchors=anchors,uname=parameters['admin_user'], posts=posts)

    if (request.method=="POST"):
        username = request.form.get("uname")
        userpass = request.form.get("adminpassword")

        if (username==parameters['admin_user'] and userpass==parameters['admin_password']):
            #session variable1
            session['user']=username
            posts = Posts.query.all()
            return render_template("dashboard.html", parameters=parameters,anchors=anchors,uname=username,posts=posts)

    return render_template('login.html',parameters=parameters)

'''

@app.route("/edit/<string:sno>" , methods = ['GET', 'POST'])
def edit(sno):
    if "user" in session and session['user'] == parameters['admin_user']:
        if request.method=="POST":
            box_title = request.form.get('title')
            tline = request.form.get('tline')
            slug = request.form.get('slug')
            content = request.form.get('content')
            img_file = request.form.get('img_file')
            date = datetime.now()

            if sno=='0':
                post = Posts(title=box_title, slug=slug, content=content, tagline=tline, img_file=img_file, date=date)
                db.session.add(post)
                db.session.commit()
            else:
                post = Posts.query.filter_by(sno=sno).first()
                post.title = box_title
                post.slug = slug
                post.content = content
                post.tagline = tline
                post.img_file = img_file
                post.date = date
                db.session.commit()
                return redirect('/edit/'+sno)
        post = Posts.query.filter_by(sno=sno).first()
        return render_template('edit.html', parameters=parameters, post=post, sno=sno, anchors=anchors)

'''
@app.route("/edit/<string:sno>" , methods=['GET', 'POST'])
def edit(sno):
    if "user" in session and session['user']==parameters['admin_user']:
        if request.method=="POST":
            box_title = request.form.get('title')
            tline = request.form.get('Tline')
            slug = request.form.get('slug')
            content = request.form.get('content')
            img_file = request.form.get('img_file')
            date = datetime.now()
        
            if sno=='0':
                post = Posts(title=box_title, slug=slug, content=content, tagline=tline, img_file=img_file, date=date)
                db.session.add(post)
                db.session.commit()
            else:
                post = Posts.query.filter_by(sno=sno).first()
                post.box_title = box_title
                post.tline = tline
                post.slug = slug
                post.content = content
                post.img_file = img_file
                post.date = date
                db.session.commit()
                return redirect('/edit/'+sno)

        post = Posts.query.filter_by(sno=sno).first()
        return render_template('edit.html', parameters=parameters, post=post, anchors=anchors,sno=sno)






#for auto-reconfiguring everytime a change is made in the app.py file
app.run(debug=True)

