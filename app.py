from flask import Flask, render_template
from controllers.controller import tasks_blueprint
import repositories.author_repository as author_repo

app = Flask(__name__)

app.register_blueprint(tasks_blueprint)

@app.route('/')
def home():
    authors = author_repo.select_all()
    return render_template('home.jinja',title = "home",authors=authors)

if __name__ == '__main__':
    app.run(debug=True)
