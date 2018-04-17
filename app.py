from flask import Flask, render_template, request, redirect
import model

app = Flask(__name__)

@app.route("/")
def index():
    ## print the guestbook
    return render_template("admin.html", entries=model.get_entries())    #new template "admin.html"--hw14 part1

@app.route("/add")
def addentry():
    ## add a guestbook entry
    return render_template("addentry.html")

@app.route("/postentry", methods=["POST"])
def postentry():
    name = request.form["name"]
    message = request.form["message"]
    model.add_entry(name, message)
    return redirect("/")

@app.route("/delete", methods=["POST"])    #implement the "/delete" route--hw14 part3
def deleteentry():
    id=request.form["id"]
    model.delete_entry(id)
    return redirect("/")

if __name__=="__main__":
    model.init()
    app.run(debug=True)
