from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', title="Home Page")

@app.route('/projects')
def projects():
    return render_template('projects.html', title="Projects")

@app.route('/contact')
def contact():
    return render_template('contact.html', title="Contact Us")

if __name__ == '__main__':
    app.run(debug=True)
