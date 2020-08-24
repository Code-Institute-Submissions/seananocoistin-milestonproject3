import os
import json
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

author = ""
app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'acmebd'
app.config["MONGO_URI"] = 'mongodb+srv://stiurthoir:b1o2l3l4i5x6@cluster0-gaug0.mongodb.net/acmebd?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/tasks")
def get_tasks():
    return render_template("tasks.html", tasks=mongo.db.users.find())

@app.route("/ownrecords")
def get_ownrecords():
    return render_template("tasks.html", tasks=mongo.db.users.find({"author":"Seanán"}))

@app.route("/create")
def add_create():
    return render_template("create.html")

@app.route("/addrecord", methods=["POST"])
def addrecord():
    if request.method == "POST":
        newrecord = request.form.to_dict()
        newrecord.update({"author":author})
        mongo.db.users.insert(newrecord)
        return get_tasks()

@app.route("/register", methods=["POST"])
def register():
    if request.method == "POST":
        user=mongo.db.accounts.insert(request.form.to_dict())
        global author
        author=request.form["username"]
        return add_create()

@app.route("/edit")
def add_edit():
    return render_template("edit.html")

@app.route("/delete")
def add_delete():
    return render_template("delete.html")

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
