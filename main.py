from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:letsgo@localhost:8889/build-a-blog'
                                         
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class Blog(db.Model): 

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(500))


    def __init__(self, title, body):
        self.title = title
        self.body = body

blogs = []
bodies = []   

@app.route('/', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':
        blog = (request.form['blog'])
        body = (request.form['body'])

        blogs.append(blog)
        bodies.append(body)
    
    return render_template('blog.html', title="Build A Blog", blogs=blogs, bodies=bodies)

if __name__ == '__main__':
    app.run()