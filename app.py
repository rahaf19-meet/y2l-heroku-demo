
from flask import Flask
from flask import render_template
from flask import request, redirect, url_for
from database import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR-VERY-SECRET-SHHH'

@app.route('/')
def catbook_home():
    cats = get_all_cats()
    return render_template("home.html", cats=cats)

@app.route('/cats/<int:id>')
def cat_page(id):
	cat = my_cat(id)
	return render_template("cat.html", id=id , cat=cat)

@app.route('/catnew', methods=["GET", "POST"])
def new_cat():
    if request.method == 'GET':
        return render_template("new_cat.html")
    else:
    	name = request.form['firstname']
        create_cat(name)
        return redirect(url_for("catbook_home"))


if __name__ == '__main__':
   app.run(debug = True)
