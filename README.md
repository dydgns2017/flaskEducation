# flaskEducation
플라스크 학습해보기!

### Flask 란?

Django 보다는 더 쉽게 웹 서비스를 구현할 수 있는 파이썬 웹 제작 도구

### Flask 설치

```
pip install Flask
```

### 1. 간단하게 시작하기

```
# save this as app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"
```

### 2. HTML/CSS 활용하여 작성해보기

POST.js 사용방법 및 JSON 방식

```
from flask import Flask, request
import json


app = Flask(
    __name__,
    static_url_path='',
    static_folder='html/',
)


@app.route('/')
@app.route('/home')
def home():
    return app.send_static_file("index.html")


@app.route('/service', methods=['POST'])
def service():
    return outputJSON("service is ok", "ok")

def outputJSON(msg, status="error"):
    return {"data": msg, "status": status}
```

### 3. 로그인 창 만들기

### 4. 간단한 홈페이지 따라서 만들기
