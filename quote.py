from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)

#connect to db
#following line is to connect to local database
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:Postg#123@localhost/quotedb'
#following line is to connect to heroku's postgres database - copied from var settings on heroku
app.config['SQLALCHEMY_DATABASE_URL']='postgres://vsaykqnctpdole:5deaa00920aa7874264c87e530fb7f0845f42de1f02e4375b704002cefc4b34d@ec2-3-224-97-209.compute-1.amazonaws.com:5432/d9lplpfhur53rq'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)
class Favquotes(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    author=db.Column(db.String(30))
    quote=db.Column(db.String(2000))

@app.route('/')
def index():
    #return render_template('index.html',quote='Be Kind') #removed variable for Jinja for rendering in index.html
    result=Favquotes.query.all()
    return render_template('index.html', result=result)





#commenting out about page
#@app.route('/about')
#def about():
 #   return render_template('about.html')

@app.route('/quotes')
def quotes():
    return render_template('quotes.html')

@app.route('/process',methods = ['POST'])
def process():
    author = request.form['author']
    quote = request.form['quote']
    quotedata=Favquotes(author=author, quote=quote)
    db.session.add(quotedata)
    db.session.commit()
    return redirect(url_for('index'))