from flask import Flask, render_template, url_for, request, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'retreading'

menu = [{"name": "My portfolio", "url": "profile"},
        {"name": "My resume", "url": "resume"},
        {"name": "My testform", "url": "contact"}]
@app.route("/")
def index():
    # print(url_for('index'))
    return render_template('index.html', menu=menu)
@app.route('/about')
def about():
    print(url_for('about'))
    return render_template('about.html', title='About Me', menu=menu)
@app.route('/contact', methods=["POST", "get"])
def contact():
    if request.method == 'POST':
        if len(request.form['username']) > 2:
            flash('Message send', category='success')
        else:
            flash('Error message send', category='error')

    return render_template('contact.html', title='Contact', menu=menu)
@app.route('/profile/<username>')
def profile(username, path):
    return f"User: {username}, {path}"


if __name__ == "__main__":
    app.run(debug=True)
