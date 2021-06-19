from flask import Flask, request

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
    print("test")
    return outputJSON("service is ok", "ok")

@app.route('/login', methods=['POST'])
def login():
    print("로그인 기능 진행")
    ## request.form["id"]
    ## request.form["pw"]
    ## id : "admin", pw : "1234" ==> 로그인 완료! 라고 출력될 수 있게!
    if ( request.form["id"] == "admin" and request.form["pw"] == "1234"):
        return outputJSON("login success", "ok")
    else:
        return outputJSON("false", "ok")


def outputJSON(msg, status="error"):
    return {"data": msg, "status": status}


if __name__ == '__main__':
    app.run(debug=True)