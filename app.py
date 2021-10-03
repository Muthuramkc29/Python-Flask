from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def homepage():
    return " HELLO UNIVERSE !!! PYTHON IS ALWAYS AWESOME "


@app.route("/no_page")
def no_page():
    return " NO USERS CURRENTLY "


@app.route('/admin')
def users():        # url_for(FUNCTION_NAME, **kwargs)
    return redirect(url_for("user_name", username="KC"))


@app.route("/<username>")
def user_name(username):
    return f"Hello {username}"


# INHERITED FROM BASE.HTML
@app.route("/temp")
def rend_temp():
    return render_template("index.html")
# BASE.HTML
# CSS STYLE SHEETS ARE PLACED UPON HEAD TAG ABOVE TITLE....
# NAV BAR IS PLACED UPON BODY TAG TO REPRESENT IN THE TOP BODY...
# JS JAVA SCRIPTS IS PLACED DOWN SIDE OF THE BODY BELOW OUR CONTENTS BLOCK...


@app.route("/new")
def new():
    return render_template("new.html")


@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form["nm"]
        return redirect(url_for("user_name", username=user))
    else:
        return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)
