from flask import Flask, render_template, url_for, request, flash, session, redirect, abort

app = Flask(__name__)
app.config['SECRET_KEY'] = 'retreading'

menu = [{"name": "About Me", "url": "about"},
        {"name": "Exemple Bug report and Testcase", "url": "bugrep"},
        {"name": "Example Testform", "url": "testform"},
        {"name": "Login", "url": "login"},
        {"name": "My resume page", "url": "/"}]


@app.route("/")
def index():
    if 'visits' in session:
        session['visits'] = session.get('visits') + 1 # update info sission
    else:
        session['visits'] = 1 # recording info in session
    # return f"<h1>Main Page</h1><p>Number visitors: {session['visits']}"

    return render_template('index.html', title='My resume page', footer=f" Visitors: {session['visits']}", menu=menu)


@app.route('/about')
def about():
    print(url_for('about'))
    return render_template('about.html', title='About Me', menu=menu)

@app.route('/bugrep')
def bugrep():
    print(url_for('bugrep'))
    return render_template('bugrep.html', title='Exemple Bug report and Testcase', menu=menu)


@app.route('/testform', methods=["POST", "get"])
def testform():
    if request.method == 'POST':
        if len(request.form['username']) > 2:
            flash('Message send', category='success')
        else:
            flash('Error message send', category='error')

    return render_template('testform.html', title='Test Form', menu=menu)


@app.route('/profile/<username>')
def profile(username):
    if 'userLogged' not in session or session['userLogged'] != username:
        abort(401)

    return f"User profile: {username}"

@app.route('/login', methods=["POST", "get"])
def login():
    if 'userLogged' in session:
        return redirect(url_for('profile', username=session['userLogged']))
    elif request.method == 'POST' and request.form['username'] == "test" and request.form['psw'] == "123":
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged']))

    return render_template('login.html', title='Autorisation', menu=menu)



@app.errorhandler(404)
def pageNotFound(error):
    return render_template('page404.html', title='Страница не найдена', menu=menu), 404


if __name__ == "__main__":
    app.run(debug=True)
