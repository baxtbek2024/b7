from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == "admin" and password == "1234":
            return redirect(url_for("home"))
        else:
            msg = "Login xato"
            return render_template("index41.html", msg=msg)

    return render_template("index41.html")

@app.route("/home")
def home():
    return render_template("home41.html")

if __name__ == "__main__":
    app.run(debug=True)
