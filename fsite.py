from flask import Flask, render_template, url_for, request

app = Flask(__name__)

menu = [{"name": "Install", "url":"install-flask"},
        {"name": "First app", "url": "first-app"},
        {"name": "Feedback", "url": "contact"}]

@app.route("/index")
@app.route("/")
def index():
    print(url_for('index'))
    return render_template('index.html', menu=menu)


@app.route("/about")
def about():
    print(url_for('about'))
    return render_template('about.html', title="About Site", menu=menu)

@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == 'POST':
        print(request.form)

    return render_template('contact.html', title="Feedback", menu=menu)

@app.route("/profile/<path:username>")
def profile(username):
    return f"User:{username}"

# with app.test_request_context():
#     print(url_for('about'))
if __name__ == "__main__":
    app.run(debug=True)
