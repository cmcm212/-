from flask import Flask, render_template, request

app = Flask(__name__)

# 배포서술자(deployment descriptor : 함수와 주소의 쌍)
@app.route("/hello")
def aaa():
    # 플라스크 함수의 리턴은 반드시 문자열
    return render_template("index.html")


# 이름을 입력받는 html 파일을 웹앱에 추가하시오.
@app.route("/name", methods=['get'])
def name_input():
    return render_template("name.html")

@app.route("/name", methods=['get'])
def name():
    # get방식 요청 데이터 : request.args
    # post방식 요청 데이터 : request.form
    name = request.form['irum']
    return render_template("name_result.html", name=name)

# 현재 서버의 모든 url을 출력해라
print(app.url_map)

# 실행되는 기본 url : 127.0.0.1:5000
# debug란 개발 모드
app.run(debug=True)