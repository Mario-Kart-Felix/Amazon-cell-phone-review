from flask import Flask,render_template,request,url_for
from flask_bootstrap import Bootstrap


from textblob import TextBlob,Word
import random

app=Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
	return render_template('index.html')


if __name__=='__main__':
	app.run(debug=True)
