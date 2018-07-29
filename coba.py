from flask import Flask, render_template, request, redirect, url_for
import MySQLdb

app =Flask(__name__)
app.debug = True

conn = MySQLdb.connect(host='localhost',user='root',password='',db=takudb)

@app.route('/')
def index():
    return render_template('index.html', title='menuawal')

@app.route('/signup')
def signup():
    username =str(request.form['user'])
    email =str(request.form['email'])
    password =str(request.form['password'])


if __name__ =='__main__':
    app.run(debug=True)

