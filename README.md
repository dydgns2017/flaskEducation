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

POST.js 사용방법 및 JSON 방식 return 

### 3. 로그인 창 만들기

### 4. 간단한 홈페이지 따라서 만들기
