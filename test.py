# save this as app.py
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "정용훈 홈페이지"

app.run(debug=True)