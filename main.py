# imports
from flask import render_template as render
from app import create_app

app = create_app()

@app.route("/")
def index():
    return render('index.html')


if __name__ == '__main__':
    app.run("0.0.0.0", debug=True)